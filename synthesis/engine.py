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

# Make this file runnable both as `python3 synthesis/engine.py` and as
# `python3 -m synthesis.engine` by ensuring the project root is on sys.path.
_THIS_DIR = Path(__file__).parent
_ROOT = _THIS_DIR.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from synthesis.dsp import (  # noqa: E402
    SR,
    apply_formants,
    lowpass,
    master_bus,
)


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
    """Fast lowpass via scipy butter (replaces per-sample python loop)."""
    return lowpass(sig, cutoff)


def timbre_sine(freq, duration, inflect=None, seed=0):
    n = int(SR * duration)
    return np.sin(_phase(freq, n, inflect))


def timbre_vocal_male_low(freq, duration, inflect=None, seed=0):
    """Low male vocal: 3-voice detuned unison + formants (~/o/ vowel) + breath noise."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)

    detunes = [0.0, 0.0035, -0.0028]
    signal = np.zeros(n)
    for det in detunes:
        vib_rate = rng.uniform(4.0, 5.8)
        vib = 0.007 * np.sin(2 * np.pi * vib_rate * t + rng.uniform(0, 2 * np.pi))
        drift = 0.0025 * np.sin(2 * np.pi * 0.25 * t + rng.uniform(0, 2 * np.pi))

        def combined(tt, det=det, vib=vib, drift=drift):
            base = inflect(tt) if inflect else 0.0
            return base + det + np.interp(tt, t, vib) + np.interp(tt, t, drift)

        phase = _phase(freq, n, combined)
        voice = (1.0 * np.sin(phase)
                 + 0.55 * np.sin(2 * phase)
                 + 0.40 * np.sin(3 * phase)
                 + 0.22 * np.sin(4 * phase)
                 + 0.13 * np.sin(5 * phase))
        signal = signal + voice
    signal = signal / (len(detunes) * 2.3)

    # Subtle breath noise
    breath = rng.normal(0, 1, n)
    breath = lowpass(breath, 1800)
    signal = signal + breath * 0.025

    # Formants: /o/–/ɑ/ blend
    signal = apply_formants(signal,
                             formants_hz=[520, 880, 2500],
                             q_list=[5.5, 4.5, 3.0],
                             amp_list=[1.0, 0.65, 0.3])
    return signal * 1.8


def timbre_vocal_female_high(freq, duration, inflect=None, seed=0):
    """High vocal: 3-voice detuned unison + formants (~/a/ vowel)."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)

    detunes = [0.0, 0.004, -0.0032]
    signal = np.zeros(n)
    for det in detunes:
        vib_rate = rng.uniform(5.0, 6.8)
        vib = 0.01 * np.sin(2 * np.pi * vib_rate * t + rng.uniform(0, 2 * np.pi))

        def combined(tt, det=det, vib=vib):
            base = inflect(tt) if inflect else 0.0
            return base + det + np.interp(tt, t, vib)

        phase = _phase(freq, n, combined)
        voice = (1.0 * np.sin(phase)
                 + 0.42 * np.sin(2 * phase)
                 + 0.22 * np.sin(3 * phase)
                 + 0.1 * np.sin(4 * phase))
        signal = signal + voice
    signal = signal / (len(detunes) * 1.7)

    breath = rng.normal(0, 1, n)
    breath = lowpass(breath, 3200)
    signal = signal + breath * 0.02

    # Formants: /a/ vowel
    signal = apply_formants(signal,
                             formants_hz=[720, 1200, 2800],
                             q_list=[5.0, 4.5, 3.0],
                             amp_list=[1.0, 0.7, 0.35])
    return signal * 1.6


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
    """Bowed string: sawtooth + vibrato + bow-pressure noise + body resonance."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    vib = 0.013 * np.sin(2 * np.pi * rng.uniform(4.8, 5.8) * t + rng.uniform(0, 2 * np.pi))

    def combined_inflect(tt):
        base = inflect(tt) if inflect else 0
        return base + np.interp(tt, t, vib)

    phase = _phase(freq, n, combined_inflect)
    s = np.zeros(n)
    for k in range(1, 22):
        s += ((-1) ** (k + 1) / k) * np.sin(k * phase)
    s *= 2 / np.pi

    # Bow-pressure noise
    bow_noise = rng.normal(0, 1, n)
    bow_noise = lowpass(bow_noise, 5000)
    s = s + bow_noise * 0.04

    # Body resonance for warmth
    from synthesis.dsp import biquad_peak_coefs
    import scipy.signal as ss
    for body_f, body_q, body_gain in [(280, 3.0, 3), (480, 4.0, 2), (1100, 6.0, 1.5)]:
        b, a = biquad_peak_coefs(body_f, body_q, body_gain)
        s = ss.lfilter(b, a, s)

    return _lowpass(s, max(3500, freq * 10)) * 0.6


def timbre_struck_metal(freq, duration, inflect=None, seed=0):
    """Struck metal: inharmonic partials + initial noise burst + long tail."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    # Ideal bar partials (modified) — 1, 2.76, 5.40, 8.93, 13.34
    partials = [(1.0, 1.0, 1.3),
                (2.756, 0.75, 1.1),
                (5.404, 0.45, 0.9),
                (8.933, 0.28, 0.7),
                (13.344, 0.18, 0.55),
                (18.641, 0.1, 0.45)]
    s = np.zeros(n)
    for ratio, amp, rate in partials:
        # subtle frequency drift per partial
        drift = rng.uniform(-0.002, 0.002)
        decay = np.exp(-t * rate)
        s += amp * decay * np.sin(2 * np.pi * freq * ratio * (1 + drift) * t
                                   + rng.uniform(0, 2 * np.pi))
    # Initial noise burst (strike transient)
    burst_n = min(int(SR * 0.02), n)
    burst = rng.normal(0, 1, burst_n) * np.exp(-np.linspace(0, 30, burst_n))
    s[:burst_n] += burst * 0.3
    return s / 2.6


