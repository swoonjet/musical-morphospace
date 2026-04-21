"""
Synthesis engine: audio_spec.json → stereo WAV.

Interprets the fields defined in prompts/audio_spec_schema.json and renders a
demonstration. Symbolic-first — the audio is obligated to match the grammar
the LLM declared, not to approximate it. Uses numpy additive synthesis + simple
filtering. Stdlib `wave` module for output to avoid scipy dependency.

Usage:
    python3 engine.py <path_to_spec.json> <path_to_output.wav>
    from engine import render_spec
    samples = render_spec(spec_dict)  # stereo int16 array
"""

import json
import sys
import wave
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

import numpy as np

SR = 44100


# ============================================================================
# Pitch resolution
# ============================================================================

def resolve_pitch(spec: dict, pitch_index: int) -> float:
    ps = spec["pitch_system"]
    enc = ps["encoding"]
    vals = ps["pitches"]
    if pitch_index >= len(vals):
        raise ValueError(f"pitch_index {pitch_index} out of range (pitches has {len(vals)})")
    if enc == "ratio":
        return ps["reference_hz"] * vals[pitch_index]
    if enc == "cents_above_reference":
        return ps["reference_hz"] * 2 ** (vals[pitch_index] / 1200)
    if enc == "hz_absolute":
        return vals[pitch_index]
    raise ValueError(f"Unknown pitch encoding: {enc}")


# ============================================================================
# Inflection — microtonal pitch bends per spec rules
# ============================================================================

def make_inflection(spec: dict, pitch_index: int, seed: int) -> Optional[Callable[[np.ndarray], np.ndarray]]:
    rules = spec["pitch_system"].get("inflection_rules", [])
    for rule in rules:
        if rule["pitch_index"] == pitch_index:
            cents_lo, cents_hi = rule["inflection_cents_range"]
            rng = np.random.default_rng(seed)
            amp_cents = (cents_hi - cents_lo) / 2
            offset_cents = (cents_hi + cents_lo) / 2
            rate = rng.uniform(0.25, 0.6)  # slow breath-pressure-like wobble
            phase = rng.uniform(0, 2 * np.pi)

            def inflect(t: np.ndarray) -> np.ndarray:
                cents = offset_cents + amp_cents * np.sin(2 * np.pi * rate * t + phase)
                return 2 ** (cents / 1200) - 1

            return inflect
    return None


# ============================================================================
# Low-level timbre synthesis
# ============================================================================

def _phase(freq: float, n: int, inflect: Optional[Callable] = None) -> np.ndarray:
    t = np.arange(n) / SR
    if inflect is not None:
        f = freq * (1 + inflect(t))
    else:
        f = np.full(n, freq)
    return 2 * np.pi * np.cumsum(f) / SR


def _lowpass(sig: np.ndarray, cutoff: float) -> np.ndarray:
    rc = 1.0 / (2 * np.pi * cutoff)
    alpha = (1.0 / SR) / (rc + 1.0 / SR)
    out = np.empty_like(sig)
    y = 0.0
    for i in range(len(sig)):
        y = y + alpha * (sig[i] - y)
        out[i] = y
    return out


def timbre_sine(freq, duration, inflect=None, seed=0):
    n = int(SR * duration)
    return np.sin(_phase(freq, n, inflect))


def timbre_vocal_male_low(freq, duration, inflect=None, seed=0):
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    vib_rate = rng.uniform(4.0, 5.5)
    vib = 0.008 * np.sin(2 * np.pi * vib_rate * t)

    def combined_inflect(tt):
        base = inflect(tt) if inflect else 0
        return base + np.interp(tt, t, vib)

    phase = _phase(freq, n, combined_inflect)
    s = 1.0 * np.sin(phase)
    s += 0.55 * np.sin(2 * phase)
    s += 0.40 * np.sin(3 * phase)
    s += 0.22 * np.sin(4 * phase)
    s += 0.13 * np.sin(5 * phase)
    s = _lowpass(s, max(1500, freq * 8))
    return s / 2.3


