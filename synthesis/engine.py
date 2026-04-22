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
    """Low male vocal: 3-voice detuned unison + /o/ formants. Warmer than v1 —
    4th+5th harmonics reduced to remove harsh upper-mid content."""
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
        # Reduced upper harmonics to soften the tone
        voice = (1.0 * np.sin(phase)
                 + 0.50 * np.sin(2 * phase)
                 + 0.28 * np.sin(3 * phase)
                 + 0.10 * np.sin(4 * phase))
        signal = signal + voice
    signal = signal / (len(detunes) * 2.0)

    breath = rng.normal(0, 1, n)
    breath = lowpass(breath, 1600)
    signal = signal + breath * 0.022

    # Formants: /o/ vowel, slightly wider Q for warmth
    signal = apply_formants(signal,
                             formants_hz=[480, 820, 2400],
                             q_list=[5.5, 4.5, 3.0],
                             amp_list=[1.0, 0.55, 0.22])
    # Gentle LPF to tame any remaining brightness
    signal = lowpass(signal, 3500)
    return signal * 1.9


def timbre_vocal_female_high(freq, duration, inflect=None, seed=0):
    """High vocal: 3-voice detuned unison + /a/ formants. Less bright than v1."""
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
                 + 0.38 * np.sin(2 * phase)
                 + 0.16 * np.sin(3 * phase))
        signal = signal + voice
    signal = signal / (len(detunes) * 1.55)

    breath = rng.normal(0, 1, n)
    breath = lowpass(breath, 2800)
    signal = signal + breath * 0.018

    # Formants: /a/ vowel
    signal = apply_formants(signal,
                             formants_hz=[680, 1150, 2700],
                             q_list=[5.0, 4.5, 3.0],
                             amp_list=[1.0, 0.6, 0.25])
    signal = lowpass(signal, 4200)
    return signal * 1.7


def timbre_bamboo_flute(freq, duration, inflect=None, seed=0):
    """Bamboo/shakuhachi-ish flute: fundamental + octave + breath noise + slight vibrato."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    vib = 0.006 * np.sin(2 * np.pi * rng.uniform(4.5, 5.5) * t + rng.uniform(0, 2 * np.pi))

    def combined(tt):
        base = inflect(tt) if inflect else 0.0
        return base + np.interp(tt, t, vib)

    phase = _phase(freq, n, combined)
    # Flute-like: strong fundamental, weak octave, minimal higher content
    s = (1.0 * np.sin(phase)
         + 0.22 * np.sin(2 * phase)
         + 0.05 * np.sin(3 * phase))
    # Air noise modulated by fundamental amplitude (breathy)
    noise = rng.normal(0, 1, n)
    noise = lowpass(noise, min(freq * 5, 3500))
    noise = noise - lowpass(noise, 300)
    s = s + noise * 0.15
    # Soft LPF
    s = lowpass(s, max(freq * 3, 2500))
    return s * 0.9


def timbre_plucked_gut(freq, duration, inflect=None, seed=0):
    """Gut string (oud/lute family): Karplus-Strong with faster decay + mellow body."""
    n = int(SR * duration)
    delay = max(2, int(SR / freq))
    rng = np.random.default_rng(seed)
    buf = rng.uniform(-1, 1, delay).astype(np.float64)
    buf[1:] = 0.4 * buf[1:] + 0.6 * buf[:-1]  # softer pluck
    out = np.zeros(n)
    idx = 0
    decay_coef = 0.9945  # faster decay than steel plucked_string
    for i in range(n):
        out[i] = buf[idx]
        prev = buf[(idx - 1) % delay]
        buf[idx] = decay_coef * 0.5 * (out[i] + prev)
        idx = (idx + 1) % delay
    # Body resonance: warmer lower resonances
    from synthesis.dsp import biquad_peak_coefs
    import scipy.signal as ss
    for body_f, body_q, body_gain in [(95, 3.0, 3.5), (180, 3.5, 2), (380, 5.0, 1)]:
        b, a = biquad_peak_coefs(body_f, body_q, body_gain)
        out = ss.lfilter(b, a, out)
    out = lowpass(out, 2800)
    return out * 0.8


def timbre_low_wood(freq, duration, inflect=None, seed=0):
    """Wooden-block / log drum: damped inharmonic pitched burst with strong body thump."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    # Two partials only, short decay
    s = (1.0 * np.exp(-t * 18) * np.sin(2 * np.pi * freq * t)
         + 0.5 * np.exp(-t * 28) * np.sin(2 * np.pi * freq * 2.3 * t + rng.uniform(0, 2 * np.pi)))
    # Initial thump
    thump_n = min(int(SR * 0.015), n)
    thump = rng.normal(0, 1, thump_n) * np.exp(-np.linspace(0, 25, thump_n))
    s[:thump_n] += thump * 0.5
    return lowpass(s, 2000) * 0.95


