# Expedition 022

### 1. System name
Gamelan of the Non-Closing Spiral

### 2. Pitch organization
Irrational-ratio spiral: each step is near-fifth (1.5 ± 0.04) stacked. 12 pitches in the playable register, reduced from a 12-step spiral that does not close. Microtonal inflection is obligatory ±15 cents on every note.

### 3. Rhythmic organization
Additive 2+3+2 at 160 ms unit (cycle 1.12 s — the *gongan*). Above this metric substrate, the piece uses **isorhythmic technique**: each melodic voice is built from a talea (rhythm pattern, 7 durations summing 23 units) and a color (pitch sequence, 5 pitches). Talea and color have mismatched lengths — 23 vs 5, 18 vs 4 — so the alignment of rhythm to pitch shifts each cycle, producing a pattern that sounds familiar but is never identical from cycle to cycle.

### 4. Formal structure
Modular combinatorial. Two sections, each a self-contained isorhythmic block:
- **Group I** — three voices (marimba, hang drum, thumb piano), all isorhythmic, in left hemisphere
- **Group II** — two voices (marimba, hang drum) mirror the first group on the right with transposed color

A closing gong (clay pot on home) ends the piece.

### 5. Texture and voicing
Layered ostinato, antiphonal choirs. Voice independence is near-maximal — each voice operates its own talea/color cycle. The texture is dense but non-random; every event is determined by its voice's mathematical pattern.

### 6. Ornament and inflection
Microtonal inflection core (mandatory). No melodic ornament. The *talea-color mismatch* is the piece's ornamental logic — each sounding event is the meeting point of an independent rhythmic and pitch cycle, and its identity comes from that coincidence.

### 7. Performance context
Court ceremony. The two groups face each other; the clay-pot player sits between. The gong marks gongan boundaries.

### 8. Relationship to neighboring systems
Shares with Javanese gamelan the gong-structured cyclic meter and the layered percussion ostinato. Shares with Gyütö tantric throat chant the drone-continuous texture. Shares with Balinese gamelan gong kebyar the antiphonal interlocking. Shares with medieval isorhythmic motet the talea/color technique. Unique: *isorhythmic gamelan in non-closing irrational spiral tuning with obligatory microtonal inflection*.

### 9. Audio specification

