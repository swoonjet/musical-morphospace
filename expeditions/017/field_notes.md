# Expedition 017

### 1. System name
Inharmonic Contemplation

### 2. Pitch organization
Inharmonic spectral tuning. Pitches are derived from a spiral of near-fifths (step ratios 1.495 ± 0.04 — deliberately irregular), stacked and reduced into a single register to yield 11 distinct pitches. The scale is **spiral non-closing**: each traversal of the spiral introduces new pitches. No octave equivalence. The reference pitch 120 Hz is sustained by a continuous drone at moderate amplitude; it provides a *weak* harmonic ground (drone_presence 0.42) — present but not dominant.

### 3. Rhythmic organization
Additive 4+5 at 450 ms unit (cycle 4.05 s). The meter is nominal — voices enter and sustain on their own timing within each phrase, with 2-3 seconds of silence between phrases. Silence is weighted equal to sound: the gaps are part of the piece, not between parts of it.

### 4. Formal structure
Static contemplation. No development, no arc. Three long sections, each 25-30 s, each holds a near-constant eight-voice heterophonic cluster with minor variation. The cluster migrates across three positions — low, neighbor, narrow — but *within* each section nothing happens. The piece is about attention, not events.

### 5. Texture and voicing
Homophonic / heterophonic group. Eight voices — two low male, two reed, two high female, bamboo flute, bowed string — spread across the stereo field from -0.7 to +0.7. Each voice picks independently from the section's chord tones each phrase, and attacks with a small timing offset (0-0.5 s), producing a slowly-evolving near-unison cloud.

### 6. Ornament and inflection
Essentially none (density 0.05). Voices simply sustain.

### 7. Performance context
Ritual-contemplative. Listener and performer are equal in attention; the piece has no audience and no narrative.

### 8. Relationship to neighboring systems
Shares with **Andean Quechua wayno** the heterophonic ensemble realization. Shares with **Zulu isicathamiya** the a-cappella choral homophony. Shares with **Mexican mariachi** the eight-voice ensemble scale. Diverges from all three by refusing arc, narrative, and rhythmic event. The unique synthesis: *eight-voice heterophonic chorale in an inharmonic spiral tuning with no development — three positions held at length, equal silence, no ornament*.

### 9. Audio specification