def timbre_chimes(freq, duration, inflect=None, seed=0):
    """Tubular bell / chime: inharmonic partials with long decay. Bright but mellowed."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    # Tubular bell partial ratios (mode frequencies of a pipe)
    partials = [(0.5, 0.55, 0.9),
                (1.0, 1.0, 0.8),
                (2.0, 0.8, 1.0),
                (3.02, 0.45, 0.9),
                (4.18, 0.25, 0.95)]
    s = np.zeros(n)
    for ratio, amp, rate in partials:
        decay = np.exp(-t * rate)
        s += amp * decay * np.sin(2 * np.pi * freq * ratio * t + rng.uniform(0, 2 * np.pi))
    # Reduced initial burst — softer strike
    burst_n = min(int(SR * 0.008), n)
    burst = rng.normal(0, 1, burst_n) * np.exp(-np.linspace(0, 40, burst_n))
    s[:burst_n] += burst * 0.15
    # Tame the brightness
    s = lowpass(s, 4500)
    return s * 0.55


def timbre_soft_pad(freq, duration, inflect=None, seed=0):
    """Soft synth-pad: slow-moving detuned oscillators with airy filtered noise."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    # 5-voice detune spread for width
    detunes = [0.0, 0.006, -0.005, 0.009, -0.007]
    signal = np.zeros(n)
    for det in detunes:
        drift = 0.003 * np.sin(2 * np.pi * rng.uniform(0.15, 0.35) * t + rng.uniform(0, 2 * np.pi))

        def combined(tt, det=det, drift=drift):
            base = inflect(tt) if inflect else 0.0
            return base + det + np.interp(tt, t, drift)

        phase = _phase(freq, n, combined)
        voice = (1.0 * np.sin(phase)
                 + 0.35 * np.sin(2 * phase)
                 + 0.12 * np.sin(3 * phase))
        signal = signal + voice
    signal = signal / len(detunes) * 0.7
    # Slow-moving air
    air = rng.normal(0, 1, n)
    air = lowpass(air, 2200)
    air = air - lowpass(air, 400)
    signal = signal + air * 0.04
    signal = lowpass(signal, 3200)
    return signal * 0.85