def timbre_vocal_female_high(freq, duration, inflect=None, seed=0):
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    vib = 0.01 * np.sin(2 * np.pi * rng.uniform(5.0, 6.5) * t)

    def combined_inflect(tt):
        base = inflect(tt) if inflect else 0
        return base + np.interp(tt, t, vib)

    phase = _phase(freq, n, combined_inflect)
    s = 1.0 * np.sin(phase)
    s += 0.4 * np.sin(2 * phase)
    s += 0.2 * np.sin(3 * phase)
    return _lowpass(s, max(2500, freq * 6)) / 1.6


def timbre_overtone_whistle(freq, duration, inflect=None, seed=0):
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    vib = 0.003 * np.sin(2 * np.pi * rng.uniform(3.5, 4.5) * t)

    def combined_inflect(tt):
        base = inflect(tt) if inflect else 0
        return base + np.interp(tt, t, vib)

    phase = _phase(freq, n, combined_inflect)
    return 0.85 * np.sin(phase)


def timbre_bowed_string(freq, duration, inflect=None, seed=0):
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    vib = 0.012 * np.sin(2 * np.pi * rng.uniform(4.8, 5.8) * t)

    def combined_inflect(tt):
        base = inflect(tt) if inflect else 0
        return base + np.interp(tt, t, vib)

    phase = _phase(freq, n, combined_inflect)
    s = np.zeros(n)
    for k in range(1, 18):
        s += ((-1) ** (k + 1) / k) * np.sin(k * phase)
    s *= 2 / np.pi
    return _lowpass(s, max(3500, freq * 10)) * 0.7


def timbre_struck_metal(freq, duration, inflect=None, seed=0):
    n = int(SR * duration)
    t = np.arange(n) / SR
    partials = [(1.0, 1.0, 2.0), (2.76, 0.65, 1.2), (5.40, 0.40, 0.8), (8.93, 0.25, 0.6), (13.34, 0.15, 0.5)]
    s = np.zeros(n)
    for ratio, amp, rate in partials:
        decay = np.exp(-t * rate)
        s += amp * decay * np.sin(2 * np.pi * freq * ratio * t)
    return s / 2.2


def timbre_plucked_string(freq, duration, inflect=None, seed=0):
    # Karplus-Strong
    n = int(SR * duration)
    delay = max(2, int(SR / freq))
    rng = np.random.default_rng(seed)
    buf = rng.uniform(-1, 1, delay).astype(np.float64)
    out = np.zeros(n)
    idx = 0
    for i in range(n):
        out[i] = buf[idx]
        prev = buf[(idx - 1) % delay]
        buf[idx] = 0.996 * 0.5 * (out[i] + prev)
        idx = (idx + 1) % delay
    return out * 0.9


def timbre_breath_noise(freq, duration, inflect=None, seed=0):
    n = int(SR * duration)
    rng = np.random.default_rng(seed)
    noise = rng.uniform(-1, 1, n)
    # Bandpass-ish via lowpass minus lower-lowpass
    lp = _lowpass(noise, max(freq * 3, 600))
    lp2 = _lowpass(noise, max(freq * 0.5, 200))
    return (lp - lp2) * 0.8


def timbre_reed(freq, duration, inflect=None, seed=0):
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    vib = 0.006 * np.sin(2 * np.pi * rng.uniform(4.5, 5.5) * t)

    def combined_inflect(tt):
        base = inflect(tt) if inflect else 0
        return base + np.interp(tt, t, vib)

    phase = _phase(freq, n, combined_inflect)
    s = np.sin(phase) + 0.33 * np.sin(3 * phase) + 0.2 * np.sin(5 * phase) + 0.14 * np.sin(7 * phase)
    return _lowpass(s, max(3000, freq * 6)) / 1.7


def timbre_percussive(freq, duration, inflect=None, seed=0):
    # Noise burst with exponential decay
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    noise = rng.uniform(-1, 1, n)
    pitched = np.sin(2 * np.pi * freq * t) * 0.3
    decay = np.exp(-t * 8)
    return (noise * 0.7 + pitched) * decay


