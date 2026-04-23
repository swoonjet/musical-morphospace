"""Compositional archetypes — small library of real compositional techniques
that each produce distinctive structure, not just chord-tone-walk.

Each archetype takes a motif (pitches + durations) and optionally parameters,
and returns a list of event dicts ready for the audio_spec.

All durations are in *units* (multiples of the audio_spec base_unit_ms).
Each archetype is deliberately parameterised small — the grammar of each
expedition picks the archetype and fills in.
"""
from __future__ import annotations
import random
from typing import List, Tuple, Dict, Callable, Optional

# Type alias: motif = list of (pitch_index, duration_units)
Motif = List[Tuple[int, int]]


# ============================================================
# Basic helpers
# ============================================================

def render_motif(start_t: float, motif: Motif, voice: str, unit_s: float,
                  amp: float = 0.7, gap: float = 0.95,
                  pitch_offset: int = 0, max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    evs = []
    t = start_t
    for p, u in motif:
        pp = p + pitch_offset
        if max_pitch is not None: pp = min(max_pitch, max(0, pp))
        dur = u * unit_s * gap
        evs.append({"t": round(t, 3), "voice": voice, "pitch_index": pp,
                    "duration_seconds": round(dur, 3), "amplitude": amp})
        t += u * unit_s
    return evs, t


def invert_motif(motif: Motif, axis: int) -> Motif:
    """Mirror pitches around `axis`."""
    return [(2 * axis - p, u) for p, u in motif]


def retrograde(motif: Motif) -> Motif:
    return list(reversed(motif))


def augment(motif: Motif, factor: float = 2.0) -> Motif:
    return [(p, max(1, int(round(u * factor)))) for p, u in motif]


def diminute(motif: Motif, factor: float = 0.5) -> Motif:
    return [(p, max(1, int(round(u * factor)))) for p, u in motif]


def transpose(motif: Motif, semitones: int) -> Motif:
    """Here 'semitones' is actually 'scale degrees' (just an integer offset)."""
    return [(p + semitones, u) for p, u in motif]


# ============================================================
# Archetype 1: PASSACAGLIA — repeating bass + variations above
# ============================================================

def passacaglia(*, start_t: float, bass_motif: Motif, n_statements: int,
                 variation_layers: List[List[dict]], bass_voice: str,
                 unit_s: float, bass_amp: float = 0.55,
                 max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    """n_statements of bass_motif back to back; at each statement, the next
    variation layer (a list of pre-made event dicts, time-relative to the
    statement's start) is overlaid. Returns (events, end_time)."""
    events = []
    t = start_t
    bass_len = sum(u for _, u in bass_motif) * unit_s
    for i in range(n_statements):
        be, _ = render_motif(t, bass_motif, bass_voice, unit_s,
                              amp=bass_amp, max_pitch=max_pitch)
        events += be
        # Overlay variation layer i, time-shifted to t
        if i < len(variation_layers):
            for ev in variation_layers[i]:
                events.append({**ev, "t": round(ev["t"] + t, 3)})
        t += bass_len
    return events, t


# ============================================================
# Archetype 2: STROPHIC — verse/chorus/verse with same melody
# ============================================================

def strophic(*, start_t: float, verse_motif: Motif, chorus_motif: Motif,
              n_verses: int, melody_voice: str, unit_s: float,
              verse_amp: float = 0.7, chorus_amp: float = 0.75,
              chorus_transposition: int = 0,
              bridge_motif: Optional[Motif] = None,
              bridge_before_last: bool = True,
              max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    """Verse → chorus → verse → chorus → [bridge] → verse → chorus ..."""
    events = []
    t = start_t
    for i in range(n_verses):
        e, t = render_motif(t, verse_motif, melody_voice, unit_s,
                             amp=verse_amp, max_pitch=max_pitch)
        events += e
        if bridge_before_last and bridge_motif and i == n_verses - 2:
            e, t = render_motif(t, bridge_motif, melody_voice, unit_s,
                                 amp=verse_amp * 0.9, max_pitch=max_pitch)
            events += e
        e, t = render_motif(t, chorus_motif, melody_voice, unit_s,
                             amp=chorus_amp, pitch_offset=chorus_transposition,
                             max_pitch=max_pitch)
        events += e
    return events, t


# ============================================================
# Archetype 3: RAGA ALAP — gradual pitch introduction over drone
# ============================================================

def raga_alap(*, start_t: float, scale_order: List[int], duration: float,
                voice: str, unit_s: float, rng: random.Random,
                home: int = 0, max_pitch: Optional[int] = None,
                amp: float = 0.7) -> Tuple[List[dict], float]:
    """Introduce scale pitches one at a time in the order given. Each new
    pitch gets 3-5 phrases exploring it before the next is added. All phrases
    return to home. Generates unscripted but scale-bounded melodic exploration.
    """
    events = []
    t = start_t
    end_t = start_t + duration
    introduced = [home]
    for target in scale_order:
        if t >= end_t: break
        if target not in introduced:
            introduced.append(target)
        # 3-5 phrases with current pitch set
        n_phrases = rng.choice([3, 4, 4, 5])
        for _ in range(n_phrases):
            if t >= end_t: break
            # phrase: touch 3-6 notes from introduced, end on home
            notes = rng.choice([3, 4, 5, 6])
            for j in range(notes):
                pi = rng.choice(introduced) if j < notes - 1 else home
                if max_pitch is not None: pi = min(max_pitch, pi)
                dur_u = rng.choice([1, 2, 2, 3, 4])
                # slight rubato: duration_seconds jittered
                dur_s = dur_u * unit_s * rng.uniform(0.85, 1.15)
                events.append({"t": round(t, 3), "voice": voice, "pitch_index": pi,
                                "duration_seconds": round(dur_s, 3),
                                "amplitude": round(amp * rng.uniform(0.85, 1.05), 3)})
                t += dur_s
            # short breath between phrases
            t += unit_s * rng.uniform(0.5, 1.3)
    return events, t


# ============================================================
# Archetype 4: ISORHYTHMIC MOTET — talea (rhythm) × color (pitch), mismatched
# lengths so the alignment changes each cycle
# ============================================================

def isorhythm(*, start_t: float, talea_durs: List[int], color_pitches: List[int],
                n_cycles: int, voice: str, unit_s: float, amp: float = 0.65,
                max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    """talea_durs (rhythm pattern, in units) and color_pitches (pitch sequence)
    have different lengths — their alignment changes each cycle (medieval
    isorhythmic technique). Returns n_cycles of the longer sequence."""
    talea_len = len(talea_durs)
    color_len = len(color_pitches)
    # Number of events to emit: n_cycles × max
    total_events = max(talea_len, color_len) * n_cycles
    events = []
    t = start_t
    for i in range(total_events):
        dur_u = talea_durs[i % talea_len]
        pi = color_pitches[i % color_len]
        if max_pitch is not None: pi = min(max_pitch, max(0, pi))
        dur_s = dur_u * unit_s * 0.95
        events.append({"t": round(t, 3), "voice": voice, "pitch_index": pi,
                        "duration_seconds": round(dur_s, 3), "amplitude": amp})
        t += dur_u * unit_s
    return events, t


# ============================================================
# Archetype 5: MINIMALIST PHASING — two voices share a pattern but slip apart
# ============================================================

def phasing(*, start_t: float, pattern: Motif, n_bars: int,
              voice_a: str, voice_b: str, unit_s: float,
              slip_per_bar: float = 0.06, amp: float = 0.55,
              max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    """voice_a plays pattern at fixed rate. voice_b plays same pattern but
    slightly faster each bar, so they gradually slip out of phase and back in.
    slip_per_bar is the tempo ratio deviation per bar."""
    events = []
    pat_len_a = sum(u for _, u in pattern) * unit_s
    t_a = start_t
    t_b = start_t
    for bar in range(n_bars):
        # voice A: normal rate
        ea, t_a = render_motif(t_a, pattern, voice_a, unit_s, amp=amp,
                                max_pitch=max_pitch)
        events += ea
        # voice B: rate scaled
        rate_b = 1.0 + slip_per_bar * bar
        eb, t_b = render_motif(t_b, pattern, voice_b, unit_s / rate_b,
                                amp=amp, max_pitch=max_pitch)
        events += eb
    return events, max(t_a, t_b)


# ============================================================
# Archetype 6: HETEROPHONIC VARIATION — several voices play same line, varied
# ============================================================

def heterophonic(*, start_t: float, motif: Motif, voices: List[str],
                  unit_s: float, rng: random.Random, amp: float = 0.55,
                  time_spread: float = 0.12, pitch_sub_prob: float = 0.2,
                  max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    """Each voice plays the same motif but with small timing offsets and
    occasional pitch substitutions (±1 step). Returns the superposition."""
    events = []
    end_t = start_t
    for vi, vn in enumerate(voices):
        t = start_t + rng.uniform(0, time_spread)
        for p, u in motif:
            pp = p
            if rng.random() < pitch_sub_prob:
                pp = p + rng.choice([-1, 1])
            if max_pitch is not None: pp = min(max_pitch, max(0, pp))
            dur = u * unit_s * rng.uniform(0.9, 1.05)
            events.append({"t": round(t, 3), "voice": vn, "pitch_index": pp,
                            "duration_seconds": round(dur, 3),
                            "amplitude": round(amp * rng.uniform(0.9, 1.08), 3)})
            t += u * unit_s * rng.uniform(0.95, 1.05)
        end_t = max(end_t, t)
    return events, end_t


# ============================================================
# Archetype 7: MELISMATIC CHANT — long unmetered lines, few pitches, heavy
# ornament on specific syllables
# ============================================================

def melismatic_chant(*, start_t: float, syllables: List[Tuple[int, int]],
                       voice: str, unit_s: float, rng: random.Random,
                       melisma_probability: float = 0.5,
                       melisma_pitches_offsets: Tuple[int, ...] = (-1, 1, 2, -2),
                       amp: float = 0.7,
                       max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    """syllables: list of (home_pitch_idx, syllable_duration_units). Each
    syllable is either sung plain on its home pitch, or decorated as a melisma
    — rapid notes around home returning to home."""
    events = []
    t = start_t
    for home, dur_u in syllables:
        if rng.random() < melisma_probability and dur_u >= 2:
            # Melisma: 3-5 quick notes within dur_u
            n_notes = rng.choice([3, 4, 5])
            sub_u = dur_u / n_notes
            for i in range(n_notes):
                if i == 0 or i == n_notes - 1:
                    pi = home
                else:
                    pi = home + rng.choice(melisma_pitches_offsets)
                if max_pitch is not None: pi = min(max_pitch, max(0, pi))
                dur_s = sub_u * unit_s * 0.9
                events.append({"t": round(t, 3), "voice": voice, "pitch_index": pi,
                                "duration_seconds": round(dur_s, 3),
                                "amplitude": amp})
                t += sub_u * unit_s
        else:
            # Plain syllable
            if max_pitch is not None: pi = min(max_pitch, max(0, home))
            else: pi = home
            dur_s = dur_u * unit_s * 0.92
            events.append({"t": round(t, 3), "voice": voice, "pitch_index": pi,
                            "duration_seconds": round(dur_s, 3),
                            "amplitude": amp})
            t += dur_u * unit_s
    return events, t


# ============================================================
# Archetype 8: ANTIPHONAL DIALOGUE — call and answer that share material
# ============================================================

def antiphonal_dialogue(*, start_t: float, exchanges: List[Tuple[Motif, Motif]],
                          caller_voice: str, answerer_voice: str,
                          unit_s: float, gap_seconds: float = 0.8,
                          amp: float = 0.7,
                          max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    """exchanges: list of (call_motif, answer_motif) pairs. Call is stated by
    caller, gap, answerer responds. Each pair is one exchange."""
    events = []
    t = start_t
    for call, answer in exchanges:
        e, t = render_motif(t, call, caller_voice, unit_s, amp=amp,
                             max_pitch=max_pitch)
        events += e
        t += gap_seconds
        e, t = render_motif(t, answer, answerer_voice, unit_s, amp=amp,
                             max_pitch=max_pitch)
        events += e
        t += gap_seconds
    return events, t


# ============================================================
# Archetype 9: GROUND BASS — looping bass, free improvisation above
# (different from passacaglia — here the "above" is scheduler-driven with
# chord_tones attraction, not pre-scripted variations)
# ============================================================

def ground_bass_loop(*, start_t: float, bass_motif: Motif, n_statements: int,
                       bass_voice: str, unit_s: float, bass_amp: float = 0.55,
                       max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    """Just the bass loop, n times. The caller is responsible for the upper
    voices (typically left to the scheduler with chord_tones)."""
    events = []
    t = start_t
    for _ in range(n_statements):
        e, t = render_motif(t, bass_motif, bass_voice, unit_s,
                             amp=bass_amp, max_pitch=max_pitch)
        events += e
    return events, t


# ============================================================
# Archetype 10: CANONIC IMITATION — same motif at staggered entries
# ============================================================

def canon(*, start_t: float, motif: Motif, voices: List[str],
            entry_offsets_units: List[int], unit_s: float, amp: float = 0.65,
            pitch_offsets: Optional[List[int]] = None,
            max_pitch: Optional[int] = None) -> Tuple[List[dict], float]:
    """Each voice enters with the motif, staggered by entry_offsets_units[i].
    Optional pitch_offsets for canonic transposition."""
    events = []
    if pitch_offsets is None:
        pitch_offsets = [0] * len(voices)
    end_t = start_t
    for vn, eo, po in zip(voices, entry_offsets_units, pitch_offsets):
        t_entry = start_t + eo * unit_s
        e, t = render_motif(t_entry, motif, vn, unit_s, amp=amp,
                             pitch_offset=po, max_pitch=max_pitch)
        events += e
        end_t = max(end_t, t)
    return events, end_t
