"""DSP primitives used by the synthesis engine.

Biquad filtering, formant shaping, simple reverb, peak compressor, tanh
saturation. All use scipy.signal where appropriate for speed.
"""

import numpy as np
from scipy import signal as sig

SR = 44100


# ----------------------------------------------------------------------------
# Biquad filters
# ----------------------------------------------------------------------------

def biquad_bandpass_coefs(freq: float, q: float, sr: int = SR):
    """Biquad bandpass (constant 0dB peak gain, RBJ cookbook)."""
    w0 = 2 * np.pi * freq / sr
    cos_w0 = np.cos(w0)
    sin_w0 = np.sin(w0)
    alpha = sin_w0 / (2 * q)
    b0, b1, b2 = alpha, 0.0, -alpha
    a0 = 1 + alpha
    a1 = -2 * cos_w0
    a2 = 1 - alpha
    return np.array([b0, b1, b2]) / a0, np.array([1.0, a1 / a0, a2 / a0])


def biquad_peak_coefs(freq: float, q: float, gain_db: float, sr: int = SR):
    """Biquad peaking EQ (RBJ cookbook)."""
    A = 10 ** (gain_db / 40)
    w0 = 2 * np.pi * freq / sr
    cos_w0 = np.cos(w0)
    alpha = np.sin(w0) / (2 * q)
    b0 = 1 + alpha * A
    b1 = -2 * cos_w0
    b2 = 1 - alpha * A
    a0 = 1 + alpha / A
    a1 = -2 * cos_w0
    a2 = 1 - alpha / A
    return np.array([b0, b1, b2]) / a0, np.array([1.0, a1 / a0, a2 / a0])


def highpass(signal_in: np.ndarray, cutoff: float, order: int = 2, sr: int = SR):
    b, a = sig.butter(order, cutoff / (sr / 2), btype="highpass")
    return sig.lfilter(b, a, signal_in, axis=0)


def lowpass(signal_in: np.ndarray, cutoff: float, order: int = 2, sr: int = SR):
    b, a = sig.butter(order, min(cutoff / (sr / 2), 0.99), btype="lowpass")
    return sig.lfilter(b, a, signal_in, axis=0)


def apply_formants(signal_in: np.ndarray, formants_hz, q_list=None, amp_list=None, sr: int = SR):
    """Apply parallel formant bandpasses to a signal."""
    if q_list is None:
        q_list = [6.0] * len(formants_hz)
    if amp_list is None:
        amp_list = [1.0] * len(formants_hz)
    out = np.zeros_like(signal_in)
    for freq, q, amp in zip(formants_hz, q_list, amp_list):
        b, a = biquad_bandpass_coefs(freq, q, sr)
        out = out + amp * sig.lfilter(b, a, signal_in)
    return out / max(sum(amp_list), 1.0)


# ----------------------------------------------------------------------------
# Reverb (FFT convolution with a synthesized IR)
# ----------------------------------------------------------------------------

_ir_cache = {}


def synth_impulse_response(length_s: float = 1.8, decay_rate: float = 4.5,
                            early_reflection_count: int = 5, seed: int = 777,
                            sr: int = SR) -> np.ndarray:
    """Generate a stereo impulse response: dense noise tail with early reflections."""
    key = (length_s, decay_rate, early_reflection_count, seed)
    if key in _ir_cache:
        return _ir_cache[key]

    rng = np.random.default_rng(seed)
    n = int(length_s * sr)
    t = np.arange(n) / sr
    env = np.exp(-decay_rate * t)
    # dense late field — uncorrelated noise * envelope, slight HF rolloff
    noise_l = rng.normal(0, 1, n) * env
    noise_r = rng.normal(0, 1, n) * env
    ir_l = lowpass(noise_l, 6500)
    ir_r = lowpass(noise_r, 6500)

    # early reflection taps
    for i in range(early_reflection_count):
        tap_time = rng.uniform(0.005, 0.07)
        tap_amp = rng.uniform(0.4, 0.9) * np.exp(-decay_rate * tap_time)
        idx = int(tap_time * sr)
        if idx < n:
            if rng.random() < 0.5:
                ir_l[idx] += tap_amp * rng.choice([1, -1])
            else:
                ir_r[idx] += tap_amp * rng.choice([1, -1])

    # normalize so RMS of IR is reasonable
    rms = np.sqrt(np.mean(ir_l ** 2 + ir_r ** 2) / 2)
    if rms > 0:
        ir_l = ir_l / rms * 0.15
        ir_r = ir_r / rms * 0.15

    ir = np.stack([ir_l, ir_r], axis=1)
    _ir_cache[key] = ir
    return ir


