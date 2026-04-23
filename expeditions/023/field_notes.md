# Expedition 023

### 1. System name
Mantra of Two Breaths

### 2. Pitch organization
Stretched tuning, non-octave. Pseudo-octave of 2.12 (≈12% wider than 2:1) divided into six logarithmically-equal steps. Two pseudo-octaves used. Reference 70 Hz (very low).

### 3. Rhythmic organization
Additive 4+4 at 400 ms unit (cycle 3.2 s, slow breath-paced). Rhythmic ornament only — dynamic shape is the only dimension of variation.

### 4. Formal structure
Static contemplation. Seven identical exchanges repeat across the piece. Pitch and rhythm are frozen; what varies is *amplitude*, which follows a single breath-arc (soft → louder → loudest at exchange 4 → softer → softest). The piece is one long inhale and exhale.

### 5. Texture and voicing
Call-response — the same call-answer pair repeats, with each call/answer sung by two voices in heterophonic doubling. Call: two close-whispers (low register). Answer: two bowed crotales (higher register). Pot strikes at the end of each call and each answer.

### 6. Ornament and inflection
Rhythmic-only — amplitude arc across the seven repetitions is the piece's only variation.

### 7. Performance context
Contemplative-ritual. The listener sits with the piece. The silences between exchanges are equal in weight to the sound.

### 8. Relationship to neighboring systems
Shares with Aboriginal didgeridoo the drone-continuous low register and breath-based phrasing. Shares with Inuit katajjaq the antiphonal call-response structure and the intimacy of the voice. Shares with Gyütö tantric throat chant the low-register ritual meditation. Unique: *seven-times-repeated mantra in stretched non-octave tuning where the only variable is the breath-arc of amplitude*.

### 9. Audio specification