```json
{
  "duration_seconds": 62.0,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 165,
    "pitches": [
      1.0,
      1.4928,
      2.2343,
      2.5515,
      2.8497,
      2.8833,
      3.2885,
      3.3159,
      3.7466,
      3.8157,
      4.3878,
      4.9211
    ],
    "octave_repeats": false,
    "inflection_rules": [
      {
        "pitch_index": 0,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 1,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 2,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 3,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 4,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 5,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 6,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 7,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 8,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 9,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 10,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      },
      {
        "pitch_index": 11,
        "inflection_cents_range": [
          -15,
          15
        ],
        "direction": "both"
      }
    ]
  },
  "rhythm_system": {
    "type": "additive",
    "groupings": [
      2,
      3,
      2
    ],
    "base_unit_ms": 160
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
      "name": "marimba",
      "timbre": "wood_marimba",
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
        11
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.6,
      "spatial_position": [
        -0.55,
        0.2
      ]
    },
    {
      "name": "hang",
      "timbre": "hang_drum",
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
        11
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.58,
      "spatial_position": [
        -0.3,
        0.15
      ]
    },
    {
      "name": "thumb",
      "timbre": "thumb_piano",
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
        11
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.52,
      "spatial_position": [
        0.0,
        0.25
      ]
    },
    {
      "name": "marimba2",
      "timbre": "wood_marimba",
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
        11
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.58,
      "spatial_position": [
        0.55,
        0.2
      ]
    },
    {
      "name": "hang2",
      "timbre": "hang_drum",
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
        11
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.56,
      "spatial_position": [
        0.3,
        0.15
      ]
    },
    {
      "name": "pot",
      "timbre": "clay_pot",
      "pitch_indices": [
        0,
        1
      ],
      "rhythm_role": "ritual_punctuation",
      "amplitude": 0.6,
      "spatial_position": [
        0.0,
        -0.15
      ]
    }
  ],
  "form": {
    "arc_type": "modular",
    "sections": [
      {
        "name": "group_I_alone",
        "start_seconds": 0,
        "duration_seconds": 31,
        "character": "three isorhythmic voices in left group",
        "chord_tones": [
          0,
          2,
          4,
          5,
          7
        ]
      },
      {
        "name": "group_II_enters",
        "start_seconds": 32,
        "duration_seconds": 28,
        "character": "right group answers antiphonally, also isorhythmic",
        "chord_tones": [
          2,
          3,
          4,
          5,
          6,
          7
        ]
      },
      {
        "name": "final_gong",
        "start_seconds": 60,
        "duration_seconds": 8,
        "character": "final gong on home",
        "chord_tones": [
          0
        ]
      }
    ]
  },
  "ornamentation": {
    "density": 0.5,
    "rule": "Microtonal inflection core on every note; otherwise no ornament. The talea-color mismatch *is* the piece's ornamental logic."
  },
  "auto_pedal": false,
  "mix": {
    "reverb_wet": 0.22,
    "reverb_length": 1.8,
    "reverb_decay": 4.0,
    "hf_shelf_gain_db": -0.8,
    "hf_shelf_freq": 4000,
    "lpf_hz": 7200
  },
  "events": [
    {
      "t": 2.0,
      "voice": "marimba",
      "pitch_index": 0,
      "duration_seconds": 0.304,
      "amplitude": 0.6
    },
    {
      "t": 2.32,
      "voice": "marimba",
      "pitch_index": 2,
      "duration_seconds": 0.456,
      "amplitude": 0.6
    },
    {
      "t": 2.8,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.304,
      "amplitude": 0.6
    },
    {
      "t": 3.12,
      "voice": "marimba",
      "pitch_index": 5,
      "duration_seconds": 0.608,
      "amplitude": 0.6
    },
    {
      "t": 3.76,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.6
    },
    {
      "t": 4.24,
      "voice": "marimba",
      "pitch_index": 0,
      "duration_seconds": 0.912,
      "amplitude": 0.6
    },
    {
      "t": 5.2,
      "voice": "marimba",
      "pitch_index": 2,
      "duration_seconds": 0.456,
      "amplitude": 0.6
    },
    {
      "t": 5.68,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.304,
      "amplitude": 0.6
    },
    {
      "t": 6.0,
      "voice": "marimba",
      "pitch_index": 5,
      "duration_seconds": 0.456,
      "amplitude": 0.6
    },
    {
      "t": 6.48,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.304,
      "amplitude": 0.6
    },
    {
      "t": 6.8,
      "voice": "marimba",
      "pitch_index": 0,
      "duration_seconds": 0.608,
      "amplitude": 0.6
    },
    {
      "t": 7.44,
      "voice": "marimba",
      "pitch_index": 2,
      "duration_seconds": 0.456,
      "amplitude": 0.6
    },
    {
      "t": 7.92,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.912,
      "amplitude": 0.6
    },
    {
      "t": 8.88,
      "voice": "marimba",
      "pitch_index": 5,
      "duration_seconds": 0.456,
      "amplitude": 0.6
    },
    {
      "t": 9.36,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.304,
      "amplitude": 0.6
    },
    {
      "t": 9.68,
      "voice": "marimba",
      "pitch_index": 0,
      "duration_seconds": 0.456,
      "amplitude": 0.6
    },
    {
      "t": 10.16,
      "voice": "marimba",
      "pitch_index": 2,
      "duration_seconds": 0.304,
      "amplitude": 0.6
    },
    {
      "t": 10.48,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.608,
      "amplitude": 0.6
    },
    {
      "t": 11.12,
      "voice": "marimba",
      "pitch_index": 5,
      "duration_seconds": 0.456,
      "amplitude": 0.6
    },
    {
      "t": 11.6,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.912,
      "amplitude": 0.6
    },
    {
      "t": 12.56,
      "voice": "marimba",
      "pitch_index": 0,
      "duration_seconds": 0.456,
      "amplitude": 0.6
    },
    {
      "t": 2.0,
      "voice": "hang",
      "pitch_index": 3,
      "duration_seconds": 0.304,
      "amplitude": 0.55
    },
    {
      "t": 2.32,
      "voice": "hang",
      "pitch_index": 5,
      "duration_seconds": 0.456,
      "amplitude": 0.55
    },
    {
      "t": 2.8,
      "voice": "hang",
      "pitch_index": 6,
      "duration_seconds": 0.304,
      "amplitude": 0.55
    },
    {
      "t": 3.12,
      "voice": "hang",
      "pitch_index": 4,
      "duration_seconds": 0.608,
      "amplitude": 0.55
    },
    {
      "t": 3.76,
      "voice": "hang",
      "pitch_index": 2,
      "duration_seconds": 0.456,
      "amplitude": 0.55
    },
    {
      "t": 4.24,
      "voice": "hang",
      "pitch_index": 3,
      "duration_seconds": 0.912,
      "amplitude": 0.55
    },
    {
      "t": 5.2,
      "voice": "hang",
      "pitch_index": 5,
      "duration_seconds": 0.456,
      "amplitude": 0.55
    },
    {
      "t": 5.68,
      "voice": "hang",
      "pitch_index": 6,
      "duration_seconds": 0.304,
      "amplitude": 0.55
    },
    {
      "t": 6.0,
      "voice": "hang",
      "pitch_index": 4,
      "duration_seconds": 0.456,
      "amplitude": 0.55
    },
    {
      "t": 6.48,
      "voice": "hang",
      "pitch_index": 2,
      "duration_seconds": 0.304,
      "amplitude": 0.55
    },
    {
      "t": 6.8,
      "voice": "hang",
      "pitch_index": 3,
      "duration_seconds": 0.608,
      "amplitude": 0.55
    },
    {
      "t": 7.44,
      "voice": "hang",
      "pitch_index": 5,
      "duration_seconds": 0.456,
      "amplitude": 0.55
    },
    {
      "t": 7.92,
      "voice": "hang",
      "pitch_index": 6,
      "duration_seconds": 0.912,
      "amplitude": 0.55
    },
    {
      "t": 8.88,
      "voice": "hang",
      "pitch_index": 4,
      "duration_seconds": 0.456,
      "amplitude": 0.55
    },
    {
      "t": 9.36,
      "voice": "hang",
      "pitch_index": 2,
      "duration_seconds": 0.304,
      "amplitude": 0.55
    },
    {
      "t": 9.68,
      "voice": "hang",
      "pitch_index": 3,
      "duration_seconds": 0.456,
      "amplitude": 0.55
    },
    {
      "t": 10.16,
      "voice": "hang",
      "pitch_index": 5,
      "duration_seconds": 0.304,
      "amplitude": 0.55
    },
    {
      "t": 10.48,
      "voice": "hang",
      "pitch_index": 6,
      "duration_seconds": 0.608,
      "amplitude": 0.55
    },
    {
      "t": 11.12,
      "voice": "hang",
      "pitch_index": 4,
      "duration_seconds": 0.456,
      "amplitude": 0.55
    },
    {
      "t": 11.6,
      "voice": "hang",
      "pitch_index": 2,
      "duration_seconds": 0.912,
      "amplitude": 0.55
    },
    {
      "t": 12.56,
      "voice": "hang",
      "pitch_index": 3,
      "duration_seconds": 0.456,
      "amplitude": 0.55
    },
    {
      "t": 2.0,
      "voice": "thumb",
      "pitch_index": 0,
      "duration_seconds": 0.608,
      "amplitude": 0.5
    },
    {
      "t": 2.64,
      "voice": "thumb",
      "pitch_index": 4,
      "duration_seconds": 0.76,
      "amplitude": 0.5
    },
    {
      "t": 3.44,
      "voice": "thumb",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.5
    },
    {
      "t": 3.92,
      "voice": "thumb",
      "pitch_index": 3,
      "duration_seconds": 0.912,
      "amplitude": 0.5
    },
    {
      "t": 4.88,
      "voice": "thumb",
      "pitch_index": 0,
      "duration_seconds": 0.608,
      "amplitude": 0.5
    },
    {
      "t": 5.52,
      "voice": "thumb",
      "pitch_index": 4,
      "duration_seconds": 0.76,
      "amplitude": 0.5
    },
    {
      "t": 6.32,
      "voice": "thumb",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.5
    },
    {
      "t": 6.8,
      "voice": "thumb",
      "pitch_index": 3,
      "duration_seconds": 0.912,
      "amplitude": 0.5
    },
    {
      "t": 7.76,
      "voice": "thumb",
      "pitch_index": 0,
      "duration_seconds": 0.608,
      "amplitude": 0.5
    },
    {
      "t": 8.4,
      "voice": "thumb",
      "pitch_index": 4,
      "duration_seconds": 0.76,
      "amplitude": 0.5
    },
    {
      "t": 9.2,
      "voice": "thumb",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.5
    },
    {
      "t": 9.68,
      "voice": "thumb",
      "pitch_index": 3,
      "duration_seconds": 0.912,
      "amplitude": 0.5
    },
    {
      "t": 10.64,
      "voice": "thumb",
      "pitch_index": 0,
      "duration_seconds": 0.608,
      "amplitude": 0.5
    },
    {
      "t": 11.28,
      "voice": "thumb",
      "pitch_index": 4,
      "duration_seconds": 0.76,
      "amplitude": 0.5
    },
    {
      "t": 12.08,
      "voice": "thumb",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.5
    },
    {
      "t": 12.56,
      "voice": "thumb",
      "pitch_index": 3,
      "duration_seconds": 0.912,
      "amplitude": 0.5
    },
    {
      "t": 32.0,
      "voice": "marimba2",
      "pitch_index": 2,
      "duration_seconds": 0.304,
      "amplitude": 0.58
    },
    {
      "t": 32.32,
      "voice": "marimba2",
      "pitch_index": 4,
      "duration_seconds": 0.456,
      "amplitude": 0.58
    },
    {
      "t": 32.8,
      "voice": "marimba2",
      "pitch_index": 6,
      "duration_seconds": 0.304,
      "amplitude": 0.58
    },
    {
      "t": 33.12,
      "voice": "marimba2",
      "pitch_index": 7,
      "duration_seconds": 0.608,
      "amplitude": 0.58
    },
    {
      "t": 33.76,
      "voice": "marimba2",
      "pitch_index": 9,
      "duration_seconds": 0.456,
      "amplitude": 0.58
    },
    {
      "t": 34.24,
      "voice": "marimba2",
      "pitch_index": 2,
      "duration_seconds": 0.912,
      "amplitude": 0.58
    },
    {
      "t": 35.2,
      "voice": "marimba2",
      "pitch_index": 4,
      "duration_seconds": 0.456,
      "amplitude": 0.58
    },
    {
      "t": 35.68,
      "voice": "marimba2",
      "pitch_index": 6,
      "duration_seconds": 0.304,
      "amplitude": 0.58
    },
    {
      "t": 36.0,
      "voice": "marimba2",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.58
    },
    {
      "t": 36.48,
      "voice": "marimba2",
      "pitch_index": 9,
      "duration_seconds": 0.304,
      "amplitude": 0.58
    },
    {
      "t": 36.8,
      "voice": "marimba2",
      "pitch_index": 2,
      "duration_seconds": 0.608,
      "amplitude": 0.58
    },
    {
      "t": 37.44,
      "voice": "marimba2",
      "pitch_index": 4,
      "duration_seconds": 0.456,
      "amplitude": 0.58
    },
    {
      "t": 37.92,
      "voice": "marimba2",
      "pitch_index": 6,
      "duration_seconds": 0.912,
      "amplitude": 0.58
    },
    {
      "t": 38.88,
      "voice": "marimba2",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.58
    },
    {
      "t": 39.36,
      "voice": "marimba2",
      "pitch_index": 9,
      "duration_seconds": 0.304,
      "amplitude": 0.58
    },
    {
      "t": 39.68,
      "voice": "marimba2",
      "pitch_index": 2,
      "duration_seconds": 0.456,
      "amplitude": 0.58
    },
    {
      "t": 40.16,
      "voice": "marimba2",
      "pitch_index": 4,
      "duration_seconds": 0.304,
      "amplitude": 0.58
    },
    {
      "t": 40.48,
      "voice": "marimba2",
      "pitch_index": 6,
      "duration_seconds": 0.608,
      "amplitude": 0.58
    },
    {
      "t": 41.12,
      "voice": "marimba2",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.58
    },
    {
      "t": 41.6,
      "voice": "marimba2",
      "pitch_index": 9,
      "duration_seconds": 0.912,
      "amplitude": 0.58
    },
    {
      "t": 42.56,
      "voice": "marimba2",
      "pitch_index": 2,
      "duration_seconds": 0.456,
      "amplitude": 0.58
    },
    {
      "t": 32.0,
      "voice": "hang2",
      "pitch_index": 5,
      "duration_seconds": 0.304,
      "amplitude": 0.53
    },
    {
      "t": 32.32,
      "voice": "hang2",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.53
    },
    {
      "t": 32.8,
      "voice": "hang2",
      "pitch_index": 8,
      "duration_seconds": 0.304,
      "amplitude": 0.53
    },
    {
      "t": 33.12,
      "voice": "hang2",
      "pitch_index": 6,
      "duration_seconds": 0.608,
      "amplitude": 0.53
    },
    {
      "t": 33.76,
      "voice": "hang2",
      "pitch_index": 4,
      "duration_seconds": 0.456,
      "amplitude": 0.53
    },
    {
      "t": 34.24,
      "voice": "hang2",
      "pitch_index": 5,
      "duration_seconds": 0.912,
      "amplitude": 0.53
    },
    {
      "t": 35.2,
      "voice": "hang2",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.53
    },
    {
      "t": 35.68,
      "voice": "hang2",
      "pitch_index": 8,
      "duration_seconds": 0.304,
      "amplitude": 0.53
    },
    {
      "t": 36.0,
      "voice": "hang2",
      "pitch_index": 6,
      "duration_seconds": 0.456,
      "amplitude": 0.53
    },
    {
      "t": 36.48,
      "voice": "hang2",
      "pitch_index": 4,
      "duration_seconds": 0.304,
      "amplitude": 0.53
    },
    {
      "t": 36.8,
      "voice": "hang2",
      "pitch_index": 5,
      "duration_seconds": 0.608,
      "amplitude": 0.53
    },
    {
      "t": 37.44,
      "voice": "hang2",
      "pitch_index": 7,
      "duration_seconds": 0.456,
      "amplitude": 0.53
    },
    {
      "t": 37.92,
      "voice": "hang2",
      "pitch_index": 8,
      "duration_seconds": 0.912,
      "amplitude": 0.53
    },
    {
      "t": 38.88,
      "voice": "hang2",
      "pitch_index": 6,
      "duration_seconds": 0.456,
      "amplitude": 0.53
    },
    {
      "t": 39.36,
      "voice": "hang2",
      "pitch_index": 4,
      "duration_seconds": 0.304,
      "amplitude": 0.53
    },
    {
      "t": 39.68,
      "voice": "hang2",
      "pitch_index": 5,
      "duration_seconds": 0.456,
      "amplitude": 0.53
    },
    {
      "t": 40.16,
      "voice": "hang2",
      "pitch_index": 7,
      "duration_seconds": 0.304,
      "amplitude": 0.53
    },
    {
      "t": 40.48,
      "voice": "hang2",
      "pitch_index": 8,
      "duration_seconds": 0.608,
      "amplitude": 0.53
    },
    {
      "t": 41.12,
      "voice": "hang2",
      "pitch_index": 6,
      "duration_seconds": 0.456,
      "amplitude": 0.53
    },
    {
      "t": 41.6,
      "voice": "hang2",
      "pitch_index": 4,
      "duration_seconds": 0.912,
      "amplitude": 0.53
    },
    {
      "t": 42.56,
      "voice": "hang2",
      "pitch_index": 5,
      "duration_seconds": 0.456,
      "amplitude": 0.53
    },
    {
      "t": 2.0,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 3.12,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 4.24,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 5.36,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 6.48,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 7.6,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 8.72,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 9.84,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 10.96,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 12.08,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 13.2,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 14.32,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 15.44,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 16.56,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 17.68,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 18.8,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 19.92,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 21.04,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 22.16,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 23.28,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 24.4,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 25.52,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 26.64,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 27.76,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 28.88,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 30.0,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 31.12,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 32.24,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 33.36,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 34.48,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 35.6,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 36.72,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 37.84,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 38.96,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 40.08,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 41.2,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 42.32,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 43.44,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 44.56,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 45.68,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 46.8,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 47.92,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 49.04,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 50.16,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 51.28,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 52.4,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 53.52,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 54.64,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 55.76,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 56.88,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 58.0,
      "voice": "pot",
      "pitch_index": 1,
      "duration_seconds": 2.5,
      "amplitude": 0.7
    }
  ]
}
```

### 10. Field note
The rhythm and the pitch are each simple. The piece lives in what they are to each other as they never quite repeat.