def timbre_membrane_drum(freq, duration, inflect=None, seed=0):
    """Membrane drum (tabla/frame drum): noise burst + damped fundamental + body."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    # Body fundamental with quick decay
    body = 1.0 * np.exp(-t * 12) * np.sin(2 * np.pi * freq * t)
    # Second mode slightly detuned
    body2 = 0.4 * np.exp(-t * 22) * np.sin(2 * np.pi * freq * 1.6 * t + rng.uniform(0, 2 * np.pi))
    s = body + body2
    # Strike burst
    burst_n = min(int(SR * 0.015), n)
    burst = rng.normal(0, 1, burst_n) * np.exp(-np.linspace(0, 20, burst_n))
    s[:burst_n] += burst * 0.7
    s = lowpass(s, 1800)
    return s * 0.95


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
    """Struck metal (bowl/gong): warmer than v1 — higher partials damped more aggressively."""
    n = int(SR * duration)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    # Ideal bar partials with much faster decay on higher modes
    partials = [(1.0, 1.0, 1.0),
                (2.756, 0.55, 1.3),
                (5.404, 0.22, 1.6),
                (8.933, 0.10, 2.0),
                (13.344, 0.04, 2.6)]
    s = np.zeros(n)
    for ratio, amp, rate in partials:
        drift = rng.uniform(-0.002, 0.002)
        decay = np.exp(-t * rate)
        s += amp * decay * np.sin(2 * np.pi * freq * ratio * (1 + drift) * t
                                   + rng.uniform(0, 2 * np.pi))
    # Softer initial burst
    burst_n = min(int(SR * 0.012), n)
    burst = rng.normal(0, 1, burst_n) * np.exp(-np.linspace(0, 35, burst_n))
    s[:burst_n] += burst * 0.18
    # Mellow LPF to keep it warm
    s = lowpass(s, max(3500, freq * 6))
    return s / 2.4


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
    "plucked_gut": timbre_plucked_gut,
    "bamboo_flute": timbre_bamboo_flute,
    "low_wood": timbre_low_wood,
    "chimes": timbre_chimes,
    "soft_pad": timbre_soft_pad,
    "membrane_drum": timbre_membrane_drum,
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


def _arched_phrase(pitches: List[int], length: int, start_idx: int,
                    rng: np.random.Generator) -> List[int]:
    """Generate one phrase with rise-peak-fall shape within the pitch set.

    A musical phrase tends to: begin near a home pitch, rise to a peak around
    40-65% through, then descend and resolve near (or back at) the home pitch.
    This mirrors how the ear expects phrases to unfold and makes even unusual
    scales feel intentional.
    """
    if length <= 0 or not pitches:
        return []
    out = []
    peak_pos = rng.uniform(0.35, 0.65)
    peak_ceiling = max(3, min(6, len(pitches)))
    peak_reach = int(rng.integers(2, peak_ceiling)) if peak_ceiling > 2 else 2
    idx = start_idx
    for i in range(length):
        frac = i / max(length - 1, 1)
        # Target index follows a skewed arc: rise to peak, then fall
        if frac < peak_pos:
            target = start_idx + (peak_reach * frac / peak_pos)
        else:
            # Fall back toward start with a slight undershoot-overshoot allowed
            target = start_idx + peak_reach * (1 - (frac - peak_pos) / (1 - peak_pos))
        # Add small random deviation so phrases aren't identical
        jitter = rng.normal(0, 0.7)
        desired = target + jitter
        # Small step from previous: never leap by more than 2-3
        diff = desired - idx
        step = int(np.clip(np.round(diff), -2, 2))
        # 25% chance of holding (no change)
        if rng.random() < 0.25:
            step = 0
        new_idx = idx + step
        # Reflect at boundaries
        if new_idx < 0:
            new_idx = -new_idx
        if new_idx >= len(pitches):
            new_idx = 2 * (len(pitches) - 1) - new_idx
        new_idx = max(0, min(len(pitches) - 1, new_idx))
        out.append(pitches[new_idx])
        idx = new_idx
    return out


def melodic_walk(pitches: List[int], count: int, rng: np.random.Generator,
                  phrase_length_range: Tuple[int, int] = (4, 8)) -> List[int]:
    """Generate a long sequence of pitch indices organized into arched phrases.

    Unlike a pure random walk, this produces sequences with rise-peak-fall
    phrase shapes separated by implicit cadences. Adjacent phrases share the
    starting pitch so phrase boundaries feel resolved rather than arbitrary.
    """
    if not pitches:
        return []
    out = []
    home_idx = rng.integers(0, max(1, len(pitches) // 2))  # home near bottom of range
    while len(out) < count:
        ph_len = int(rng.integers(phrase_length_range[0], phrase_length_range[1] + 1))
        phrase = _arched_phrase(pitches, ph_len, home_idx, rng)
        out.extend(phrase)
        # Occasionally shift home for variety — stay close to original
        if rng.random() < 0.3:
            shift = int(rng.choice([-1, 0, 1]))
            home_idx = max(0, min(len(pitches) - 1, home_idx + shift))
    return out[:count]


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


def _chord_tones_at_time(t: float, form: dict) -> Optional[List[int]]:
    """Return the chord_tones of the section containing t, or None. Sections may
    declare a `chord_tones` array (indices into pitch_system.pitches). Voices
    without scripted events will be biased toward these pitches — giving the
    ensemble real harmonic alignment on each section."""
    for s in form.get("sections", []):
        if s["start_seconds"] <= t < s["start_seconds"] + s["duration_seconds"]:
            return s.get("chord_tones")
    return None


def _snap_to_chord(pitch_idx: int, chord_tones: Optional[List[int]],
                    voice_pitches: List[int], bias: float,
                    rng: np.random.Generator) -> int:
    """With probability `bias`, move pitch_idx to the nearest chord tone the
    voice is allowed to play. Otherwise pass through (produces passing tones)."""
    if not chord_tones or rng.random() > bias:
        return pitch_idx
    allowed = [c for c in chord_tones if c in voice_pitches]
    if not allowed:
        return pitch_idx
    return min(allowed, key=lambda c: abs(c - pitch_idx))


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
                chord_tones = _chord_tones_at_time(t, form)
                if role == "ostinato":
                    # Cycle chord tones if provided, else the voice's pitch pool
                    allowed = [c for c in (chord_tones or []) if c in pitches]
                    pool = allowed if allowed else pitches
                    pitch = pool[beat_in_cycle % len(pool)]
                    dur = beat_dur * 0.9
                elif role == "melodic_lead":
                    pitch = walk[cursor % len(walk)]
                    # Strong snap on cycle downbeats, weak otherwise
                    bias = 0.85 if beat_in_cycle == 0 else 0.35
                    pitch = _snap_to_chord(pitch, chord_tones, pitches, bias, rng)
                    dur = beat_dur * float(rng.choice([0.5, 1.0, 1.0, 2.0]))
                elif role == "percussive":
                    pitch = walk[cursor % len(walk)]
                    # Fire one hit per beat; the hit itself is short.
                    hit_dur = beat_dur * 0.3
                    events.append((t, v["name"], pitch, min(hit_dur, w_end - t), amp * accent_mult))
                    t += beat_dur
                    cursor += 1
                    continue
                elif role == "hocket_single_pitch":
                    if rng.random() < 0.4:
                        pitch = pitches[0]
                        dur = beat_dur * 0.5
                    else:
                        t += beat_dur
                        continue
                elif role == "ornamental":
                    pitch = walk[cursor % len(walk)]
                    pitch = _snap_to_chord(pitch, chord_tones, pitches, 0.5, rng)
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
    """Hybrid: scripted events fire as written. Voices with NO scripted events
    get populated by the procedural scheduler so they still contribute (drums,
    drones, pad). Voices that have any scripted events are trusted to be
    fully scripted — the scheduler does not fill gaps for them."""
    scripted: List[Event] = []
    scripted_voices: set = set()
    voice_map = {v["name"]: v for v in spec["voices"]}

    for e in spec.get("events", []) or []:
        amp = e.get("amplitude", voice_map[e["voice"]]["amplitude"])
        scripted.append((e["t"], e["voice"], e["pitch_index"], e["duration_seconds"], amp))
        scripted_voices.add(e["voice"])

    # Voices with no scripted events go through the scheduler
    unscripted_voices = [v for v in spec["voices"] if v["name"] not in scripted_voices]
    scheduled: List[Event] = []
    if unscripted_voices:
        rhythm = spec["rhythm_system"]
        scheduler = SCHEDULERS.get(rhythm["type"], schedule_metric)
        rng = np.random.default_rng(seed)
        # Only pass the unscripted voices through the walk/scheduler pipeline
        sub_spec = dict(spec)
        sub_spec["voices"] = unscripted_voices
        prepared = _prepare_voices_with_walks(sub_spec, seed)
        scheduled = scheduler(rhythm, prepared, spec["form"], spec["duration_seconds"], rng)

    return scripted + scheduled


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
                reverb_wet: float = 0.28,
                apply_master: bool = True,
                auto_pedal: bool = True) -> np.ndarray:
    # Spec can opt out of the auto-pedal when the grammar says drone should be absent
    if spec.get("auto_pedal") is False:
        auto_pedal = False
    if auto_pedal:
        spec = _inject_pedal_if_missing(spec)
    duration = spec["duration_seconds"]
    total_samples = int(duration * SR)
    stereo = np.zeros((total_samples, 2), dtype=np.float64)
    voice_map = {v["name"]: v for v in spec["voices"]}

    # Partition scripted vs scheduled so we humanize only the scheduled ones
    scripted_voices = {e["voice"] for e in (spec.get("events") or [])}
    all_events = schedule_events(spec, seed=seed)
    scripted = [e for e in all_events if e[1] in scripted_voices]
    scheduled = [e for e in all_events if e[1] not in scripted_voices]
    if scheduled:
        scheduled = humanize_events(scheduled, seed=seed)
    events = scripted + scheduled
    print(f"  events: {len(scripted)} scripted + {len(scheduled)} scheduled")

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

    # Pre-master: bring summed mix to ~0.6 peak so reverb has headroom.
    pre_peak = float(np.max(np.abs(stereo)))
    if pre_peak > 0.6:
        stereo *= (0.6 / pre_peak)

    # Master bus — HPF + reverb + gentle HF rolloff. No saturation, no comp.
    if apply_master:
        stereo = master_bus(stereo, reverb_wet=reverb_wet)

    # Normalize to standard mastered level (-1 dBFS ≈ 0.89).
    # Nothing above 0dBFS, no saturation, so laptop speakers see a clean signal.
    peak = float(np.max(np.abs(stereo)))
    target = 0.89
    if peak > 0:
        stereo *= (target / peak)
    print(f"  mix peak: {peak:.3f} → normalized to {target}")

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