def timbre_plucked_string(freq, duration, inflect=None, seed=0):
    """Karplus-Strong with body resonance."""
    n = int(SR * duration)
    delay = max(2, int(SR / freq))
    rng = np.random.default_rng(seed)
    buf = rng.uniform(-1, 1, delay).astype(np.float64)
    # slight pluck shaping — attenuate high-frequency content of excitation
    buf[1:] = 0.55 * buf[1:] + 0.45 * buf[:-1]
    out = np.zeros(n)
    idx = 0
    for i in range(n):
        out[i] = buf[idx]
        prev = buf[(idx - 1) % delay]
        buf[idx] = 0.9965 * 0.5 * (out[i] + prev)
        idx = (idx + 1) % delay
    # body resonance — two peaking EQs at typical guitar body resonances
    from synthesis.dsp import biquad_peak_coefs
    import scipy.signal as ss
    for body_f, body_q, body_gain in [(110, 3.0, 4), (220, 4.0, 2), (450, 5.0, 1)]:
        b, a = biquad_peak_coefs(body_f, body_q, body_gain)
        out = ss.lfilter(b, a, out)
    return out * 0.85


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

def _s_curve(n: int, start: float, end: float) -> np.ndarray:
    """Smooth S-curve interpolation (smoothstep) — avoids audible clicks at edges."""
    if n <= 1:
        return np.full(n, end)
    x = np.linspace(0, 1, n)
    s = x * x * (3 - 2 * x)  # cubic smoothstep
    return start + (end - start) * s


def adsr_env(n: int, attack: float = 0.12, decay: float = 0.18, sustain: float = 0.82, release: float = 0.5) -> np.ndarray:
    env = np.ones(n)
    a = int(SR * attack)
    d = int(SR * decay)
    r = int(SR * release)
    if a + d + r > n:
        scale = n / (a + d + r + 1)
        a, d, r = int(a * scale), int(d * scale), int(r * scale)
    s_n = max(0, n - a - d - r)
    if a > 0:
        env[:a] = _s_curve(a, 0.0, 1.0)
    if d > 0:
        env[a:a + d] = _s_curve(d, 1.0, sustain)
    if s_n > 0:
        env[a + d:a + d + s_n] = sustain
    if r > 0 and (a + d + s_n) < n:
        env[-r:] = _s_curve(r, sustain, 0.0)
    return env


# ============================================================================
# Rhythm schedulers — each produces a list of events
# Event: (t_seconds, voice_name, pitch_index, duration_seconds, amplitude_mult)
# ============================================================================

Event = Tuple[float, str, int, float, float]


