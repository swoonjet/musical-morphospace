# Expedition 016

### 1. System name
Pythagorean Spiral Counterpoint

### 2. Pitch organization
Pythagorean tuning. Stacked 3/2 fifths, 13 steps generated. The scale is **spiral non-closing** — the 13th fifth does not return to the starting pitch (it overshoots by the Pythagorean comma, ~23.5 cents). This means the system has no true octave equivalence and every repetition of the spiral introduces new pitches in absolute space. Ratios are reduced into a single register for playability, yielding 13 distinct pitches; the spiral's non-closure is preserved conceptually — performers ascend rather than cycle.

### 3. Rhythmic organization
Additive 3+2+3 units at 220 ms (cycle 1.76 s). The meter is regular; rhythmic ornament is essentially absent (density 0.05) — the piece is austere, long durations, clear attacks.

### 4. Formal structure
Arc buildup — slow entry, mid-piece development, climax at ~60%, decisive recession. Through-composed:
- **Exposition** — four voices of Group A enter one-by-one at ~4s intervals on four distinct lines
- **Development** — Group B's four voices answer with independent counterpoint; A re-enters with transposed versions of its original lines
- **Climax** — all eight voices overlap, staggered by 0.6 s entries
- **Recession** — voices drop out in reverse, last line cadences on home in the bass

### 5. Texture and voicing
Polyphonic independent in two call-response groups. Group A (bass, tenor, alto, soprano — vocal-male, reed, vocal-female, bamboo-flute) and Group B (plucked gut, reed, flute, bowed string) face each other antiphonally. Voice *independence* is low (0.15) in the ethnographic sense: within each group the voices move as a unified body — they are heard as "Group A speaking" rather than as four discrete voices. Between groups, the independence is the central formal device.

### 6. Ornament and inflection
None. The piece is austere — long durations, no decoration. This is unusual for Pythagorean traditions; the grammar deliberately removes ornament so that the *intervallic relationships themselves* are the material.

### 7. Performance context
Ritual-ceremonial, notated-prescriptive transmission. The eight-voice ensemble is fully written; no improvisation.

### 8. Relationship to neighboring systems
Shares with **Korean Aak court music** the austere, long-duration character and the reverence for strict intervallic ratios. Shares with **Western Romantic symphony** the arc-buildup form with climax at 60-70%. Shares with **Sephardic liturgical song** the antiphonal call-response between two groups. The unique synthesis: *eight-voice Pythagorean-spiral counterpoint organized as an arc-buildup in two antiphonal groups with no ornament — the intervals themselves carry all expressive weight*.

### 9. Audio specification