TIMBRES: Dict[str, Callable] = {
    "sine": timbre_sine,
    "vocal_male_low": timbre_vocal_male_low,
    "vocal_female_high": timbre_vocal_female_high,
    "overtone_whistle": timbre_overtone_whistle,
    "bowed_string": timbre_bowed_string,
    "struck_metal": timbre_struck_metal,
    "plucked_string": timbre_plucked_string,
    "breath_noise": timbre_breath_noise,
    "reed": timbre_reed,
    "percussive": timbre_percussive,
}


def get_timbre(name: str) -> Callable:
    if name in TIMBRES:
        return TIMBRES[name]
    # graceful fallback for unseen names
    lower = name.lower()
    for key in TIMBRES:
        if key in lower:
            return TIMBRES[key]
    return TIMBRES["sine"]


# ============================================================================
# Envelope
# ============================================================================

def adsr_env(n: int, attack: float = 0.08, decay: float = 0.15, sustain: float = 0.8, release: float = 0.3) -> np.ndarray:
    env = np.ones(n)
    a = int(SR * attack)
    d = int(SR * decay)
    r = int(SR * release)
    if a + d + r > n:
        # short note — compress envelope
        scale = n / (a + d + r + 1)
        a, d, r = int(a * scale), int(d * scale), int(r * scale)
    s_n = max(0, n - a - d - r)
    if a > 0:
        env[:a] = np.linspace(0, 1, a)
    if d > 0:
        env[a:a + d] = np.linspace(1, sustain, d)
    if s_n > 0:
        env[a + d:a + d + s_n] = sustain
    if r > 0 and (a + d + s_n) < n:
        env[-r:] = np.linspace(sustain, 0, r)
    return env


# ============================================================================
# Rhythm schedulers — each produces a list of events
# Event: (t_seconds, voice_name, pitch_index, duration_seconds, amplitude_mult)
# ============================================================================

Event = Tuple[float, str, int, float, float]


def _active_in_section(voice: dict, section_name: str) -> bool:
    active = voice.get("active_sections")
    if active is None:
        return True
    return section_name in active


def _voice_section_windows(voice: dict, form: dict, duration: float) -> List[Tuple[float, float]]:
    sections = form.get("sections", [])
    if not sections:
        return [(0, duration)]
    windows = []
    for s in sections:
        if _active_in_section(voice, s["name"]):
            windows.append((s["start_seconds"], s["start_seconds"] + s["duration_seconds"]))
    return windows or [(0, duration)]


def schedule_metric(rhythm: dict, voices: List[dict], form: dict, duration: float, rng: np.random.Generator) -> List[Event]:
    events: List[Event] = []
    bpm = rhythm["tempo_bpm"]
    beats_per_cycle = rhythm["beats_per_cycle"]
    beat_dur = 60.0 / bpm
    accent = rhythm.get("accent_pattern", [0.8] * beats_per_cycle)

    for v in voices:
        windows = _voice_section_windows(v, form, duration)
        role = v["rhythm_role"]
        amp = v["amplitude"]
        pitches = v["pitch_indices"]
        for w_start, w_end in windows:
            if role == "sustained_drone":
                events.append((w_start, v["name"], pitches[0], w_end - w_start, amp))
                continue
            t = w_start
            cursor = 0
            while t < w_end:
                beat_in_cycle = int((t / beat_dur) % beats_per_cycle)
                accent_mult = accent[beat_in_cycle] if beat_in_cycle < len(accent) else 0.8
                if role == "ostinato":
                    pitch = pitches[beat_in_cycle % len(pitches)]
                    dur = beat_dur * 0.9
                elif role == "melodic_lead":
                    pitch = pitches[cursor % len(pitches)]
                    dur = beat_dur * float(rng.choice([0.5, 1.0, 1.0, 2.0]))
                elif role == "percussive":
                    pitch = pitches[cursor % len(pitches)]
                    dur = beat_dur * 0.3
                elif role == "hocket_single_pitch":
                    if rng.random() < 0.4:
                        pitch = pitches[0]
                        dur = beat_dur * 0.5
                    else:
                        t += beat_dur
                        continue
                elif role == "ornamental":
                    pitch = pitches[cursor % len(pitches)]
                    dur = beat_dur * 0.25
                    t += beat_dur * 0.1
                else:
                    pitch = pitches[cursor % len(pitches)]
                    dur = beat_dur
                events.append((t, v["name"], pitch, min(dur, w_end - t), amp * accent_mult))
                t += dur
                cursor += 1
    return events