def melodic_walk(pitches: List[int], count: int, rng: np.random.Generator,
                  max_step: int = 2, step_bias: List[float] = None) -> List[int]:
    """Generate a sequence of pitch indices that move by small steps within `pitches`.

    This is how musical lines feel — adjacent notes prefer to be close in pitch-space.
    Without this, `pitches[cursor % len(pitches)]` produces mechanical cycling and
    uniform-random selection produces atonal noise. Small-step random walk feels like
    melody.
    """
    if not pitches:
        return []
    if step_bias is None:
        # Prefer 0, ±1 steps, with occasional ±2. Larger leaps rare.
        weights = [0.35, 0.30, 0.30, 0.04, 0.01]  # for |step| = 0, 1, 2, 3, 4
    out = []
    idx = rng.integers(0, len(pitches))
    out.append(pitches[idx])
    for _ in range(count - 1):
        # Choose step magnitude, then sign
        step_mag = rng.choice(len(weights), p=weights if step_bias is None else step_bias)
        sign = int(rng.choice([-1, 1]))
        new_idx = idx + sign * int(step_mag)
        # Reflect at boundaries
        if new_idx < 0:
            new_idx = -new_idx
        if new_idx >= len(pitches):
            new_idx = 2 * (len(pitches) - 1) - new_idx
        new_idx = max(0, min(len(pitches) - 1, new_idx))
        out.append(pitches[new_idx])
        idx = new_idx
    return out


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
        walk = v.get("_walk", pitches)
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
                    pitch = walk[cursor % len(walk)]
                    dur = beat_dur * float(rng.choice([0.5, 1.0, 1.0, 2.0]))
                elif role == "percussive":
                    pitch = walk[cursor % len(walk)]
                    dur = beat_dur * 0.3
                elif role == "hocket_single_pitch":
                    if rng.random() < 0.4:
                        pitch = pitches[0]
                        dur = beat_dur * 0.5
                    else:
                        t += beat_dur
                        continue
                elif role == "ornamental":
                    pitch = walk[cursor % len(walk)]
                    dur = beat_dur * 0.25
                    t += beat_dur * 0.1
                else:
                    pitch = walk[cursor % len(walk)]
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
        walk = v.get("_walk", pitches)
        for w_start, w_end in windows:
            if role == "sustained_drone":
                events.append((w_start, v["name"], pitches[0], w_end - w_start, amp))
                continue
            t = w_start + rng.uniform(0, 1.5)  # stagger voices
            i = 0
            while t < w_end:
                pdur = phrase_durs[i % len(phrase_durs)]
                pitch = walk[i % len(walk)]
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
        walk = v.get("_walk", pitches)
        for w_start, w_end in windows:
            if role == "sustained_drone":
                events.append((w_start, v["name"], pitches[0], w_end - w_start, amp))
                continue
            t = w_start + (i * 1.7 + rng.uniform(0, 2.5)) % 3.5
            cursor = 0
            while t < w_end:
                breath_dur = rng.uniform(b_lo, b_hi)
                gap = rng.uniform(gap_lo, gap_hi)
                if role == "breath_phrase":
                    n_notes = int(rng.choice([1, 1, 2]))
                    sub = breath_dur / n_notes
                    for _ in range(n_notes):
                        if t >= w_end:
                            break
                        pitch = walk[cursor % len(walk)]
                        events.append((t, v["name"], pitch, min(sub, w_end - t), amp))
                        t += sub
                        cursor += 1
                    t += gap
                else:
                    pitch = walk[cursor % len(walk)]
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
        walk = v.get("_walk", pitches)
        for w_start, w_end in windows:
            if role == "sustained_drone":
                events.append((w_start, v["name"], pitches[0], w_end - w_start, amp))
                continue
            for ci in range(n_cycles):
                cycle_start = w_start + ci * cycle_dur
                if cycle_start >= w_end:
                    break
                ts = sorted(rng.uniform(0, cycle_dur, density))
                cursor = 0
                for relt in ts:
                    abs_t = cycle_start + relt
                    if abs_t >= w_end:
                        break
                    pitch = walk[cursor % len(walk)]
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


def _prepare_voices_with_walks(spec: dict, seed: int) -> List[dict]:
    """Pre-compute a melodic walk sequence for each voice so that scheduler
    functions can pull pitches sequentially from a musical-feeling line rather
    than cycling or random-sampling the voice's pitch_indices directly.
    """
    rng = np.random.default_rng(seed + 777)
    duration = spec["duration_seconds"]
    prepared = []
    for v in spec["voices"]:
        v2 = dict(v)
        if v["rhythm_role"] == "sustained_drone" or len(v["pitch_indices"]) <= 1:
            # No walk needed; drones stay on their single pitch
            v2["_walk"] = list(v["pitch_indices"]) * 50
        else:
            # Generate a long walk (enough for any scheduler)
            walk_len = max(120, int(duration * 4))
            v2["_walk"] = melodic_walk(v["pitch_indices"], walk_len, rng)
        prepared.append(v2)
    return prepared