```json
{
  "duration_seconds": 81.0,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 70,
    "pitches": [
      1.0,
      1.1334,
      1.2846,
      1.456,
      1.6503,
      1.8705,
      2.12,
      2.4028,
      2.7234,
      3.0867,
      3.4986,
      3.9655,
      4.4944
    ],
    "octave_repeats": false
  },
  "rhythm_system": {
    "type": "additive",
    "groupings": [
      4,
      4
    ],
    "base_unit_ms": 400
  },
  "voices": [
    {
      "name": "drone",
      "timbre": "bass_drone",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "sustained_drone",
      "amplitude": 0.55,
      "spatial_position": [
        0.0,
        -0.4
      ]
    },
    {
      "name": "whisper_low",
      "timbre": "close_whisper",
      "pitch_indices": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
      ],
      "rhythm_role": "breath_phrase",
      "amplitude": 0.6,
      "spatial_position": [
        -0.3,
        0.3
      ]
    },
    {
      "name": "whisper_mid",
      "timbre": "close_whisper",
      "pitch_indices": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
      ],
      "rhythm_role": "breath_phrase",
      "amplitude": 0.5,
      "spatial_position": [
        0.3,
        0.3
      ]
    },
    {
      "name": "crotales_hi",
      "timbre": "bowed_crotales",
      "pitch_indices": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
      ],
      "rhythm_role": "breath_phrase",
      "amplitude": 0.55,
      "spatial_position": [
        0.55,
        0.1
      ]
    },
    {
      "name": "crotales_mid",
      "timbre": "bowed_crotales",
      "pitch_indices": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
      ],
      "rhythm_role": "breath_phrase",
      "amplitude": 0.45,
      "spatial_position": [
        -0.55,
        0.1
      ]
    },
    {
      "name": "pot",
      "timbre": "clay_pot",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "ritual_punctuation",
      "amplitude": 0.55,
      "spatial_position": [
        0.0,
        0.15
      ]
    }
  ],
  "form": {
    "arc_type": "static",
    "sections": [
      {
        "name": "mantra",
        "start_seconds": 0,
        "duration_seconds": 81.0,
        "character": "seven identical exchanges with breath-arc dynamics",
        "chord_tones": [
          0,
          2,
          3,
          4
        ]
      }
    ]
  },
  "ornamentation": {
    "density": 0.56,
    "rule": "Rhythmic-only: amplitude varies across the seven exchanges in a single breath arc (soft\u2192loud\u2192soft). Pitch and rhythm are identical."
  },
  "auto_pedal": false,
  "mix": {
    "reverb_wet": 0.55,
    "reverb_length": 3.2,
    "reverb_decay": 2.0,
    "hf_shelf_gain_db": -2.5,
    "hf_shelf_freq": 3500,
    "lpf_hz": 6500,
    "hpf_hz": 55
  },
  "events": [
    {
      "t": 2.0,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.08,
      "amplitude": 0.55
    },
    {
      "t": 2.08,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.056,
      "amplitude": 0.385
    },
    {
      "t": 3.2,
      "voice": "whisper_low",
      "pitch_index": 2,
      "duration_seconds": 0.72,
      "amplitude": 0.55
    },
    {
      "t": 3.28,
      "voice": "whisper_mid",
      "pitch_index": 2,
      "duration_seconds": 0.704,
      "amplitude": 0.385
    },
    {
      "t": 4.0,
      "voice": "whisper_low",
      "pitch_index": 1,
      "duration_seconds": 0.72,
      "amplitude": 0.55
    },
    {
      "t": 4.08,
      "voice": "whisper_mid",
      "pitch_index": 1,
      "duration_seconds": 0.704,
      "amplitude": 0.385
    },
    {
      "t": 4.8,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.44,
      "amplitude": 0.55
    },
    {
      "t": 4.88,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.408,
      "amplitude": 0.385
    },
    {
      "t": 6.28,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 7.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.116,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 7.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.092,
      "amplitude": 0.41250000000000003
    },
    {
      "t": 8.4,
      "voice": "crotales_hi",
      "pitch_index": 4,
      "duration_seconds": 0.744,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 8.52,
      "voice": "crotales_mid",
      "pitch_index": 4,
      "duration_seconds": 0.728,
      "amplitude": 0.41250000000000003
    },
    {
      "t": 9.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.86,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 9.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.82,
      "amplitude": 0.41250000000000003
    },
    {
      "t": 11.08,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 13.0,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.08,
      "amplitude": 0.6
    },
    {
      "t": 13.08,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.056,
      "amplitude": 0.42
    },
    {
      "t": 14.2,
      "voice": "whisper_low",
      "pitch_index": 2,
      "duration_seconds": 0.72,
      "amplitude": 0.6
    },
    {
      "t": 14.28,
      "voice": "whisper_mid",
      "pitch_index": 2,
      "duration_seconds": 0.704,
      "amplitude": 0.42
    },
    {
      "t": 15.0,
      "voice": "whisper_low",
      "pitch_index": 1,
      "duration_seconds": 0.72,
      "amplitude": 0.6
    },
    {
      "t": 15.08,
      "voice": "whisper_mid",
      "pitch_index": 1,
      "duration_seconds": 0.704,
      "amplitude": 0.42
    },
    {
      "t": 15.8,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.44,
      "amplitude": 0.6
    },
    {
      "t": 15.88,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.408,
      "amplitude": 0.42
    },
    {
      "t": 17.28,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.54
    },
    {
      "t": 18.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.116,
      "amplitude": 0.54
    },
    {
      "t": 18.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.092,
      "amplitude": 0.44999999999999996
    },
    {
      "t": 19.4,
      "voice": "crotales_hi",
      "pitch_index": 4,
      "duration_seconds": 0.744,
      "amplitude": 0.54
    },
    {
      "t": 19.52,
      "voice": "crotales_mid",
      "pitch_index": 4,
      "duration_seconds": 0.728,
      "amplitude": 0.44999999999999996
    },
    {
      "t": 20.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.86,
      "amplitude": 0.54
    },
    {
      "t": 20.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.82,
      "amplitude": 0.44999999999999996
    },
    {
      "t": 22.08,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.54
    },
    {
      "t": 24.0,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.08,
      "amplitude": 0.65
    },
    {
      "t": 24.08,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.056,
      "amplitude": 0.45499999999999996
    },
    {
      "t": 25.2,
      "voice": "whisper_low",
      "pitch_index": 2,
      "duration_seconds": 0.72,
      "amplitude": 0.65
    },
    {
      "t": 25.28,
      "voice": "whisper_mid",
      "pitch_index": 2,
      "duration_seconds": 0.704,
      "amplitude": 0.45499999999999996
    },
    {
      "t": 26.0,
      "voice": "whisper_low",
      "pitch_index": 1,
      "duration_seconds": 0.72,
      "amplitude": 0.65
    },
    {
      "t": 26.08,
      "voice": "whisper_mid",
      "pitch_index": 1,
      "duration_seconds": 0.704,
      "amplitude": 0.45499999999999996
    },
    {
      "t": 26.8,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.44,
      "amplitude": 0.65
    },
    {
      "t": 26.88,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.408,
      "amplitude": 0.45499999999999996
    },
    {
      "t": 28.28,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 29.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.116,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 29.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.092,
      "amplitude": 0.48750000000000004
    },
    {
      "t": 30.4,
      "voice": "crotales_hi",
      "pitch_index": 4,
      "duration_seconds": 0.744,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 30.52,
      "voice": "crotales_mid",
      "pitch_index": 4,
      "duration_seconds": 0.728,
      "amplitude": 0.48750000000000004
    },
    {
      "t": 31.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.86,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 31.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.82,
      "amplitude": 0.48750000000000004
    },
    {
      "t": 33.08,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 35.0,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.08,
      "amplitude": 0.7
    },
    {
      "t": 35.08,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.056,
      "amplitude": 0.48999999999999994
    },
    {
      "t": 36.2,
      "voice": "whisper_low",
      "pitch_index": 2,
      "duration_seconds": 0.72,
      "amplitude": 0.7
    },
    {
      "t": 36.28,
      "voice": "whisper_mid",
      "pitch_index": 2,
      "duration_seconds": 0.704,
      "amplitude": 0.48999999999999994
    },
    {
      "t": 37.0,
      "voice": "whisper_low",
      "pitch_index": 1,
      "duration_seconds": 0.72,
      "amplitude": 0.7
    },
    {
      "t": 37.08,
      "voice": "whisper_mid",
      "pitch_index": 1,
      "duration_seconds": 0.704,
      "amplitude": 0.48999999999999994
    },
    {
      "t": 37.8,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.44,
      "amplitude": 0.7
    },
    {
      "t": 37.88,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.408,
      "amplitude": 0.48999999999999994
    },
    {
      "t": 39.28,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.63
    },
    {
      "t": 40.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.116,
      "amplitude": 0.63
    },
    {
      "t": 40.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.092,
      "amplitude": 0.5249999999999999
    },
    {
      "t": 41.4,
      "voice": "crotales_hi",
      "pitch_index": 4,
      "duration_seconds": 0.744,
      "amplitude": 0.63
    },
    {
      "t": 41.52,
      "voice": "crotales_mid",
      "pitch_index": 4,
      "duration_seconds": 0.728,
      "amplitude": 0.5249999999999999
    },
    {
      "t": 42.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.86,
      "amplitude": 0.63
    },
    {
      "t": 42.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.82,
      "amplitude": 0.5249999999999999
    },
    {
      "t": 44.08,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.63
    },
    {
      "t": 46.0,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.08,
      "amplitude": 0.65
    },
    {
      "t": 46.08,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.056,
      "amplitude": 0.45499999999999996
    },
    {
      "t": 47.2,
      "voice": "whisper_low",
      "pitch_index": 2,
      "duration_seconds": 0.72,
      "amplitude": 0.65
    },
    {
      "t": 47.28,
      "voice": "whisper_mid",
      "pitch_index": 2,
      "duration_seconds": 0.704,
      "amplitude": 0.45499999999999996
    },
    {
      "t": 48.0,
      "voice": "whisper_low",
      "pitch_index": 1,
      "duration_seconds": 0.72,
      "amplitude": 0.65
    },
    {
      "t": 48.08,
      "voice": "whisper_mid",
      "pitch_index": 1,
      "duration_seconds": 0.704,
      "amplitude": 0.45499999999999996
    },
    {
      "t": 48.8,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.44,
      "amplitude": 0.65
    },
    {
      "t": 48.88,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.408,
      "amplitude": 0.45499999999999996
    },
    {
      "t": 50.28,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 51.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.116,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 51.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.092,
      "amplitude": 0.48750000000000004
    },
    {
      "t": 52.4,
      "voice": "crotales_hi",
      "pitch_index": 4,
      "duration_seconds": 0.744,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 52.52,
      "voice": "crotales_mid",
      "pitch_index": 4,
      "duration_seconds": 0.728,
      "amplitude": 0.48750000000000004
    },
    {
      "t": 53.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.86,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 53.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.82,
      "amplitude": 0.48750000000000004
    },
    {
      "t": 55.08,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.5850000000000001
    },
    {
      "t": 57.0,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.08,
      "amplitude": 0.55
    },
    {
      "t": 57.08,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.056,
      "amplitude": 0.385
    },
    {
      "t": 58.2,
      "voice": "whisper_low",
      "pitch_index": 2,
      "duration_seconds": 0.72,
      "amplitude": 0.55
    },
    {
      "t": 58.28,
      "voice": "whisper_mid",
      "pitch_index": 2,
      "duration_seconds": 0.704,
      "amplitude": 0.385
    },
    {
      "t": 59.0,
      "voice": "whisper_low",
      "pitch_index": 1,
      "duration_seconds": 0.72,
      "amplitude": 0.55
    },
    {
      "t": 59.08,
      "voice": "whisper_mid",
      "pitch_index": 1,
      "duration_seconds": 0.704,
      "amplitude": 0.385
    },
    {
      "t": 59.8,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.44,
      "amplitude": 0.55
    },
    {
      "t": 59.88,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.408,
      "amplitude": 0.385
    },
    {
      "t": 61.28,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 62.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.116,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 62.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.092,
      "amplitude": 0.41250000000000003
    },
    {
      "t": 63.4,
      "voice": "crotales_hi",
      "pitch_index": 4,
      "duration_seconds": 0.744,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 63.52,
      "voice": "crotales_mid",
      "pitch_index": 4,
      "duration_seconds": 0.728,
      "amplitude": 0.41250000000000003
    },
    {
      "t": 64.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.86,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 64.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.82,
      "amplitude": 0.41250000000000003
    },
    {
      "t": 66.08,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.49500000000000005
    },
    {
      "t": 68.0,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.08,
      "amplitude": 0.48
    },
    {
      "t": 68.08,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.056,
      "amplitude": 0.33599999999999997
    },
    {
      "t": 69.2,
      "voice": "whisper_low",
      "pitch_index": 2,
      "duration_seconds": 0.72,
      "amplitude": 0.48
    },
    {
      "t": 69.28,
      "voice": "whisper_mid",
      "pitch_index": 2,
      "duration_seconds": 0.704,
      "amplitude": 0.33599999999999997
    },
    {
      "t": 70.0,
      "voice": "whisper_low",
      "pitch_index": 1,
      "duration_seconds": 0.72,
      "amplitude": 0.48
    },
    {
      "t": 70.08,
      "voice": "whisper_mid",
      "pitch_index": 1,
      "duration_seconds": 0.704,
      "amplitude": 0.33599999999999997
    },
    {
      "t": 70.8,
      "voice": "whisper_low",
      "pitch_index": 0,
      "duration_seconds": 1.44,
      "amplitude": 0.48
    },
    {
      "t": 70.88,
      "voice": "whisper_mid",
      "pitch_index": 0,
      "duration_seconds": 1.408,
      "amplitude": 0.33599999999999997
    },
    {
      "t": 72.28,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.432
    },
    {
      "t": 73.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.116,
      "amplitude": 0.432
    },
    {
      "t": 73.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.092,
      "amplitude": 0.36
    },
    {
      "t": 74.4,
      "voice": "crotales_hi",
      "pitch_index": 4,
      "duration_seconds": 0.744,
      "amplitude": 0.432
    },
    {
      "t": 74.52,
      "voice": "crotales_mid",
      "pitch_index": 4,
      "duration_seconds": 0.728,
      "amplitude": 0.36
    },
    {
      "t": 75.2,
      "voice": "crotales_hi",
      "pitch_index": 3,
      "duration_seconds": 1.86,
      "amplitude": 0.432
    },
    {
      "t": 75.32,
      "voice": "crotales_mid",
      "pitch_index": 3,
      "duration_seconds": 1.82,
      "amplitude": 0.36
    },
    {
      "t": 77.08,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.432
    }
  ]
}
```

### 10. Field note
The same phrase seven times with seven different meanings.