def apply_reverb(stereo: np.ndarray, wet: float = 0.3, length_s: float = 1.8,
                 decay_rate: float = 4.5, sr: int = SR) -> np.ndarray:
    if wet <= 0:
        return stereo
    ir = synth_impulse_response(length_s=length_s, decay_rate=decay_rate, sr=sr)
    wet_l = sig.fftconvolve(stereo[:, 0], ir[:, 0])[:len(stereo)]
    wet_r = sig.fftconvolve(stereo[:, 1], ir[:, 1])[:len(stereo)]
    wet_sig = np.stack([wet_l, wet_r], axis=1)
    # Match wet RMS to dry RMS so the reverb adds "space" at equivalent energy
    # rather than amplifying. Without this, FFT convolution with a long IR
    # produces wet peaks 10-20× the dry peak.
    dry_rms = np.sqrt(np.mean(stereo ** 2))
    wet_rms = np.sqrt(np.mean(wet_sig ** 2))
    if wet_rms > 1e-9:
        wet_sig = wet_sig * (dry_rms / wet_rms)
    return stereo * (1 - wet) + wet_sig * wet


# ----------------------------------------------------------------------------
# Compressor
# ----------------------------------------------------------------------------

def compress(stereo: np.ndarray, threshold: float = 0.5, ratio: float = 3.0,
             attack_ms: float = 5.0, release_ms: float = 80.0,
             sr: int = SR, makeup_db: float = 2.0) -> np.ndarray:
    """Simple feed-forward peak compressor with attack/release smoothing."""
    # Peak envelope across channels
    peak = np.max(np.abs(stereo), axis=1)
    # Attack/release one-pole
    a_attack = 1 - np.exp(-1.0 / (sr * attack_ms / 1000.0))
    a_release = 1 - np.exp(-1.0 / (sr * release_ms / 1000.0))
    env = np.zeros_like(peak)
    prev = 0.0
    for i in range(len(peak)):
        tgt = peak[i]
        coef = a_attack if tgt > prev else a_release
        prev = prev + coef * (tgt - prev)
        env[i] = prev
    # Gain reduction
    over = np.maximum(env - threshold, 0)
    gain_reduction = over * (1 - 1 / ratio) / np.maximum(env, 1e-9)
    gain = (1 - gain_reduction) * 10 ** (makeup_db / 20)
    return stereo * gain[:, None]


# ----------------------------------------------------------------------------
# Saturation
# ----------------------------------------------------------------------------

def soft_saturate(stereo: np.ndarray, drive: float = 1.2) -> np.ndarray:
    """Tape-style soft saturation via tanh."""
    return np.tanh(stereo * drive) / np.tanh(drive)


# ----------------------------------------------------------------------------
# Master bus
# ----------------------------------------------------------------------------

def notch(signal_in: np.ndarray, freq: float, q: float = 4.0, sr: int = SR):
    """Narrow notch filter at `freq` to carve out harsh frequency ranges."""
    w0 = 2 * np.pi * freq / sr
    cos_w0 = np.cos(w0)
    sin_w0 = np.sin(w0)
    alpha = sin_w0 / (2 * q)
    b0, b1, b2 = 1, -2 * cos_w0, 1
    a0 = 1 + alpha
    a1 = -2 * cos_w0
    a2 = 1 - alpha
    b = np.array([b0, b1, b2]) / a0
    a = np.array([1.0, a1 / a0, a2 / a0])
    return sig.lfilter(b, a, signal_in, axis=0)


def master_bus(stereo: np.ndarray, reverb_wet: float = 0.25,
               reverb_length: float = 2.0, sr: int = SR) -> np.ndarray:
    """Standard mix-down master. HPF → reverb → gentle HF rolloff. Nothing
    else. The caller normalizes to a target peak afterwards — no saturation,
    no compression, no limiter. Distortion on playback comes from harmonic
    stages (saturation, compression pumping), not from normal mix levels,
    so remove them.
    """
    out = highpass(stereo, 40)
    out = apply_reverb(out, wet=reverb_wet, length_s=reverb_length,
                       decay_rate=3.8, sr=sr)
    out = lowpass(out, 8000, order=2)
    return out