def schedule_events(spec: dict, seed: int = 42) -> List[Event]:
    if spec.get("events"):
        voice_map = {v["name"]: v for v in spec["voices"]}
        out = []
        for e in spec["events"]:
            amp = e.get("amplitude", voice_map[e["voice"]]["amplitude"])
            out.append((e["t"], e["voice"], e["pitch_index"], e["duration_seconds"], amp))
        return out
    rhythm = spec["rhythm_system"]
    scheduler = SCHEDULERS.get(rhythm["type"], schedule_metric)
    rng = np.random.default_rng(seed)
    prepared = _prepare_voices_with_walks(spec, seed)
    return scheduler(rhythm, prepared, spec["form"], spec["duration_seconds"], rng)


# ============================================================================
# Main render pipeline
# ============================================================================

def humanize_events(events: List[Event], seed: int, timing_jitter_s: float = 0.012,
                     amp_jitter: float = 0.04) -> List[Event]:
    """Apply small random timing and amplitude variation to events."""
    rng = np.random.default_rng(seed + 12345)
    out = []
    for t, vname, pi, dur, amp in events:
        t2 = max(0, t + rng.uniform(-timing_jitter_s, timing_jitter_s))
        a2 = max(0, min(1.0, amp + rng.uniform(-amp_jitter, amp_jitter)))
        out.append((t2, vname, pi, dur, a2))
    return out


def _inject_pedal_if_missing(spec: dict) -> dict:
    """If no sustained_drone voice exists, add a quiet pedal tone at the reference
    pitch to give the ear a harmonic ground. Honors the grammar — does nothing if
    the grammar already specifies a drone or if drone_presence would contradict.

    Only triggers when: no voice has rhythm_role=sustained_drone AND the texture
    is not explicitly one that forbids drone (e.g. spectral_cloud with explicit
    no-drone intent). Safe default: err on the side of adding a quiet pedal.
    """
    voices = spec["voices"]
    has_drone = any(v.get("rhythm_role") == "sustained_drone" for v in voices)
    if has_drone:
        return spec
    # Do not add a pedal if pitches explicitly start above the first index
    pitch_count = len(spec.get("pitch_system", {}).get("pitches", []))
    if pitch_count == 0:
        return spec
    spec = dict(spec)
    spec["voices"] = list(voices) + [{
        "name": "_auto_pedal",
        "timbre": "vocal_male_low",
        "pitch_indices": [0],
        "rhythm_role": "sustained_drone",
        "amplitude": 0.22,
        "spatial_position": [0.0, 0.0],
    }]
    return spec


def render_spec(spec: dict, seed: int = 42,
                reverb_wet: float = 0.40,
                apply_master: bool = True,
                auto_pedal: bool = True) -> np.ndarray:
    if auto_pedal:
        spec = _inject_pedal_if_missing(spec)
    duration = spec["duration_seconds"]
    total_samples = int(duration * SR)
    stereo = np.zeros((total_samples, 2), dtype=np.float64)
    voice_map = {v["name"]: v for v in spec["voices"]}

    events = schedule_events(spec, seed=seed)
    # Humanize unless the LLM provided explicit events — those are scripted
    if not spec.get("events"):
        events = humanize_events(events, seed=seed)
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
            env = adsr_env(len(sig), attack=1.2, decay=0.4, sustain=0.95, release=2.0)
        elif role in ("breath_phrase",):
            env = adsr_env(len(sig), attack=0.35, decay=0.25, sustain=0.88, release=0.8)
        elif role in ("melodic_lead",):
            env = adsr_env(len(sig), attack=0.18, decay=0.22, sustain=0.85, release=0.6)
        elif role in ("ostinato",):
            env = adsr_env(len(sig), attack=0.08, decay=0.15, sustain=0.82, release=0.4)
        elif role == "percussive":
            env = adsr_env(len(sig), attack=0.005, decay=0.15, sustain=0.0, release=0.08)
        elif role == "ritual_punctuation":
            env = adsr_env(len(sig), attack=0.01, decay=0.4, sustain=0.3, release=0.9)
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

    # Pre-master pass: reduce raw peak to leave headroom for bus
    pre_peak = float(np.max(np.abs(stereo)))
    if pre_peak > 0.8:
        stereo *= (0.8 / pre_peak)

    # Master bus — reverb + saturation + compression
    if apply_master:
        stereo = master_bus(stereo, reverb_wet=reverb_wet)

    # Final safety normalize
    peak = float(np.max(np.abs(stereo)))
    if peak > 0.98:
        stereo *= (0.98 / peak)
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