```json
{
  "duration_seconds": 92.0,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 146,
    "pitches": [
      1.0,
      1.5,
      2.0273,
      2.1357,
      2.25,
      2.4027,
      2.5312,
      2.703,
      2.8477,
      3.2036,
      3.375,
      3.6041,
      3.7969
    ],
    "octave_repeats": false
  },
  "rhythm_system": {
    "type": "additive",
    "groupings": [
      3,
      2,
      3
    ],
    "base_unit_ms": 220
  },
  "voices": [
    {
      "name": "a_bass",
      "timbre": "vocal_male_low",
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
      "rhythm_role": "melodic_lead",
      "amplitude": 0.65,
      "spatial_position": [
        -0.5,
        0.2
      ]
    },
    {
      "name": "a_ten",
      "timbre": "reed",
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
      "rhythm_role": "melodic_lead",
      "amplitude": 0.65,
      "spatial_position": [
        -0.25,
        0.2
      ]
    },
    {
      "name": "a_alt",
      "timbre": "vocal_female_high",
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
      "rhythm_role": "melodic_lead",
      "amplitude": 0.65,
      "spatial_position": [
        0.0,
        0.2
      ]
    },
    {
      "name": "a_sop",
      "timbre": "bamboo_flute",
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
      "rhythm_role": "melodic_lead",
      "amplitude": 0.65,
      "spatial_position": [
        0.25,
        0.2
      ]
    },
    {
      "name": "b_bass",
      "timbre": "plucked_gut",
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
      "rhythm_role": "melodic_lead",
      "amplitude": 0.6,
      "spatial_position": [
        0.5,
        0.15
      ]
    },
    {
      "name": "b_ten",
      "timbre": "reed",
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
      "rhythm_role": "melodic_lead",
      "amplitude": 0.6,
      "spatial_position": [
        0.35,
        0.15
      ]
    },
    {
      "name": "b_alt",
      "timbre": "bamboo_flute",
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
      "rhythm_role": "melodic_lead",
      "amplitude": 0.6,
      "spatial_position": [
        0.2,
        0.15
      ]
    },
    {
      "name": "b_sop",
      "timbre": "bowed_string",
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
      "rhythm_role": "melodic_lead",
      "amplitude": 0.6,
      "spatial_position": [
        0.45,
        0.15
      ]
    }
  ],
  "form": {
    "arc_type": "arc_buildup",
    "sections": [
      {
        "name": "exposition",
        "start_seconds": 0,
        "duration_seconds": 25,
        "character": "Group A voices enter one-by-one",
        "chord_tones": [
          0,
          2,
          4
        ]
      },
      {
        "name": "development",
        "start_seconds": 25,
        "duration_seconds": 30,
        "character": "Group B answers; A re-enters transposed",
        "chord_tones": [
          2,
          4,
          5
        ]
      },
      {
        "name": "climax",
        "start_seconds": 55,
        "duration_seconds": 15,
        "character": "all eight voices overlap at maximum density",
        "chord_tones": [
          0,
          2,
          4,
          5,
          7
        ]
      },
      {
        "name": "recession",
        "start_seconds": 70,
        "duration_seconds": 22,
        "character": "voices drop out in reverse; final bass cadence",
        "chord_tones": [
          0,
          2,
          4
        ]
      }
    ]
  },
  "ornamentation": {
    "density": 0.05,
    "rule": "No ornament."
  },
  "auto_pedal": false,
  "events": [
    {
      "t": 1.0,
      "voice": "a_bass",
      "pitch_index": 0,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 1.44,
      "voice": "a_bass",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 1.88,
      "voice": "a_bass",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 2.32,
      "voice": "a_bass",
      "pitch_index": 2,
      "duration_seconds": 0.209,
      "amplitude": 0.65
    },
    {
      "t": 2.54,
      "voice": "a_bass",
      "pitch_index": 4,
      "duration_seconds": 0.627,
      "amplitude": 0.65
    },
    {
      "t": 3.2,
      "voice": "a_bass",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 3.64,
      "voice": "a_bass",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 4.08,
      "voice": "a_bass",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 4.52,
      "voice": "a_bass",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.65
    },
    {
      "t": 5.0,
      "voice": "a_ten",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 5.44,
      "voice": "a_ten",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 5.88,
      "voice": "a_ten",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 6.32,
      "voice": "a_ten",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 6.76,
      "voice": "a_ten",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 7.2,
      "voice": "a_ten",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 7.64,
      "voice": "a_ten",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 8.08,
      "voice": "a_ten",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.65
    },
    {
      "t": 9.0,
      "voice": "a_alt",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 9.44,
      "voice": "a_alt",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 9.88,
      "voice": "a_alt",
      "pitch_index": 7,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 10.32,
      "voice": "a_alt",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 10.76,
      "voice": "a_alt",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 11.2,
      "voice": "a_alt",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 11.64,
      "voice": "a_alt",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.65
    },
    {
      "t": 13.0,
      "voice": "a_sop",
      "pitch_index": 0,
      "duration_seconds": 0.627,
      "amplitude": 0.65
    },
    {
      "t": 13.66,
      "voice": "a_sop",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 14.1,
      "voice": "a_sop",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 14.54,
      "voice": "a_sop",
      "pitch_index": 5,
      "duration_seconds": 0.627,
      "amplitude": 0.65
    },
    {
      "t": 15.2,
      "voice": "a_sop",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.65
    },
    {
      "t": 15.64,
      "voice": "a_sop",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.65
    },
    {
      "t": 26,
      "voice": "b_bass",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 26.44,
      "voice": "b_bass",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 26.88,
      "voice": "b_bass",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 27.32,
      "voice": "b_bass",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 27.76,
      "voice": "b_bass",
      "pitch_index": 0,
      "duration_seconds": 0.627,
      "amplitude": 0.62
    },
    {
      "t": 28,
      "voice": "b_ten",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 28.44,
      "voice": "b_ten",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 28.88,
      "voice": "b_ten",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 29.32,
      "voice": "b_ten",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 29.76,
      "voice": "b_ten",
      "pitch_index": 1,
      "duration_seconds": 0.627,
      "amplitude": 0.62
    },
    {
      "t": 30,
      "voice": "b_alt",
      "pitch_index": 7,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 30.44,
      "voice": "b_alt",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 30.88,
      "voice": "b_alt",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 31.32,
      "voice": "b_alt",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 31.76,
      "voice": "b_alt",
      "pitch_index": 2,
      "duration_seconds": 0.627,
      "amplitude": 0.62
    },
    {
      "t": 32,
      "voice": "b_sop",
      "pitch_index": 0,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 32.44,
      "voice": "b_sop",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 32.88,
      "voice": "b_sop",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 33.32,
      "voice": "b_sop",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 33.76,
      "voice": "b_sop",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 34.2,
      "voice": "b_sop",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.62
    },
    {
      "t": 34.64,
      "voice": "b_sop",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.62
    },
    {
      "t": 36,
      "voice": "a_bass",
      "pitch_index": 1,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 36.44,
      "voice": "a_bass",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 36.88,
      "voice": "a_bass",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 37.32,
      "voice": "a_bass",
      "pitch_index": 3,
      "duration_seconds": 0.209,
      "amplitude": 0.7
    },
    {
      "t": 37.54,
      "voice": "a_bass",
      "pitch_index": 5,
      "duration_seconds": 0.627,
      "amplitude": 0.7
    },
    {
      "t": 38.2,
      "voice": "a_bass",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 38.64,
      "voice": "a_bass",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 39.08,
      "voice": "a_bass",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 39.52,
      "voice": "a_bass",
      "pitch_index": 1,
      "duration_seconds": 0.836,
      "amplitude": 0.7
    },
    {
      "t": 38,
      "voice": "a_ten",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 38.44,
      "voice": "a_ten",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 38.88,
      "voice": "a_ten",
      "pitch_index": 7,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 39.32,
      "voice": "a_ten",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 39.76,
      "voice": "a_ten",
      "pitch_index": 8,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 40.2,
      "voice": "a_ten",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 40.64,
      "voice": "a_ten",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 41.08,
      "voice": "a_ten",
      "pitch_index": 2,
      "duration_seconds": 0.836,
      "amplitude": 0.7
    },
    {
      "t": 40,
      "voice": "a_alt",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 40.44,
      "voice": "a_alt",
      "pitch_index": 7,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 40.88,
      "voice": "a_alt",
      "pitch_index": 8,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 41.32,
      "voice": "a_alt",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 41.76,
      "voice": "a_alt",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 42.2,
      "voice": "a_alt",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 42.64,
      "voice": "a_alt",
      "pitch_index": 1,
      "duration_seconds": 0.836,
      "amplitude": 0.7
    },
    {
      "t": 42,
      "voice": "a_sop",
      "pitch_index": 3,
      "duration_seconds": 0.627,
      "amplitude": 0.7
    },
    {
      "t": 42.66,
      "voice": "a_sop",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 43.1,
      "voice": "a_sop",
      "pitch_index": 7,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 43.54,
      "voice": "a_sop",
      "pitch_index": 8,
      "duration_seconds": 0.627,
      "amplitude": 0.7
    },
    {
      "t": 44.2,
      "voice": "a_sop",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.7
    },
    {
      "t": 44.64,
      "voice": "a_sop",
      "pitch_index": 3,
      "duration_seconds": 0.836,
      "amplitude": 0.7
    },
    {
      "t": 55.0,
      "voice": "a_bass",
      "pitch_index": 0,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 55.44,
      "voice": "a_bass",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 55.88,
      "voice": "a_bass",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 56.32,
      "voice": "a_bass",
      "pitch_index": 2,
      "duration_seconds": 0.209,
      "amplitude": 0.75
    },
    {
      "t": 56.54,
      "voice": "a_bass",
      "pitch_index": 4,
      "duration_seconds": 0.627,
      "amplitude": 0.75
    },
    {
      "t": 57.2,
      "voice": "a_bass",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 57.64,
      "voice": "a_bass",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 58.08,
      "voice": "a_bass",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 58.52,
      "voice": "a_bass",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.75
    },
    {
      "t": 55.6,
      "voice": "a_ten",
      "pitch_index": 1,
      "duration_seconds": 0.627,
      "amplitude": 0.75
    },
    {
      "t": 56.26,
      "voice": "a_ten",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 56.7,
      "voice": "a_ten",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 57.14,
      "voice": "a_ten",
      "pitch_index": 6,
      "duration_seconds": 0.627,
      "amplitude": 0.75
    },
    {
      "t": 57.8,
      "voice": "a_ten",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 58.24,
      "voice": "a_ten",
      "pitch_index": 1,
      "duration_seconds": 0.836,
      "amplitude": 0.75
    },
    {
      "t": 56.2,
      "voice": "a_alt",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 56.64,
      "voice": "a_alt",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 57.08,
      "voice": "a_alt",
      "pitch_index": 7,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 57.52,
      "voice": "a_alt",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 57.96,
      "voice": "a_alt",
      "pitch_index": 8,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 58.4,
      "voice": "a_alt",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 58.84,
      "voice": "a_alt",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 59.28,
      "voice": "a_alt",
      "pitch_index": 2,
      "duration_seconds": 0.836,
      "amplitude": 0.75
    },
    {
      "t": 56.8,
      "voice": "a_sop",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 57.24,
      "voice": "a_sop",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 57.68,
      "voice": "a_sop",
      "pitch_index": 7,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 58.12,
      "voice": "a_sop",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 58.56,
      "voice": "a_sop",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 59.0,
      "voice": "a_sop",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.75
    },
    {
      "t": 59.44,
      "voice": "a_sop",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.75
    },
    {
      "t": 57.0,
      "voice": "b_bass",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 57.44,
      "voice": "b_bass",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 57.88,
      "voice": "b_bass",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 58.32,
      "voice": "b_bass",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 58.76,
      "voice": "b_bass",
      "pitch_index": 1,
      "duration_seconds": 0.627,
      "amplitude": 0.72
    },
    {
      "t": 57.6,
      "voice": "b_ten",
      "pitch_index": 8,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 58.04,
      "voice": "b_ten",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 58.48,
      "voice": "b_ten",
      "pitch_index": 7,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 58.92,
      "voice": "b_ten",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 59.36,
      "voice": "b_ten",
      "pitch_index": 3,
      "duration_seconds": 0.627,
      "amplitude": 0.72
    },
    {
      "t": 58.2,
      "voice": "b_alt",
      "pitch_index": 0,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 58.64,
      "voice": "b_alt",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 59.08,
      "voice": "b_alt",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 59.52,
      "voice": "b_alt",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 59.96,
      "voice": "b_alt",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 60.4,
      "voice": "b_alt",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 60.84,
      "voice": "b_alt",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.72
    },
    {
      "t": 58.8,
      "voice": "b_sop",
      "pitch_index": 6,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 59.24,
      "voice": "b_sop",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 59.68,
      "voice": "b_sop",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 60.12,
      "voice": "b_sop",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.72
    },
    {
      "t": 60.56,
      "voice": "b_sop",
      "pitch_index": 1,
      "duration_seconds": 0.627,
      "amplitude": 0.72
    },
    {
      "t": 72,
      "voice": "a_sop",
      "pitch_index": 0,
      "duration_seconds": 0.418,
      "amplitude": 0.55
    },
    {
      "t": 72.44,
      "voice": "a_sop",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.55
    },
    {
      "t": 72.88,
      "voice": "a_sop",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.55
    },
    {
      "t": 73.32,
      "voice": "a_sop",
      "pitch_index": 2,
      "duration_seconds": 0.209,
      "amplitude": 0.55
    },
    {
      "t": 73.54,
      "voice": "a_sop",
      "pitch_index": 4,
      "duration_seconds": 0.627,
      "amplitude": 0.55
    },
    {
      "t": 74.2,
      "voice": "a_sop",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.55
    },
    {
      "t": 74.64,
      "voice": "a_sop",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.55
    },
    {
      "t": 75.08,
      "voice": "a_sop",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.55
    },
    {
      "t": 75.52,
      "voice": "a_sop",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.55
    },
    {
      "t": 75,
      "voice": "b_alt",
      "pitch_index": 0,
      "duration_seconds": 0.418,
      "amplitude": 0.5
    },
    {
      "t": 75.44,
      "voice": "b_alt",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.5
    },
    {
      "t": 75.88,
      "voice": "b_alt",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.5
    },
    {
      "t": 76.32,
      "voice": "b_alt",
      "pitch_index": 5,
      "duration_seconds": 0.418,
      "amplitude": 0.5
    },
    {
      "t": 76.76,
      "voice": "b_alt",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.5
    },
    {
      "t": 77.2,
      "voice": "b_alt",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.5
    },
    {
      "t": 77.64,
      "voice": "b_alt",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.5
    },
    {
      "t": 79,
      "voice": "a_ten",
      "pitch_index": 0,
      "duration_seconds": 0.627,
      "amplitude": 0.5
    },
    {
      "t": 79.66,
      "voice": "a_ten",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.5
    },
    {
      "t": 80.1,
      "voice": "a_ten",
      "pitch_index": 4,
      "duration_seconds": 0.418,
      "amplitude": 0.5
    },
    {
      "t": 80.54,
      "voice": "a_ten",
      "pitch_index": 5,
      "duration_seconds": 0.627,
      "amplitude": 0.5
    },
    {
      "t": 81.2,
      "voice": "a_ten",
      "pitch_index": 3,
      "duration_seconds": 0.418,
      "amplitude": 0.5
    },
    {
      "t": 81.64,
      "voice": "a_ten",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.5
    },
    {
      "t": 83,
      "voice": "a_bass",
      "pitch_index": 0,
      "duration_seconds": 0.627,
      "amplitude": 0.55
    },
    {
      "t": 83.66,
      "voice": "a_bass",
      "pitch_index": 2,
      "duration_seconds": 0.418,
      "amplitude": 0.55
    },
    {
      "t": 84.1,
      "voice": "a_bass",
      "pitch_index": 0,
      "duration_seconds": 0.836,
      "amplitude": 0.55
    }
  ]
}
```

### 10. Field note
The spiral never closes. When the piece ends on home, it is on *one* of the homes — not the same one it started on.