```json
{
  "duration_seconds": 88.0,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 120,
    "pitches": [
      1.0,
      1.4855,
      2.201,
      3.2998,
      3.3283,
      3.7042,
      3.751,
      4.3283,
      4.9104,
      5.0384,
      5.686
    ],
    "octave_repeats": false
  },
  "rhythm_system": {
    "type": "additive",
    "groupings": [
      4,
      5
    ],
    "base_unit_ms": 450
  },
  "voices": [
    {
      "name": "drone",
      "timbre": "soft_pad",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "sustained_drone",
      "amplitude": 0.32,
      "spatial_position": [
        0.0,
        -0.3
      ]
    },
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
        10
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.42,
      "spatial_position": [
        -0.7,
        0.0
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
        10
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.42,
      "spatial_position": [
        -0.5,
        -0.1
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
        10
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.42,
      "spatial_position": [
        -0.3,
        0.1
      ]
    },
    {
      "name": "v4",
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
        10
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.42,
      "spatial_position": [
        -0.1,
        0.2
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
        10
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.42,
      "spatial_position": [
        0.1,
        0.15
      ]
    },
    {
      "name": "v6",
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
        10
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.42,
      "spatial_position": [
        0.3,
        0.1
      ]
    },
    {
      "name": "v7",
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
        10
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.42,
      "spatial_position": [
        0.5,
        0.05
      ]
    },
    {
      "name": "v8",
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
        10
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.42,
      "spatial_position": [
        0.7,
        0.0
      ]
    }
  ],
  "form": {
    "arc_type": "static",
    "sections": [
      {
        "name": "A_cluster_low",
        "start_seconds": 0,
        "duration_seconds": 28,
        "character": "eight-voice heterophonic cluster on lower partials",
        "chord_tones": [
          0,
          2,
          4,
          6
        ]
      },
      {
        "name": "B_cluster_shift",
        "start_seconds": 28,
        "duration_seconds": 30,
        "character": "cluster shifts to neighboring partials",
        "chord_tones": [
          1,
          3,
          5,
          7
        ]
      },
      {
        "name": "C_cluster_narrow",
        "start_seconds": 58,
        "duration_seconds": 30,
        "character": "cluster narrows around tonic family",
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
    "rule": "None \u2014 voices simply sustain their chosen partial for each phrase."
  },
  "events": [
    {
      "t": 0.884,
      "voice": "v1",
      "pitch_index": 4,
      "duration_seconds": 4.58,
      "amplitude": 0.45
    },
    {
      "t": 0.544,
      "voice": "v2",
      "pitch_index": 4,
      "duration_seconds": 4.315,
      "amplitude": 0.4
    },
    {
      "t": 0.601,
      "voice": "v3",
      "pitch_index": 6,
      "duration_seconds": 4.793,
      "amplitude": 0.391
    },
    {
      "t": 0.555,
      "voice": "v4",
      "pitch_index": 6,
      "duration_seconds": 4.843,
      "amplitude": 0.368
    },
    {
      "t": 0.56,
      "voice": "v5",
      "pitch_index": 2,
      "duration_seconds": 4.999,
      "amplitude": 0.423
    },
    {
      "t": 0.632,
      "voice": "v6",
      "pitch_index": 2,
      "duration_seconds": 4.412,
      "amplitude": 0.443
    },
    {
      "t": 0.624,
      "voice": "v7",
      "pitch_index": 0,
      "duration_seconds": 4.37,
      "amplitude": 0.472
    },
    {
      "t": 0.756,
      "voice": "v8",
      "pitch_index": 6,
      "duration_seconds": 4.893,
      "amplitude": 0.439
    },
    {
      "t": 7.46,
      "voice": "v1",
      "pitch_index": 4,
      "duration_seconds": 4.633,
      "amplitude": 0.357
    },
    {
      "t": 7.473,
      "voice": "v2",
      "pitch_index": 4,
      "duration_seconds": 4.739,
      "amplitude": 0.425
    },
    {
      "t": 7.8,
      "voice": "v3",
      "pitch_index": 0,
      "duration_seconds": 4.5,
      "amplitude": 0.422
    },
    {
      "t": 7.663,
      "voice": "v4",
      "pitch_index": 2,
      "duration_seconds": 4.621,
      "amplitude": 0.385
    },
    {
      "t": 7.53,
      "voice": "v5",
      "pitch_index": 4,
      "duration_seconds": 4.866,
      "amplitude": 0.422
    },
    {
      "t": 7.553,
      "voice": "v6",
      "pitch_index": 2,
      "duration_seconds": 4.569,
      "amplitude": 0.395
    },
    {
      "t": 7.585,
      "voice": "v7",
      "pitch_index": 2,
      "duration_seconds": 5.172,
      "amplitude": 0.425
    },
    {
      "t": 7.587,
      "voice": "v8",
      "pitch_index": 4,
      "duration_seconds": 4.311,
      "amplitude": 0.479
    },
    {
      "t": 14.237,
      "voice": "v1",
      "pitch_index": 6,
      "duration_seconds": 5.466,
      "amplitude": 0.39
    },
    {
      "t": 14.283,
      "voice": "v2",
      "pitch_index": 0,
      "duration_seconds": 5.451,
      "amplitude": 0.413
    },
    {
      "t": 14.145,
      "voice": "v3",
      "pitch_index": 2,
      "duration_seconds": 5.469,
      "amplitude": 0.475
    },
    {
      "t": 14.057,
      "voice": "v4",
      "pitch_index": 6,
      "duration_seconds": 5.759,
      "amplitude": 0.475
    },
    {
      "t": 14.347,
      "voice": "v5",
      "pitch_index": 0,
      "duration_seconds": 4.721,
      "amplitude": 0.477
    },
    {
      "t": 14.306,
      "voice": "v6",
      "pitch_index": 4,
      "duration_seconds": 5.676,
      "amplitude": 0.455
    },
    {
      "t": 14.049,
      "voice": "v7",
      "pitch_index": 0,
      "duration_seconds": 5.126,
      "amplitude": 0.44
    },
    {
      "t": 14.32,
      "voice": "v8",
      "pitch_index": 4,
      "duration_seconds": 5.388,
      "amplitude": 0.402
    },
    {
      "t": 21.138,
      "voice": "v1",
      "pitch_index": 2,
      "duration_seconds": 4.344,
      "amplitude": 0.425
    },
    {
      "t": 21.068,
      "voice": "v2",
      "pitch_index": 4,
      "duration_seconds": 4.285,
      "amplitude": 0.426
    },
    {
      "t": 21.137,
      "voice": "v3",
      "pitch_index": 6,
      "duration_seconds": 3.885,
      "amplitude": 0.431
    },
    {
      "t": 21.435,
      "voice": "v4",
      "pitch_index": 0,
      "duration_seconds": 4.172,
      "amplitude": 0.38
    },
    {
      "t": 21.376,
      "voice": "v5",
      "pitch_index": 4,
      "duration_seconds": 4.354,
      "amplitude": 0.428
    },
    {
      "t": 21.07,
      "voice": "v6",
      "pitch_index": 6,
      "duration_seconds": 4.239,
      "amplitude": 0.475
    },
    {
      "t": 21.42,
      "voice": "v7",
      "pitch_index": 2,
      "duration_seconds": 4.008,
      "amplitude": 0.43
    },
    {
      "t": 21.117,
      "voice": "v8",
      "pitch_index": 4,
      "duration_seconds": 4.356,
      "amplitude": 0.377
    },
    {
      "t": 27.36,
      "voice": "v1",
      "pitch_index": 0,
      "duration_seconds": 4.676,
      "amplitude": 0.375
    },
    {
      "t": 27.332,
      "voice": "v2",
      "pitch_index": 2,
      "duration_seconds": 4.6,
      "amplitude": 0.416
    },
    {
      "t": 27.334,
      "voice": "v3",
      "pitch_index": 6,
      "duration_seconds": 4.452,
      "amplitude": 0.374
    },
    {
      "t": 27.483,
      "voice": "v4",
      "pitch_index": 0,
      "duration_seconds": 4.621,
      "amplitude": 0.448
    },
    {
      "t": 27.173,
      "voice": "v5",
      "pitch_index": 2,
      "duration_seconds": 4.26,
      "amplitude": 0.437
    },
    {
      "t": 27.163,
      "voice": "v6",
      "pitch_index": 0,
      "duration_seconds": 4.625,
      "amplitude": 0.468
    },
    {
      "t": 27.55,
      "voice": "v7",
      "pitch_index": 2,
      "duration_seconds": 4.26,
      "amplitude": 0.468
    },
    {
      "t": 27.335,
      "voice": "v8",
      "pitch_index": 0,
      "duration_seconds": 4.968,
      "amplitude": 0.47
    },
    {
      "t": 29.397,
      "voice": "v1",
      "pitch_index": 7,
      "duration_seconds": 4.266,
      "amplitude": 0.358
    },
    {
      "t": 29.094,
      "voice": "v2",
      "pitch_index": 1,
      "duration_seconds": 4.367,
      "amplitude": 0.385
    },
    {
      "t": 29.47,
      "voice": "v3",
      "pitch_index": 5,
      "duration_seconds": 4.406,
      "amplitude": 0.48
    },
    {
      "t": 29.203,
      "voice": "v4",
      "pitch_index": 7,
      "duration_seconds": 3.883,
      "amplitude": 0.448
    },
    {
      "t": 29.04,
      "voice": "v5",
      "pitch_index": 5,
      "duration_seconds": 4.559,
      "amplitude": 0.453
    },
    {
      "t": 29.163,
      "voice": "v6",
      "pitch_index": 5,
      "duration_seconds": 3.983,
      "amplitude": 0.367
    },
    {
      "t": 29.462,
      "voice": "v7",
      "pitch_index": 3,
      "duration_seconds": 4.625,
      "amplitude": 0.408
    },
    {
      "t": 29.125,
      "voice": "v8",
      "pitch_index": 5,
      "duration_seconds": 4.497,
      "amplitude": 0.39
    },
    {
      "t": 36.013,
      "voice": "v1",
      "pitch_index": 3,
      "duration_seconds": 5.466,
      "amplitude": 0.424
    },
    {
      "t": 35.802,
      "voice": "v2",
      "pitch_index": 5,
      "duration_seconds": 4.904,
      "amplitude": 0.467
    },
    {
      "t": 36.092,
      "voice": "v3",
      "pitch_index": 3,
      "duration_seconds": 4.596,
      "amplitude": 0.426
    },
    {
      "t": 36.007,
      "voice": "v4",
      "pitch_index": 5,
      "duration_seconds": 5.36,
      "amplitude": 0.387
    },
    {
      "t": 35.793,
      "voice": "v5",
      "pitch_index": 7,
      "duration_seconds": 4.694,
      "amplitude": 0.467
    },
    {
      "t": 36.149,
      "voice": "v6",
      "pitch_index": 3,
      "duration_seconds": 4.893,
      "amplitude": 0.392
    },
    {
      "t": 36.135,
      "voice": "v7",
      "pitch_index": 7,
      "duration_seconds": 5.283,
      "amplitude": 0.388
    },
    {
      "t": 36.008,
      "voice": "v8",
      "pitch_index": 3,
      "duration_seconds": 4.972,
      "amplitude": 0.398
    },
    {
      "t": 43.842,
      "voice": "v1",
      "pitch_index": 1,
      "duration_seconds": 5.314,
      "amplitude": 0.399
    },
    {
      "t": 43.662,
      "voice": "v2",
      "pitch_index": 3,
      "duration_seconds": 4.701,
      "amplitude": 0.388
    },
    {
      "t": 43.787,
      "voice": "v3",
      "pitch_index": 7,
      "duration_seconds": 5.391,
      "amplitude": 0.447
    },
    {
      "t": 43.818,
      "voice": "v4",
      "pitch_index": 5,
      "duration_seconds": 4.731,
      "amplitude": 0.425
    },
    {
      "t": 43.845,
      "voice": "v5",
      "pitch_index": 3,
      "duration_seconds": 5.376,
      "amplitude": 0.448
    },
    {
      "t": 43.745,
      "voice": "v6",
      "pitch_index": 5,
      "duration_seconds": 4.615,
      "amplitude": 0.463
    },
    {
      "t": 43.815,
      "voice": "v7",
      "pitch_index": 7,
      "duration_seconds": 5.372,
      "amplitude": 0.39
    },
    {
      "t": 44.067,
      "voice": "v8",
      "pitch_index": 3,
      "duration_seconds": 4.407,
      "amplitude": 0.463
    },
    {
      "t": 51.581,
      "voice": "v1",
      "pitch_index": 7,
      "duration_seconds": 5.058,
      "amplitude": 0.44
    },
    {
      "t": 51.825,
      "voice": "v2",
      "pitch_index": 7,
      "duration_seconds": 5.403,
      "amplitude": 0.448
    },
    {
      "t": 51.474,
      "voice": "v3",
      "pitch_index": 3,
      "duration_seconds": 5.312,
      "amplitude": 0.446
    },
    {
      "t": 51.494,
      "voice": "v4",
      "pitch_index": 3,
      "duration_seconds": 5.083,
      "amplitude": 0.399
    },
    {
      "t": 51.708,
      "voice": "v5",
      "pitch_index": 7,
      "duration_seconds": 4.793,
      "amplitude": 0.415
    },
    {
      "t": 51.849,
      "voice": "v6",
      "pitch_index": 3,
      "duration_seconds": 4.927,
      "amplitude": 0.407
    },
    {
      "t": 51.444,
      "voice": "v7",
      "pitch_index": 1,
      "duration_seconds": 5.338,
      "amplitude": 0.45
    },
    {
      "t": 51.722,
      "voice": "v8",
      "pitch_index": 3,
      "duration_seconds": 4.817,
      "amplitude": 0.393
    },
    {
      "t": 59.38,
      "voice": "v1",
      "pitch_index": 2,
      "duration_seconds": 5.378,
      "amplitude": 0.426
    },
    {
      "t": 59.005,
      "voice": "v2",
      "pitch_index": 2,
      "duration_seconds": 4.515,
      "amplitude": 0.427
    },
    {
      "t": 59.193,
      "voice": "v3",
      "pitch_index": 4,
      "duration_seconds": 5.409,
      "amplitude": 0.358
    },
    {
      "t": 59.106,
      "voice": "v4",
      "pitch_index": 0,
      "duration_seconds": 4.547,
      "amplitude": 0.356
    },
    {
      "t": 59.014,
      "voice": "v5",
      "pitch_index": 0,
      "duration_seconds": 4.542,
      "amplitude": 0.384
    },
    {
      "t": 59.36,
      "voice": "v6",
      "pitch_index": 0,
      "duration_seconds": 5.294,
      "amplitude": 0.405
    },
    {
      "t": 59.125,
      "voice": "v7",
      "pitch_index": 4,
      "duration_seconds": 4.806,
      "amplitude": 0.366
    },
    {
      "t": 59.014,
      "voice": "v8",
      "pitch_index": 4,
      "duration_seconds": 5.086,
      "amplitude": 0.411
    },
    {
      "t": 66.258,
      "voice": "v1",
      "pitch_index": 0,
      "duration_seconds": 4.45,
      "amplitude": 0.402
    },
    {
      "t": 66.357,
      "voice": "v2",
      "pitch_index": 2,
      "duration_seconds": 4.935,
      "amplitude": 0.351
    },
    {
      "t": 66.126,
      "voice": "v3",
      "pitch_index": 2,
      "duration_seconds": 4.619,
      "amplitude": 0.42
    },
    {
      "t": 66.123,
      "voice": "v4",
      "pitch_index": 2,
      "duration_seconds": 4.396,
      "amplitude": 0.4
    },
    {
      "t": 66.116,
      "voice": "v5",
      "pitch_index": 0,
      "duration_seconds": 4.955,
      "amplitude": 0.425
    },
    {
      "t": 66.221,
      "voice": "v6",
      "pitch_index": 0,
      "duration_seconds": 5.123,
      "amplitude": 0.344
    },
    {
      "t": 66.352,
      "voice": "v7",
      "pitch_index": 2,
      "duration_seconds": 4.845,
      "amplitude": 0.386
    },
    {
      "t": 66.055,
      "voice": "v8",
      "pitch_index": 4,
      "duration_seconds": 4.976,
      "amplitude": 0.345
    },
    {
      "t": 73.322,
      "voice": "v1",
      "pitch_index": 4,
      "duration_seconds": 3.827,
      "amplitude": 0.388
    },
    {
      "t": 73.596,
      "voice": "v2",
      "pitch_index": 2,
      "duration_seconds": 4.007,
      "amplitude": 0.401
    },
    {
      "t": 73.286,
      "voice": "v3",
      "pitch_index": 4,
      "duration_seconds": 3.82,
      "amplitude": 0.34
    },
    {
      "t": 73.321,
      "voice": "v4",
      "pitch_index": 2,
      "duration_seconds": 4.029,
      "amplitude": 0.415
    },
    {
      "t": 73.463,
      "voice": "v5",
      "pitch_index": 4,
      "duration_seconds": 4.416,
      "amplitude": 0.427
    },
    {
      "t": 73.493,
      "voice": "v6",
      "pitch_index": 0,
      "duration_seconds": 4.154,
      "amplitude": 0.401
    },
    {
      "t": 73.57,
      "voice": "v7",
      "pitch_index": 0,
      "duration_seconds": 4.262,
      "amplitude": 0.407
    },
    {
      "t": 73.551,
      "voice": "v8",
      "pitch_index": 0,
      "duration_seconds": 4.341,
      "amplitude": 0.425
    },
    {
      "t": 80.104,
      "voice": "v1",
      "pitch_index": 4,
      "duration_seconds": 4.935,
      "amplitude": 0.382
    },
    {
      "t": 80.067,
      "voice": "v2",
      "pitch_index": 0,
      "duration_seconds": 5.446,
      "amplitude": 0.42
    },
    {
      "t": 80.23,
      "voice": "v3",
      "pitch_index": 2,
      "duration_seconds": 5.064,
      "amplitude": 0.416
    },
    {
      "t": 80.255,
      "voice": "v4",
      "pitch_index": 2,
      "duration_seconds": 5.226,
      "amplitude": 0.413
    },
    {
      "t": 80.076,
      "voice": "v5",
      "pitch_index": 4,
      "duration_seconds": 5.413,
      "amplitude": 0.427
    },
    {
      "t": 80.287,
      "voice": "v6",
      "pitch_index": 0,
      "duration_seconds": 5.126,
      "amplitude": 0.419
    },
    {
      "t": 80.272,
      "voice": "v7",
      "pitch_index": 0,
      "duration_seconds": 5.521,
      "amplitude": 0.415
    },
    {
      "t": 80.107,
      "voice": "v8",
      "pitch_index": 2,
      "duration_seconds": 5.088,
      "amplitude": 0.421
    }
  ]
}
```

### 10. Field note
The piece does not end; it stops. There is no cadence because there was no tension.
