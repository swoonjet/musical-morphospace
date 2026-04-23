# Expedition 014

### 1. System name
Spatial Overtone Respiration

### 2. Pitch organization
Overtone series. The twelve first partials of a 110 Hz fundamental: 110, 220, 330, ... 1320 Hz (ratios 1 through 12). The scale is *single-cycle non-repeating* — overtones do not fold; each partial occupies a unique, never-returned position. The fundamental functions as a structural anchor but is rarely sounded as a drone. Microtonal inflection is obligatory on every note (±30 cents, independently chosen by each singer).

### 3. Rhythmic organization
Additive metric, 5+4+3 units at 350 ms unit (cycle ≈ 4.2 s). The metric is skeletal — voices attack together on phrase-starts but the grouping is felt more as breath-punctuation than pulse. Decorative pauses separate phrases within sections.

### 4. Formal structure
Nested hierarchical:
- **Breath I** (outer A) — three homophonic breath-chords on low partials [0,2,4,6]
- **Inner a1** — two chords on [0,3,5]
- **Inner a2** — two chords on higher partials [2,4,6,8]
- **Breath II** (outer B) — three chords on widened [0,4,7,10]
- **Inner b1** — two chords on [0,5,8]
- **Inner b2** — two chords on highest partials [3,6,9,11]
- **Breath III** (return) — three chords converging back to [0,2,4]

Each outer section contains two inner sections; the seven named sections nest into a breath-I / breath-II / breath-III arch.

### 5. Texture and voicing
Homophonic — all voices attack together on each breath — but voice independence is near-maximal: each singer chooses which of the section's chord tones to land on, independently, so the *attack* is unison but the *chord* is improvised by the collective each phrase. Five voices spatially distributed hard-panned across the stereo field (-0.85 to +0.85).

### 6. Ornament and inflection
Microtonal inflection is core. Every pitch bends ±30 cents sinusoidally at onset. Each singer's curve is independent, so the five voices form a slowly rippling microtonal cloud at each attack.

### 7. Performance context
Ritual. The spatial distribution is its structure — listeners walk through the choir rather than facing it. No drone ensures the overtone partials hang alone in space.

### 8. Relationship to neighboring systems
Shares with **Bulgarian women's choir** the close-interval homophony and the partial-stacking logic. Shares with **Tuvan khoomei** the overtone-series material. Shares with **Turkish classical makam** the ensemble microtonal coordination (obligatory inflection). The unique synthesis: *homophonic breath-chord ensemble where attack is unison but pitch choice within the chord is improvised, voices dispersed in space, and microtonal inflection is each singer's own*.

### 9. Audio specification