def schedule_additive(rhythm: dict, voices: List[dict], form: dict, duration: float, rng: np.random.Generator) -> List[Event]:
    base_ms = rhythm["base_unit_ms"]
    groupings = rhythm["groupings"]
    unit_s = base_ms / 1000.0
    # build accent pattern: first of each grouping accented
    accent = []
    for g in groupings:
        accent.append(1.0)
        accent.extend([0.55] * (g - 1))
    cycle_units = sum(groupings)
    synthetic_rhythm = {
        "tempo_bpm": 60.0 / unit_s,
        "beats_per_cycle": cycle_units,
        "accent_pattern": accent,
    }
    return schedule_metric(synthetic_rhythm, voices, form, duration, rng)


def schedule_pulse_free(rhythm: dict, voices: List[dict], form: dict, duration: float, rng: np.random.Generator) -> List[Event]:
    events: List[Event] = []
    phrase_durs = rhythm["phrase_durations_seconds"]
    for v in voices:
        windows = _voice_section_windows(v, form, duration)
        role = v["rhythm_role"]
        amp = v["amplitude"]
        pitches = v["pitch_indices"]
        for w_start, w_end in windows:
            if role == "sustained_drone":
                events.append((w_start, v["name"], pitches[0], w_end - w_start, amp))
                continue
            t = w_start + rng.uniform(0, 1.5)  # stagger voices
            i = 0
            while t < w_end:
                pdur = phrase_durs[i % len(phrase_durs)]
                pitch = pitches[i % len(pitches)]
                events.append((t, v["name"], pitch, min(pdur, w_end - t), amp))
                t += pdur + rng.uniform(0.5, 1.5)
                i += 1
    return events


def schedule_breath_based(rhythm: dict, voices: List[dict], form: dict, duration: float, rng: np.random.Generator) -> List[Event]:
    events: List[Event] = []
    b_lo, b_hi = rhythm["breath_duration_range_seconds"]
    gap_lo, gap_hi = rhythm.get("between_breaths_seconds", [0.4, 1.2])

    for i, v in enumerate(voices):
        windows = _voice_section_windows(v, form, duration)
        role = v["rhythm_role"]
        amp = v["amplitude"]
        pitches = v["pitch_indices"]
        for w_start, w_end in windows:
            if role == "sustained_drone":
                # True drone: one event spanning the window
                events.append((w_start, v["name"], pitches[0], w_end - w_start, amp))
                continue
            # breath-based voices stagger their cycles
            t = w_start + (i * 1.7 + rng.uniform(0, 2.5)) % 3.5
            cursor = 0
            while t < w_end:
                breath_dur = rng.uniform(b_lo, b_hi)
                gap = rng.uniform(gap_lo, gap_hi)
                if role == "breath_phrase":
                    # 1 or 2 pitches per breath
                    n_notes = int(rng.choice([1, 1, 2]))
                    sub = breath_dur / n_notes
                    for _ in range(n_notes):
                        if t >= w_end:
                            break
                        pitch = pitches[cursor % len(pitches)]
                        events.append((t, v["name"], pitch, min(sub, w_end - t), amp))
                        t += sub
                        cursor += 1
                    t += gap
                else:
                    pitch = pitches[cursor % len(pitches)]
                    events.append((t, v["name"], pitch, min(breath_dur, w_end - t), amp))
                    t += breath_dur + gap
                cursor += 1
    return events


def schedule_cyclical_nonmetric(rhythm: dict, voices: List[dict], form: dict, duration: float, rng: np.random.Generator) -> List[Event]:
    events: List[Event] = []
    cycle_dur = rhythm["cycle_duration_seconds"]
    density = rhythm["event_density_per_cycle"]
    n_cycles = rhythm.get("cycle_count", max(1, int(duration / cycle_dur)))

    for v in voices:
        windows = _voice_section_windows(v, form, duration)
        role = v["rhythm_role"]
        amp = v["amplitude"]
        pitches = v["pitch_indices"]
        for w_start, w_end in windows:
            if role == "sustained_drone":
                events.append((w_start, v["name"], pitches[0], w_end - w_start, amp))
                continue
            for ci in range(n_cycles):
                cycle_start = w_start + ci * cycle_dur
                if cycle_start >= w_end:
                    break
                # distribute events (roughly exponential gaps)
                ts = sorted(rng.uniform(0, cycle_dur, density))
                cursor = 0
                for relt in ts:
                    abs_t = cycle_start + relt
                    if abs_t >= w_end:
                        break
                    pitch = pitches[cursor % len(pitches)]
                    note_dur = cycle_dur / density * rng.uniform(0.6, 1.4)
                    events.append((abs_t, v["name"], pitch, min(note_dur, w_end - abs_t), amp))
                    cursor += 1
    return events


def schedule_ritual_cued(rhythm: dict, voices: List[dict], form: dict, duration: float, rng: np.random.Generator) -> List[Event]:
    events: List[Event] = []
    cues = rhythm["cue_points_seconds"]
    for v in voices:
        windows = _voice_section_windows(v, form, duration)
        role = v["rhythm_role"]
        amp = v["amplitude"]
        pitches = v["pitch_indices"]
        for w_start, w_end in windows:
            if role == "sustained_drone":
                events.append((w_start, v["name"], pitches[0], w_end - w_start, amp))
                continue
            # events between cues
            bounds = [w_start] + [c for c in cues if w_start < c < w_end] + [w_end]
            for a, b in zip(bounds, bounds[1:]):
                # one event per segment
                pitch = pitches[rng.integers(0, len(pitches))]
                events.append((a + 0.3, v["name"], int(pitch), (b - a) * 0.7, amp))
                if role == "ritual_punctuation":
                    # extra hit at cue
                    events.append((a, v["name"], pitches[0], 0.4, amp * 0.9))
    return events


def schedule_indeterminate(rhythm: dict, voices: List[dict], form: dict, duration: float, rng: np.random.Generator) -> List[Event]:
    # Treat as sparse event cloud
    synthetic = {
        "cycle_duration_seconds": duration,
        "event_density_per_cycle": 24,
        "cycle_count": 1,
    }
    return schedule_cyclical_nonmetric(synthetic, voices, form, duration, rng)


SCHEDULERS = {
    "metric": schedule_metric,
    "additive": schedule_additive,
    "pulse_free": schedule_pulse_free,
    "breath_based": schedule_breath_based,
    "cyclical_nonmetric": schedule_cyclical_nonmetric,
    "ritual_cued": schedule_ritual_cued,
    "indeterminate_proportional": schedule_indeterminate,
}


def schedule_events(spec: dict, seed: int = 42) -> List[Event]:
    if spec.get("events"):
        # use explicit events, resolving amplitude defaults
        voice_map = {v["name"]: v for v in spec["voices"]}
        out = []
        for e in spec["events"]:
            amp = e.get("amplitude", voice_map[e["voice"]]["amplitude"])
            out.append((e["t"], e["voice"], e["pitch_index"], e["duration_seconds"], amp))
        return out
    rhythm = spec["rhythm_system"]
    scheduler = SCHEDULERS.get(rhythm["type"], schedule_metric)
    rng = np.random.default_rng(seed)
    return scheduler(rhythm, spec["voices"], spec["form"], spec["duration_seconds"], rng)