```json
{
  "duration_seconds": 73.0,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 110,
    "pitches": [
      1.0,
      2.0,
      3.0,
      4.0,
      5.0,
      6.0,
      7.0,
      8.0,
      9.0,
      10.0,
      11.0,
      12.0
    ],
    "octave_repeats": false,
    "inflection_rules": [
      {
        "pitch_index": 0,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 1,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 2,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 3,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 4,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 5,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 6,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 7,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 8,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 9,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 10,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      },
      {
        "pitch_index": 11,
        "inflection_cents_range": [
          -30,
          30
        ],
        "direction": "both"
      }
    ]
  },
  "rhythm_system": {
    "type": "additive",
    "groupings": [
      5,
      4,
      3
    ],
    "base_unit_ms": 350
  },
  "voices": [
    {
      "name": "v1",
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
        11
      ],
      "rhythm_role": "breath_phrase",
      "amplitude": 0.55,
      "spatial_position": [
        -0.85,
        0.1
      ]
    },
    {
      "name": "v2",
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
        11
      ],
      "rhythm_role": "breath_phrase",
      "amplitude": 0.55,
      "spatial_position": [
        -0.45,
        0.1
      ]
    },
    {
      "name": "v3",
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
        11
      ],
      "rhythm_role": "breath_phrase",
      "amplitude": 0.55,
      "spatial_position": [
        0.0,
        0.1
      ]
    },
    {
      "name": "v4",
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
        11
      ],
      "rhythm_role": "breath_phrase",
      "amplitude": 0.55,
      "spatial_position": [
        0.45,
        0.1
      ]
    },
    {
      "name": "v5",
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
        11
      ],
      "rhythm_role": "breath_phrase",
      "amplitude": 0.55,
      "spatial_position": [
        0.85,
        0.1
      ]
    }
  ],
  "form": {
    "arc_type": "nested_hierarchical",
    "sections": [
      {
        "name": "breath_I_outer_A",
        "start_seconds": 0.0,
        "duration_seconds": 14,
        "chord_tones": [
          0,
          2,
          4,
          6
        ],
        "character": "homophonic breath chord from [0, 2, 4, 6]"
      },
      {
        "name": "breath_I_inner_a1",
        "start_seconds": 14.0,
        "duration_seconds": 8,
        "chord_tones": [
          0,
          3,
          5
        ],
        "character": "homophonic breath chord from [0, 3, 5]"
      },
      {
        "name": "breath_I_inner_a2",
        "start_seconds": 22.0,
        "duration_seconds": 8,
        "chord_tones": [
          2,
          4,
          6,
          8
        ],
        "character": "homophonic breath chord from [2, 4, 6, 8]"
      },
      {
        "name": "breath_II_outer_B",
        "start_seconds": 30.0,
        "duration_seconds": 14,
        "chord_tones": [
          0,
          4,
          7,
          10
        ],
        "character": "homophonic breath chord from [0, 4, 7, 10]"
      },
      {
        "name": "breath_II_inner_b1",
        "start_seconds": 44.0,
        "duration_seconds": 8,
        "chord_tones": [
          0,
          5,
          8
        ],
        "character": "homophonic breath chord from [0, 5, 8]"
      },
      {
        "name": "breath_II_inner_b2",
        "start_seconds": 52.0,
        "duration_seconds": 8,
        "chord_tones": [
          3,
          6,
          9,
          11
        ],
        "character": "homophonic breath chord from [3, 6, 9, 11]"
      },
      {
        "name": "breath_III_return",
        "start_seconds": 60.0,
        "duration_seconds": 12,
        "chord_tones": [
          0,
          2,
          4
        ],
        "character": "homophonic breath chord from [0, 2, 4]"
      }
    ]
  },
  "ornamentation": {
    "density": 0.85,
    "rule": "Microtonal inflection core: every pitch bends \u00b130 cents at onset. Each singer improvises inflection curve independently \u2014 this is the only dimension of improvisation; pitch choice within a chord is also free."
  },
  "auto_pedal": false,
  "events": [
    {
      "t": 0.0,
      "voice": "v1",
      "pitch_index": 6,
      "duration_seconds": 3.027,
      "amplitude": 0.598
    },
    {
      "t": 0.0,
      "voice": "v2",
      "pitch_index": 2,
      "duration_seconds": 3.027,
      "amplitude": 0.475
    },
    {
      "t": 0.0,
      "voice": "v3",
      "pitch_index": 6,
      "duration_seconds": 3.027,
      "amplitude": 0.443
    },
    {
      "t": 0.0,
      "voice": "v4",
      "pitch_index": 6,
      "duration_seconds": 3.027,
      "amplitude": 0.484
    },
    {
      "t": 0.0,
      "voice": "v5",
      "pitch_index": 0,
      "duration_seconds": 3.027,
      "amplitude": 0.552
    },
    {
      "t": 4.282,
      "voice": "v1",
      "pitch_index": 6,
      "duration_seconds": 3.391,
      "amplitude": 0.559
    },
    {
      "t": 4.282,
      "voice": "v2",
      "pitch_index": 6,
      "duration_seconds": 3.391,
      "amplitude": 0.542
    },
    {
      "t": 4.282,
      "voice": "v3",
      "pitch_index": 4,
      "duration_seconds": 3.391,
      "amplitude": 0.45
    },
    {
      "t": 4.282,
      "voice": "v4",
      "pitch_index": 4,
      "duration_seconds": 3.391,
      "amplitude": 0.481
    },
    {
      "t": 4.282,
      "voice": "v5",
      "pitch_index": 4,
      "duration_seconds": 3.391,
      "amplitude": 0.515
    },
    {
      "t": 9.267,
      "voice": "v1",
      "pitch_index": 2,
      "duration_seconds": 3.105,
      "amplitude": 0.597
    },
    {
      "t": 9.267,
      "voice": "v2",
      "pitch_index": 6,
      "duration_seconds": 3.105,
      "amplitude": 0.475
    },
    {
      "t": 9.267,
      "voice": "v3",
      "pitch_index": 6,
      "duration_seconds": 3.105,
      "amplitude": 0.441
    },
    {
      "t": 9.267,
      "voice": "v4",
      "pitch_index": 4,
      "duration_seconds": 3.105,
      "amplitude": 0.486
    },
    {
      "t": 9.267,
      "voice": "v5",
      "pitch_index": 4,
      "duration_seconds": 3.105,
      "amplitude": 0.516
    },
    {
      "t": 14.0,
      "voice": "v1",
      "pitch_index": 5,
      "duration_seconds": 2.682,
      "amplitude": 0.516
    },
    {
      "t": 14.0,
      "voice": "v2",
      "pitch_index": 5,
      "duration_seconds": 2.682,
      "amplitude": 0.481
    },
    {
      "t": 14.0,
      "voice": "v3",
      "pitch_index": 0,
      "duration_seconds": 2.682,
      "amplitude": 0.445
    },
    {
      "t": 14.0,
      "voice": "v4",
      "pitch_index": 3,
      "duration_seconds": 2.682,
      "amplitude": 0.496
    },
    {
      "t": 14.0,
      "voice": "v5",
      "pitch_index": 5,
      "duration_seconds": 2.682,
      "amplitude": 0.535
    },
    {
      "t": 18.0,
      "voice": "v1",
      "pitch_index": 0,
      "duration_seconds": 2.801,
      "amplitude": 0.558
    },
    {
      "t": 18.0,
      "voice": "v2",
      "pitch_index": 3,
      "duration_seconds": 2.801,
      "amplitude": 0.524
    },
    {
      "t": 18.0,
      "voice": "v3",
      "pitch_index": 0,
      "duration_seconds": 2.801,
      "amplitude": 0.498
    },
    {
      "t": 18.0,
      "voice": "v4",
      "pitch_index": 3,
      "duration_seconds": 2.801,
      "amplitude": 0.483
    },
    {
      "t": 18.0,
      "voice": "v5",
      "pitch_index": 5,
      "duration_seconds": 2.801,
      "amplitude": 0.602
    },
    {
      "t": 22.0,
      "voice": "v1",
      "pitch_index": 2,
      "duration_seconds": 2.801,
      "amplitude": 0.599
    },
    {
      "t": 22.0,
      "voice": "v2",
      "pitch_index": 2,
      "duration_seconds": 2.801,
      "amplitude": 0.525
    },
    {
      "t": 22.0,
      "voice": "v3",
      "pitch_index": 8,
      "duration_seconds": 2.801,
      "amplitude": 0.449
    },
    {
      "t": 22.0,
      "voice": "v4",
      "pitch_index": 6,
      "duration_seconds": 2.801,
      "amplitude": 0.537
    },
    {
      "t": 22.0,
      "voice": "v5",
      "pitch_index": 2,
      "duration_seconds": 2.801,
      "amplitude": 0.521
    },
    {
      "t": 26.254,
      "voice": "v1",
      "pitch_index": 8,
      "duration_seconds": 2.98,
      "amplitude": 0.539
    },
    {
      "t": 26.254,
      "voice": "v2",
      "pitch_index": 2,
      "duration_seconds": 2.98,
      "amplitude": 0.501
    },
    {
      "t": 26.254,
      "voice": "v3",
      "pitch_index": 4,
      "duration_seconds": 2.98,
      "amplitude": 0.527
    },
    {
      "t": 26.254,
      "voice": "v4",
      "pitch_index": 4,
      "duration_seconds": 2.98,
      "amplitude": 0.484
    },
    {
      "t": 26.254,
      "voice": "v5",
      "pitch_index": 8,
      "duration_seconds": 2.98,
      "amplitude": 0.582
    },
    {
      "t": 30.0,
      "voice": "v1",
      "pitch_index": 4,
      "duration_seconds": 3.534,
      "amplitude": 0.519
    },
    {
      "t": 30.0,
      "voice": "v2",
      "pitch_index": 7,
      "duration_seconds": 3.534,
      "amplitude": 0.483
    },
    {
      "t": 30.0,
      "voice": "v3",
      "pitch_index": 0,
      "duration_seconds": 3.534,
      "amplitude": 0.446
    },
    {
      "t": 30.0,
      "voice": "v4",
      "pitch_index": 0,
      "duration_seconds": 3.534,
      "amplitude": 0.488
    },
    {
      "t": 30.0,
      "voice": "v5",
      "pitch_index": 10,
      "duration_seconds": 3.534,
      "amplitude": 0.534
    },
    {
      "t": 35.042,
      "voice": "v1",
      "pitch_index": 4,
      "duration_seconds": 4.071,
      "amplitude": 0.56
    },
    {
      "t": 35.042,
      "voice": "v2",
      "pitch_index": 7,
      "duration_seconds": 4.071,
      "amplitude": 0.532
    },
    {
      "t": 35.042,
      "voice": "v3",
      "pitch_index": 4,
      "duration_seconds": 4.071,
      "amplitude": 0.485
    },
    {
      "t": 35.042,
      "voice": "v4",
      "pitch_index": 0,
      "duration_seconds": 4.071,
      "amplitude": 0.538
    },
    {
      "t": 35.042,
      "voice": "v5",
      "pitch_index": 7,
      "duration_seconds": 4.071,
      "amplitude": 0.57
    },
    {
      "t": 40.509,
      "voice": "v1",
      "pitch_index": 10,
      "duration_seconds": 3.921,
      "amplitude": 0.538
    },
    {
      "t": 40.509,
      "voice": "v2",
      "pitch_index": 4,
      "duration_seconds": 3.921,
      "amplitude": 0.473
    },
    {
      "t": 40.509,
      "voice": "v3",
      "pitch_index": 0,
      "duration_seconds": 3.921,
      "amplitude": 0.453
    },
    {
      "t": 40.509,
      "voice": "v4",
      "pitch_index": 0,
      "duration_seconds": 3.921,
      "amplitude": 0.53
    },
    {
      "t": 40.509,
      "voice": "v5",
      "pitch_index": 4,
      "duration_seconds": 3.921,
      "amplitude": 0.605
    },
    {
      "t": 44.0,
      "voice": "v1",
      "pitch_index": 5,
      "duration_seconds": 3.518,
      "amplitude": 0.558
    },
    {
      "t": 44.0,
      "voice": "v2",
      "pitch_index": 8,
      "duration_seconds": 3.518,
      "amplitude": 0.522
    },
    {
      "t": 44.0,
      "voice": "v3",
      "pitch_index": 0,
      "duration_seconds": 3.518,
      "amplitude": 0.476
    },
    {
      "t": 44.0,
      "voice": "v4",
      "pitch_index": 5,
      "duration_seconds": 3.518,
      "amplitude": 0.476
    },
    {
      "t": 44.0,
      "voice": "v5",
      "pitch_index": 0,
      "duration_seconds": 3.518,
      "amplitude": 0.559
    },
    {
      "t": 48.746,
      "voice": "v1",
      "pitch_index": 8,
      "duration_seconds": 3.44,
      "amplitude": 0.564
    },
    {
      "t": 48.746,
      "voice": "v2",
      "pitch_index": 0,
      "duration_seconds": 3.44,
      "amplitude": 0.516
    },
    {
      "t": 48.746,
      "voice": "v3",
      "pitch_index": 5,
      "duration_seconds": 3.44,
      "amplitude": 0.467
    },
    {
      "t": 48.746,
      "voice": "v4",
      "pitch_index": 8,
      "duration_seconds": 3.44,
      "amplitude": 0.46
    },
    {
      "t": 48.746,
      "voice": "v5",
      "pitch_index": 8,
      "duration_seconds": 3.44,
      "amplitude": 0.583
    },
    {
      "t": 52.0,
      "voice": "v1",
      "pitch_index": 6,
      "duration_seconds": 3.819,
      "amplitude": 0.603
    },
    {
      "t": 52.0,
      "voice": "v2",
      "pitch_index": 11,
      "duration_seconds": 3.819,
      "amplitude": 0.519
    },
    {
      "t": 52.0,
      "voice": "v3",
      "pitch_index": 3,
      "duration_seconds": 3.819,
      "amplitude": 0.502
    },
    {
      "t": 52.0,
      "voice": "v4",
      "pitch_index": 9,
      "duration_seconds": 3.819,
      "amplitude": 0.485
    },
    {
      "t": 52.0,
      "voice": "v5",
      "pitch_index": 3,
      "duration_seconds": 3.819,
      "amplitude": 0.579
    },
    {
      "t": 57.424,
      "voice": "v1",
      "pitch_index": 9,
      "duration_seconds": 3.787,
      "amplitude": 0.519
    },
    {
      "t": 57.424,
      "voice": "v2",
      "pitch_index": 6,
      "duration_seconds": 3.787,
      "amplitude": 0.46
    },
    {
      "t": 57.424,
      "voice": "v3",
      "pitch_index": 9,
      "duration_seconds": 3.787,
      "amplitude": 0.439
    },
    {
      "t": 57.424,
      "voice": "v4",
      "pitch_index": 6,
      "duration_seconds": 3.787,
      "amplitude": 0.488
    },
    {
      "t": 57.424,
      "voice": "v5",
      "pitch_index": 11,
      "duration_seconds": 3.787,
      "amplitude": 0.526
    },
    {
      "t": 60.0,
      "voice": "v1",
      "pitch_index": 0,
      "duration_seconds": 2.809,
      "amplitude": 0.508
    },
    {
      "t": 60.0,
      "voice": "v2",
      "pitch_index": 4,
      "duration_seconds": 2.809,
      "amplitude": 0.486
    },
    {
      "t": 60.0,
      "voice": "v3",
      "pitch_index": 4,
      "duration_seconds": 2.809,
      "amplitude": 0.505
    },
    {
      "t": 60.0,
      "voice": "v4",
      "pitch_index": 4,
      "duration_seconds": 2.809,
      "amplitude": 0.508
    },
    {
      "t": 60.0,
      "voice": "v5",
      "pitch_index": 2,
      "duration_seconds": 2.809,
      "amplitude": 0.51
    },
    {
      "t": 63.959,
      "voice": "v1",
      "pitch_index": 2,
      "duration_seconds": 3.377,
      "amplitude": 0.557
    },
    {
      "t": 63.959,
      "voice": "v2",
      "pitch_index": 4,
      "duration_seconds": 3.377,
      "amplitude": 0.517
    },
    {
      "t": 63.959,
      "voice": "v3",
      "pitch_index": 0,
      "duration_seconds": 3.377,
      "amplitude": 0.49
    },
    {
      "t": 63.959,
      "voice": "v4",
      "pitch_index": 4,
      "duration_seconds": 3.377,
      "amplitude": 0.523
    },
    {
      "t": 63.959,
      "voice": "v5",
      "pitch_index": 4,
      "duration_seconds": 3.377,
      "amplitude": 0.601
    },
    {
      "t": 68.82,
      "voice": "v1",
      "pitch_index": 2,
      "duration_seconds": 3.371,
      "amplitude": 0.556
    },
    {
      "t": 68.82,
      "voice": "v2",
      "pitch_index": 0,
      "duration_seconds": 3.371,
      "amplitude": 0.505
    },
    {
      "t": 68.82,
      "voice": "v3",
      "pitch_index": 4,
      "duration_seconds": 3.371,
      "amplitude": 0.445
    },
    {
      "t": 68.82,
      "voice": "v4",
      "pitch_index": 2,
      "duration_seconds": 3.371,
      "amplitude": 0.481
    },
    {
      "t": 68.82,
      "voice": "v5",
      "pitch_index": 0,
      "duration_seconds": 3.371,
      "amplitude": 0.514
    }
  ]
}
```

### 10. Field note
Five singers stand in the room. They breathe together. The chord is different each time; the breath is the same.