# ============================================================================
# Main render pipeline
# ============================================================================

def render_spec(spec: dict, seed: int = 42) -> np.ndarray:
    duration = spec["duration_seconds"]
    total_samples = int(duration * SR)
    stereo = np.zeros((total_samples, 2), dtype=np.float64)
    voice_map = {v["name"]: v for v in spec["voices"]}

    events = schedule_events(spec, seed=seed)
    print(f"  scheduled {len(events)} events")

    for ev_idx, (t, vname, pi, dur, amp) in enumerate(events):
        if t >= duration or dur <= 0:
            continue
        voice = voice_map.get(vname)
        if not voice:
            continue
        freq = resolve_pitch(spec, pi)
        timbre_fn = get_timbre(voice["timbre"])
        inflect = make_inflection(spec, pi, seed + ev_idx * 17)
        actual_dur = min(dur, duration - t)
        sig = timbre_fn(freq, actual_dur, inflect=inflect, seed=seed + ev_idx)

        # envelope — longer release for sustained roles
        role = voice.get("rhythm_role", "")
        if role in ("sustained_drone",):
            env = adsr_env(len(sig), attack=0.6, decay=0.3, sustain=0.95, release=1.2)
        elif role in ("breath_phrase", "melodic_lead"):
            env = adsr_env(len(sig), attack=0.15, decay=0.2, sustain=0.85, release=0.4)
        elif role == "percussive":
            env = adsr_env(len(sig), attack=0.005, decay=0.2, sustain=0.0, release=0.05)
        else:
            env = adsr_env(len(sig))
        sig = sig * env * amp

        # spatial panning
        pos = voice.get("spatial_position", [0.0, 0.0])
        pan = float(pos[0])
        pan = max(-1.0, min(1.0, pan))
        left_gain = np.sqrt((1 - pan) / 2)
        right_gain = np.sqrt((1 + pan) / 2)

        start = int(t * SR)
        end = min(start + len(sig), total_samples)
        n = end - start
        stereo[start:end, 0] += sig[:n] * left_gain
        stereo[start:end, 1] += sig[:n] * right_gain

    # Normalize to prevent clipping
    peak = float(np.max(np.abs(stereo)))
    if peak > 0.97:
        stereo *= (0.97 / peak)
    print(f"  peak amplitude: {peak:.3f}")

    # to int16
    return (stereo * 32767).astype(np.int16)


def write_wav(samples: np.ndarray, path: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    n_channels = samples.shape[1] if samples.ndim == 2 else 1
    with wave.open(str(path), "wb") as w:
        w.setnchannels(n_channels)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(samples.tobytes())


# ============================================================================
# Spec loading — can read .json directly or extract from markdown code block
# ============================================================================

def load_spec(path: str) -> dict:
    text = Path(path).read_text()
    if path.endswith(".json"):
        return json.loads(text)
    # extract fenced ```json block from markdown
    import re
    m = re.search(r"```json\s*\n(.*?)\n```", text, re.DOTALL)
    if not m:
        raise ValueError(f"No ```json block found in {path}")
    return json.loads(m.group(1))


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 engine.py <spec.json|spec.md> <output.wav> [seed]")
        sys.exit(1)
    spec_path = sys.argv[1]
    out_path = sys.argv[2]
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42

    print(f"Loading spec: {spec_path}")
    spec = load_spec(spec_path)
    print(f"  duration: {spec['duration_seconds']}s")
    print(f"  rhythm: {spec['rhythm_system']['type']}")
    print(f"  voices: {[v['name'] for v in spec['voices']]}")
    print(f"  sections: {[s['name'] for s in spec['form']['sections']]}")

    samples = render_spec(spec, seed=seed)
    write_wav(samples, out_path)
    print(f"Wrote {out_path} ({samples.shape[0] / SR:.1f}s, {samples.shape[1]} ch)")


if __name__ == "__main__":
    main()
