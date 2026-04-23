# Expedition 025

### 1. System name
Ring Weave

### 2. Pitch organization
Inharmonic spiral tuning — stacked near-fifths (1.49 ± 0.03), 12 pitches reduced into a single register. The scale never closes. Reference 145 Hz.

### 3. Rhythmic organization
Additive 3+2+3+2+2 (12-unit bar) at 175 ms unit — bar ≈ 2.1 s. The cycle is the fundamental unit of the piece; everything is one or more cycles. Rhythmic density is moderate (0.69) — enough to feel a groove, not enough to feel driven.

### 4. Formal structure
Cyclical return in six sections. The pot-pattern establishes the cycle alone; a percussion bed (shakers + marimba) enters; three heterophonic voices trace a melody; contrast section reduces texture; a transposed-melody return follows with full ensemble; pot alone fades.

### 5. Texture and voicing
Layered ostinato, heterophonic group. The percussion bed (clay pot, two shakers, wood marimba) cycles through the 12-unit bar. Three melodic voices — strummed harp, blown bottle, bowed crotales — each realize the same melodic line with small timing offsets and occasional pitch substitutions, producing a slowly-shifting melodic cloud.

### 6. Ornament and inflection
Decorative-optional. Heterophonic variation + ghost hits in the percussion (20% probability on selected beats).

### 7. Performance context
Community gathering. The pot-player establishes the cycle; shakers and marimba join; melodic voices enter last. Listeners circle.

### 8. Relationship to neighboring systems
Shares with **Ewe agbekor** the bell-grounded layered percussion logic and the heterophonic community texture. Shares with **Arabic maqam** the near-fifth-stacked pitch system. Shares with **Turkish classical makam** the spiral-non-closing scale logic. Unique: *low-energy cyclic-return layered ostinato in inharmonic spiral tuning with a three-voice heterophonic melodic cloud*.

### 9. Audio specification

```json
{
  "duration_seconds": 71.9,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 145,
    "pitches": [
      1.0,
      1.4917,
      2.0567,
      2.267,
      2.2809,
      2.4833,
      2.5552,
      2.779,
      3.0907,
      3.3756,
      3.4454,
      3.7512
    ],
    "octave_repeats": false
  },
  "rhythm_system": {
    "type": "additive",
    "groupings": [
      3,
      2,
      3,
      2,
      2
    ],
    "base_unit_ms": 175
  },
  "voices": [
    {
      "name": "pot",
      "timbre": "clay_pot",
      "pitch_indices": [
        0,
        2
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.55,
      "spatial_position": [
        0.0,
        -0.15
      ]
    },
    {
      "name": "shaker_L",
      "timbre": "shaker",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.3,
      "spatial_position": [
        -0.7,
        -0.05
      ]
    },
    {
      "name": "shaker_R",
      "timbre": "shaker",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.28,
      "spatial_position": [
        0.7,
        -0.05
      ]
    },
    {
      "name": "marimba_bed",
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
      "rhythm_role": "ostinato",
      "amplitude": 0.4,
      "spatial_position": [
        -0.35,
        0.15
      ]
    },
    {
      "name": "harp",
      "timbre": "strummed_harp",
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
      "amplitude": 0.5,
      "spatial_position": [
        0.35,
        0.25
      ]
    },
    {
      "name": "bottle",
      "timbre": "blown_bottle",
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
      "amplitude": 0.48,
      "spatial_position": [
        -0.15,
        0.3
      ]
    },
    {
      "name": "crotales",
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
        11
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.48,
      "spatial_position": [
        0.55,
        0.2
      ]
    }
  ],
  "form": {
    "arc_type": "cyclical",
    "sections": [
      {
        "name": "pot_alone",
        "start_seconds": 0,
        "duration_seconds": 9,
        "character": "pot establishes the 12-unit cycle",
        "chord_tones": [
          0,
          2,
          4
        ]
      },
      {
        "name": "bed_enters",
        "start_seconds": 9,
        "duration_seconds": 13,
        "character": "shakers + marimba bed enter",
        "chord_tones": [
          0,
          2,
          4,
          5
        ]
      },
      {
        "name": "heterophonic_melody",
        "start_seconds": 22,
        "duration_seconds": 14.9,
        "character": "three heterophonic voices trace melody",
        "chord_tones": [
          0,
          2,
          4,
          5,
          7
        ]
      },
      {
        "name": "contrast",
        "start_seconds": 45.4,
        "duration_seconds": 8,
        "character": "melody alone, percussion thins",
        "chord_tones": [
          0,
          3,
          5
        ]
      },
      {
        "name": "full_return",
        "start_seconds": 54.6,
        "duration_seconds": 20,
        "character": "full ensemble, transposed melody",
        "chord_tones": [
          2,
          4,
          5,
          7
        ]
      },
      {
        "name": "pot_fade",
        "start_seconds": 61.9,
        "duration_seconds": 10,
        "character": "pot alone, fading",
        "chord_tones": [
          0
        ]
      }
    ]
  },
  "ornamentation": {
    "density": 0.35,
    "rule": "Decorative: heterophonic voices may add \u00b11-step passing tones and small timing offsets. Percussion uses occasional ghost hits (20% probability)."
  },
  "auto_pedal": false,
  "mix": {
    "reverb_wet": 0.28,
    "reverb_length": 2.0,
    "reverb_decay": 3.5,
    "hpf_hz": 45,
    "lpf_hz": 8500,
    "hf_shelf_gain_db": 0.5,
    "hf_shelf_freq": 4200
  },
  "events": [
    {
      "t": 0.5,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 1.025,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 1.375,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 1.9,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 2.25,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 2.6,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 3.125,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 3.475,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 4.0,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 4.35,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 4.7,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 5.225,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 5.575,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 6.1,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 6.45,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 6.8,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 7.325,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 7.675,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 8.2,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 8.55,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 8.9,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 9.425,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 9.775,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 10.3,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 10.65,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 8.9,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 9.25,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 9.6,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 9.95,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 10.3,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 10.65,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 9.075,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 9.425,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 9.775,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 10.125,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 10.475,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 10.825,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 8.9,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 9.25,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 9.6,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 9.775,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 10.125,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 10.475,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 11.0,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 11.525,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 11.875,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 12.4,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 12.75,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 11.0,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 11.35,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 11.7,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 12.05,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 12.4,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 12.75,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 11.175,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 11.525,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 11.875,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 12.225,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 12.575,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 12.925,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 11.0,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 11.35,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 11.7,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 11.875,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 12.225,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 12.575,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 13.1,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 13.625,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 13.975,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 14.5,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 14.85,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 13.1,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 13.45,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 13.8,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 14.15,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 14.5,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 14.85,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 13.275,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 13.625,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 13.975,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 14.325,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 14.675,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 15.025,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 13.1,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 13.45,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 13.8,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 13.975,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 14.325,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 14.675,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 15.2,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 15.725,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 16.075,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 16.6,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 16.95,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 15.2,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 15.55,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 15.9,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 16.25,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 16.6,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 16.95,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 15.375,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 15.725,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 16.075,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 16.425,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 16.775,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 17.125,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 15.2,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 15.55,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 15.9,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 16.075,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 16.425,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 16.775,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 17.3,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 17.825,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 18.175,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 18.7,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 19.05,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 17.3,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 17.65,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 18.0,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 18.35,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 18.7,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 19.05,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 17.475,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 17.825,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 18.175,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 18.525,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 18.875,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 19.225,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 17.3,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 17.65,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 18.0,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 18.175,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 18.525,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 18.875,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 19.4,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 19.925,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 20.275,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 20.8,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 21.15,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 19.4,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 19.75,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 20.1,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 20.45,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 20.8,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 21.15,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 19.575,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 19.925,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 20.275,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 20.625,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 20.975,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 21.325,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 19.4,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 19.75,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 20.1,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 20.275,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 20.625,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 20.975,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 21.651,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.539,
      "amplitude": 0.469
    },
    {
      "t": 22.195,
      "voice": "harp",
      "pitch_index": 6,
      "duration_seconds": 0.476,
      "amplitude": 0.536
    },
    {
      "t": 22.707,
      "voice": "harp",
      "pitch_index": 5,
      "duration_seconds": 0.506,
      "amplitude": 0.503
    },
    {
      "t": 23.213,
      "voice": "harp",
      "pitch_index": 7,
      "duration_seconds": 0.807,
      "amplitude": 0.496
    },
    {
      "t": 24.023,
      "voice": "harp",
      "pitch_index": 6,
      "duration_seconds": 0.537,
      "amplitude": 0.466
    },
    {
      "t": 24.541,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.721,
      "amplitude": 0.538
    },
    {
      "t": 25.339,
      "voice": "harp",
      "pitch_index": 6,
      "duration_seconds": 0.505,
      "amplitude": 0.467
    },
    {
      "t": 25.846,
      "voice": "harp",
      "pitch_index": 3,
      "duration_seconds": 0.478,
      "amplitude": 0.501
    },
    {
      "t": 26.372,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.541,
      "amplitude": 0.454
    },
    {
      "t": 26.88,
      "voice": "harp",
      "pitch_index": 2,
      "duration_seconds": 0.735,
      "amplitude": 0.488
    },
    {
      "t": 27.672,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.511,
      "amplitude": 0.495
    },
    {
      "t": 28.196,
      "voice": "harp",
      "pitch_index": 1,
      "duration_seconds": 0.742,
      "amplitude": 0.454
    },
    {
      "t": 28.977,
      "voice": "harp",
      "pitch_index": 2,
      "duration_seconds": 0.522,
      "amplitude": 0.491
    },
    {
      "t": 29.5,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.521,
      "amplitude": 0.482
    },
    {
      "t": 30.003,
      "voice": "harp",
      "pitch_index": 5,
      "duration_seconds": 0.72,
      "amplitude": 0.512
    },
    {
      "t": 30.82,
      "voice": "harp",
      "pitch_index": 7,
      "duration_seconds": 0.735,
      "amplitude": 0.463
    },
    {
      "t": 31.643,
      "voice": "harp",
      "pitch_index": 5,
      "duration_seconds": 0.486,
      "amplitude": 0.501
    },
    {
      "t": 32.174,
      "voice": "harp",
      "pitch_index": 3,
      "duration_seconds": 0.508,
      "amplitude": 0.477
    },
    {
      "t": 32.699,
      "voice": "harp",
      "pitch_index": 2,
      "duration_seconds": 0.526,
      "amplitude": 0.49
    },
    {
      "t": 33.216,
      "voice": "harp",
      "pitch_index": 0,
      "duration_seconds": 0.722,
      "amplitude": 0.518
    },
    {
      "t": 33.997,
      "voice": "harp",
      "pitch_index": 2,
      "duration_seconds": 0.528,
      "amplitude": 0.501
    },
    {
      "t": 34.528,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.711,
      "amplitude": 0.517
    },
    {
      "t": 35.297,
      "voice": "harp",
      "pitch_index": 3,
      "duration_seconds": 0.519,
      "amplitude": 0.453
    },
    {
      "t": 35.823,
      "voice": "harp",
      "pitch_index": 0,
      "duration_seconds": 1.081,
      "amplitude": 0.474
    },
    {
      "t": 21.745,
      "voice": "bottle",
      "pitch_index": 5,
      "duration_seconds": 0.525,
      "amplitude": 0.504
    },
    {
      "t": 22.278,
      "voice": "bottle",
      "pitch_index": 6,
      "duration_seconds": 0.482,
      "amplitude": 0.537
    },
    {
      "t": 22.828,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.549,
      "amplitude": 0.514
    },
    {
      "t": 23.36,
      "voice": "bottle",
      "pitch_index": 7,
      "duration_seconds": 0.717,
      "amplitude": 0.505
    },
    {
      "t": 24.109,
      "voice": "bottle",
      "pitch_index": 6,
      "duration_seconds": 0.512,
      "amplitude": 0.471
    },
    {
      "t": 24.612,
      "voice": "bottle",
      "pitch_index": 3,
      "duration_seconds": 0.743,
      "amplitude": 0.491
    },
    {
      "t": 25.383,
      "voice": "bottle",
      "pitch_index": 5,
      "duration_seconds": 0.495,
      "amplitude": 0.475
    },
    {
      "t": 25.927,
      "voice": "bottle",
      "pitch_index": 3,
      "duration_seconds": 0.507,
      "amplitude": 0.496
    },
    {
      "t": 26.426,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.531,
      "amplitude": 0.538
    },
    {
      "t": 26.942,
      "voice": "bottle",
      "pitch_index": 2,
      "duration_seconds": 0.715,
      "amplitude": 0.494
    },
    {
      "t": 27.719,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.496,
      "amplitude": 0.478
    },
    {
      "t": 28.265,
      "voice": "bottle",
      "pitch_index": 0,
      "duration_seconds": 0.751,
      "amplitude": 0.456
    },
    {
      "t": 29.018,
      "voice": "bottle",
      "pitch_index": 1,
      "duration_seconds": 0.538,
      "amplitude": 0.485
    },
    {
      "t": 29.517,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.483,
      "amplitude": 0.457
    },
    {
      "t": 30.061,
      "voice": "bottle",
      "pitch_index": 5,
      "duration_seconds": 0.743,
      "amplitude": 0.499
    },
    {
      "t": 30.876,
      "voice": "bottle",
      "pitch_index": 7,
      "duration_seconds": 0.718,
      "amplitude": 0.484
    },
    {
      "t": 31.702,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.482,
      "amplitude": 0.511
    },
    {
      "t": 32.25,
      "voice": "bottle",
      "pitch_index": 3,
      "duration_seconds": 0.536,
      "amplitude": 0.522
    },
    {
      "t": 32.791,
      "voice": "bottle",
      "pitch_index": 2,
      "duration_seconds": 0.478,
      "amplitude": 0.536
    },
    {
      "t": 33.33,
      "voice": "bottle",
      "pitch_index": 0,
      "duration_seconds": 0.814,
      "amplitude": 0.517
    },
    {
      "t": 34.136,
      "voice": "bottle",
      "pitch_index": 2,
      "duration_seconds": 0.527,
      "amplitude": 0.5
    },
    {
      "t": 34.638,
      "voice": "bottle",
      "pitch_index": 3,
      "duration_seconds": 0.729,
      "amplitude": 0.495
    },
    {
      "t": 35.394,
      "voice": "bottle",
      "pitch_index": 2,
      "duration_seconds": 0.521,
      "amplitude": 0.533
    },
    {
      "t": 35.904,
      "voice": "bottle",
      "pitch_index": 0,
      "duration_seconds": 1.069,
      "amplitude": 0.462
    },
    {
      "t": 21.691,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.551,
      "amplitude": 0.456
    },
    {
      "t": 22.236,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.483,
      "amplitude": 0.471
    },
    {
      "t": 22.782,
      "voice": "crotales",
      "pitch_index": 5,
      "duration_seconds": 0.506,
      "amplitude": 0.454
    },
    {
      "t": 23.307,
      "voice": "crotales",
      "pitch_index": 7,
      "duration_seconds": 0.796,
      "amplitude": 0.481
    },
    {
      "t": 24.088,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.542,
      "amplitude": 0.49
    },
    {
      "t": 24.59,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.749,
      "amplitude": 0.493
    },
    {
      "t": 25.342,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.482,
      "amplitude": 0.485
    },
    {
      "t": 25.882,
      "voice": "crotales",
      "pitch_index": 3,
      "duration_seconds": 0.543,
      "amplitude": 0.521
    },
    {
      "t": 26.431,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.506,
      "amplitude": 0.54
    },
    {
      "t": 26.975,
      "voice": "crotales",
      "pitch_index": 3,
      "duration_seconds": 0.767,
      "amplitude": 0.472
    },
    {
      "t": 27.767,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.542,
      "amplitude": 0.488
    },
    {
      "t": 28.27,
      "voice": "crotales",
      "pitch_index": 0,
      "duration_seconds": 0.715,
      "amplitude": 0.519
    },
    {
      "t": 29.026,
      "voice": "crotales",
      "pitch_index": 2,
      "duration_seconds": 0.519,
      "amplitude": 0.458
    },
    {
      "t": 29.558,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.546,
      "amplitude": 0.534
    },
    {
      "t": 30.108,
      "voice": "crotales",
      "pitch_index": 5,
      "duration_seconds": 0.766,
      "amplitude": 0.489
    },
    {
      "t": 30.867,
      "voice": "crotales",
      "pitch_index": 7,
      "duration_seconds": 0.827,
      "amplitude": 0.495
    },
    {
      "t": 31.682,
      "voice": "crotales",
      "pitch_index": 5,
      "duration_seconds": 0.502,
      "amplitude": 0.488
    },
    {
      "t": 32.232,
      "voice": "crotales",
      "pitch_index": 3,
      "duration_seconds": 0.532,
      "amplitude": 0.463
    },
    {
      "t": 32.771,
      "voice": "crotales",
      "pitch_index": 2,
      "duration_seconds": 0.551,
      "amplitude": 0.451
    },
    {
      "t": 33.283,
      "voice": "crotales",
      "pitch_index": 0,
      "duration_seconds": 0.761,
      "amplitude": 0.475
    },
    {
      "t": 34.1,
      "voice": "crotales",
      "pitch_index": 2,
      "duration_seconds": 0.542,
      "amplitude": 0.499
    },
    {
      "t": 34.602,
      "voice": "crotales",
      "pitch_index": 3,
      "duration_seconds": 0.729,
      "amplitude": 0.539
    },
    {
      "t": 35.416,
      "voice": "crotales",
      "pitch_index": 2,
      "duration_seconds": 0.533,
      "amplitude": 0.498
    },
    {
      "t": 35.916,
      "voice": "crotales",
      "pitch_index": 0,
      "duration_seconds": 0.999,
      "amplitude": 0.531
    },
    {
      "t": 21.5,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 22.025,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 22.375,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 22.9,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 23.25,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 21.5,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 21.85,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 22.2,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 22.55,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 22.9,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 23.25,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 21.675,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 22.025,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 22.375,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 22.725,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 23.075,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 23.425,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 21.5,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 21.85,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 22.2,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 22.375,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 22.725,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 23.075,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 23.6,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 24.125,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 24.475,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 25.0,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 25.35,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 23.6,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 23.95,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 24.3,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 24.65,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 25.0,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 25.35,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 23.775,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 24.125,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 24.475,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 24.825,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 25.175,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 25.525,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 23.6,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 23.95,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 24.3,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 24.475,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 24.825,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 25.175,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 25.7,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 26.225,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 26.575,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 27.1,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 27.45,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 25.7,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 26.05,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 26.4,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 26.75,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 27.1,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 27.45,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 25.875,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 26.225,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 26.575,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 26.925,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 27.275,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 27.625,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 25.7,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 26.05,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 26.4,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 26.575,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 26.925,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 27.275,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 27.8,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 28.325,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 28.675,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 29.2,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 29.55,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 27.8,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 28.15,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 28.5,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 28.85,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 29.2,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 29.55,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 27.975,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 28.325,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 28.675,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 29.025,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 29.375,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 29.725,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 27.8,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 28.15,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 28.5,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 28.675,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 29.025,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 29.375,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 29.9,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 30.425,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 30.775,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 31.3,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 31.65,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 29.9,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 30.25,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 30.6,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 30.95,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 31.3,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 31.65,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 30.075,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 30.425,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 30.775,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 31.125,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 31.475,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 31.825,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 29.9,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 30.25,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 30.6,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 30.775,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 31.125,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 31.475,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 32.0,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 32.525,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 32.875,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 33.4,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 33.75,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 32.0,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 32.35,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 32.7,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 33.05,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 33.4,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 33.75,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 32.175,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 32.525,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 32.875,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 33.225,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 33.575,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 33.925,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 32.0,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 32.35,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 32.7,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 32.875,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 33.225,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 33.575,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 34.1,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 34.625,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 34.975,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 35.5,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 35.85,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.55
    },
    {
      "t": 34.1,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 34.45,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 34.8,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 35.15,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 35.5,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 35.85,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 34.275,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 34.625,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 34.975,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 35.325,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 35.675,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 36.025,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.26
    },
    {
      "t": 34.1,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 34.45,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 34.8,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 34.975,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 35.325,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 35.675,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.38
    },
    {
      "t": 36.943,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.4
    },
    {
      "t": 37.993,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.4
    },
    {
      "t": 36.943,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 37.643,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 38.343,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 39.043,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.4
    },
    {
      "t": 40.093,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.4
    },
    {
      "t": 39.043,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 39.743,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 40.443,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 41.143,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.4
    },
    {
      "t": 42.193,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.4
    },
    {
      "t": 41.143,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 41.843,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 42.543,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 43.243,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.4
    },
    {
      "t": 44.293,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.4
    },
    {
      "t": 43.243,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 43.943,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 44.643,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.22
    },
    {
      "t": 37.443,
      "voice": "crotales",
      "pitch_index": 3,
      "duration_seconds": 0.748,
      "amplitude": 0.5
    },
    {
      "t": 38.23,
      "voice": "crotales",
      "pitch_index": 5,
      "duration_seconds": 0.499,
      "amplitude": 0.5
    },
    {
      "t": 38.755,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.748,
      "amplitude": 0.5
    },
    {
      "t": 39.543,
      "voice": "crotales",
      "pitch_index": 2,
      "duration_seconds": 0.748,
      "amplitude": 0.5
    },
    {
      "t": 40.33,
      "voice": "crotales",
      "pitch_index": 0,
      "duration_seconds": 0.997,
      "amplitude": 0.5
    },
    {
      "t": 45.691,
      "voice": "harp",
      "pitch_index": 6,
      "duration_seconds": 0.45,
      "amplitude": 0.54
    },
    {
      "t": 46.183,
      "voice": "harp",
      "pitch_index": 8,
      "duration_seconds": 0.467,
      "amplitude": 0.593
    },
    {
      "t": 46.688,
      "voice": "harp",
      "pitch_index": 8,
      "duration_seconds": 0.486,
      "amplitude": 0.588
    },
    {
      "t": 47.165,
      "voice": "harp",
      "pitch_index": 9,
      "duration_seconds": 0.74,
      "amplitude": 0.535
    },
    {
      "t": 47.889,
      "voice": "harp",
      "pitch_index": 8,
      "duration_seconds": 0.513,
      "amplitude": 0.563
    },
    {
      "t": 48.386,
      "voice": "harp",
      "pitch_index": 6,
      "duration_seconds": 0.754,
      "amplitude": 0.553
    },
    {
      "t": 49.137,
      "voice": "harp",
      "pitch_index": 8,
      "duration_seconds": 0.512,
      "amplitude": 0.552
    },
    {
      "t": 49.63,
      "voice": "harp",
      "pitch_index": 5,
      "duration_seconds": 0.483,
      "amplitude": 0.583
    },
    {
      "t": 50.123,
      "voice": "harp",
      "pitch_index": 6,
      "duration_seconds": 0.508,
      "amplitude": 0.586
    },
    {
      "t": 50.617,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.722,
      "amplitude": 0.541
    },
    {
      "t": 51.343,
      "voice": "harp",
      "pitch_index": 6,
      "duration_seconds": 0.462,
      "amplitude": 0.517
    },
    {
      "t": 51.854,
      "voice": "harp",
      "pitch_index": 2,
      "duration_seconds": 0.758,
      "amplitude": 0.542
    },
    {
      "t": 52.626,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.466,
      "amplitude": 0.537
    },
    {
      "t": 53.104,
      "voice": "harp",
      "pitch_index": 6,
      "duration_seconds": 0.462,
      "amplitude": 0.523
    },
    {
      "t": 53.589,
      "voice": "harp",
      "pitch_index": 8,
      "duration_seconds": 0.68,
      "amplitude": 0.521
    },
    {
      "t": 54.358,
      "voice": "harp",
      "pitch_index": 9,
      "duration_seconds": 0.705,
      "amplitude": 0.515
    },
    {
      "t": 55.081,
      "voice": "harp",
      "pitch_index": 7,
      "duration_seconds": 0.442,
      "amplitude": 0.503
    },
    {
      "t": 55.589,
      "voice": "harp",
      "pitch_index": 5,
      "duration_seconds": 0.498,
      "amplitude": 0.556
    },
    {
      "t": 56.088,
      "voice": "harp",
      "pitch_index": 3,
      "duration_seconds": 0.476,
      "amplitude": 0.578
    },
    {
      "t": 56.571,
      "voice": "harp",
      "pitch_index": 2,
      "duration_seconds": 0.747,
      "amplitude": 0.513
    },
    {
      "t": 57.336,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.453,
      "amplitude": 0.591
    },
    {
      "t": 57.813,
      "voice": "harp",
      "pitch_index": 6,
      "duration_seconds": 0.765,
      "amplitude": 0.516
    },
    {
      "t": 58.56,
      "voice": "harp",
      "pitch_index": 4,
      "duration_seconds": 0.447,
      "amplitude": 0.506
    },
    {
      "t": 59.073,
      "voice": "harp",
      "pitch_index": 2,
      "duration_seconds": 0.98,
      "amplitude": 0.558
    },
    {
      "t": 45.797,
      "voice": "bottle",
      "pitch_index": 7,
      "duration_seconds": 0.503,
      "amplitude": 0.54
    },
    {
      "t": 46.274,
      "voice": "bottle",
      "pitch_index": 8,
      "duration_seconds": 0.443,
      "amplitude": 0.564
    },
    {
      "t": 46.742,
      "voice": "bottle",
      "pitch_index": 7,
      "duration_seconds": 0.448,
      "amplitude": 0.584
    },
    {
      "t": 47.212,
      "voice": "bottle",
      "pitch_index": 9,
      "duration_seconds": 0.734,
      "amplitude": 0.547
    },
    {
      "t": 47.948,
      "voice": "bottle",
      "pitch_index": 8,
      "duration_seconds": 0.452,
      "amplitude": 0.556
    },
    {
      "t": 48.425,
      "voice": "bottle",
      "pitch_index": 6,
      "duration_seconds": 0.687,
      "amplitude": 0.59
    },
    {
      "t": 49.133,
      "voice": "bottle",
      "pitch_index": 6,
      "duration_seconds": 0.488,
      "amplitude": 0.502
    },
    {
      "t": 49.622,
      "voice": "bottle",
      "pitch_index": 5,
      "duration_seconds": 0.449,
      "amplitude": 0.593
    },
    {
      "t": 50.136,
      "voice": "bottle",
      "pitch_index": 6,
      "duration_seconds": 0.484,
      "amplitude": 0.55
    },
    {
      "t": 50.605,
      "voice": "bottle",
      "pitch_index": 5,
      "duration_seconds": 0.747,
      "amplitude": 0.591
    },
    {
      "t": 51.376,
      "voice": "bottle",
      "pitch_index": 5,
      "duration_seconds": 0.482,
      "amplitude": 0.515
    },
    {
      "t": 51.858,
      "voice": "bottle",
      "pitch_index": 2,
      "duration_seconds": 0.683,
      "amplitude": 0.543
    },
    {
      "t": 52.623,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.453,
      "amplitude": 0.52
    },
    {
      "t": 53.106,
      "voice": "bottle",
      "pitch_index": 6,
      "duration_seconds": 0.443,
      "amplitude": 0.504
    },
    {
      "t": 53.613,
      "voice": "bottle",
      "pitch_index": 7,
      "duration_seconds": 0.682,
      "amplitude": 0.549
    },
    {
      "t": 54.314,
      "voice": "bottle",
      "pitch_index": 9,
      "duration_seconds": 0.76,
      "amplitude": 0.501
    },
    {
      "t": 55.051,
      "voice": "bottle",
      "pitch_index": 7,
      "duration_seconds": 0.464,
      "amplitude": 0.524
    },
    {
      "t": 55.56,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.513,
      "amplitude": 0.519
    },
    {
      "t": 56.069,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.461,
      "amplitude": 0.586
    },
    {
      "t": 56.542,
      "voice": "bottle",
      "pitch_index": 2,
      "duration_seconds": 0.762,
      "amplitude": 0.563
    },
    {
      "t": 57.272,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.5,
      "amplitude": 0.525
    },
    {
      "t": 57.775,
      "voice": "bottle",
      "pitch_index": 6,
      "duration_seconds": 0.702,
      "amplitude": 0.529
    },
    {
      "t": 58.518,
      "voice": "bottle",
      "pitch_index": 4,
      "duration_seconds": 0.493,
      "amplitude": 0.508
    },
    {
      "t": 59.016,
      "voice": "bottle",
      "pitch_index": 2,
      "duration_seconds": 0.92,
      "amplitude": 0.532
    },
    {
      "t": 45.448,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.488,
      "amplitude": 0.526
    },
    {
      "t": 45.93,
      "voice": "crotales",
      "pitch_index": 8,
      "duration_seconds": 0.505,
      "amplitude": 0.55
    },
    {
      "t": 46.434,
      "voice": "crotales",
      "pitch_index": 7,
      "duration_seconds": 0.443,
      "amplitude": 0.52
    },
    {
      "t": 46.923,
      "voice": "crotales",
      "pitch_index": 9,
      "duration_seconds": 0.699,
      "amplitude": 0.532
    },
    {
      "t": 47.627,
      "voice": "crotales",
      "pitch_index": 8,
      "duration_seconds": 0.479,
      "amplitude": 0.592
    },
    {
      "t": 48.101,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.695,
      "amplitude": 0.545
    },
    {
      "t": 48.852,
      "voice": "crotales",
      "pitch_index": 7,
      "duration_seconds": 0.461,
      "amplitude": 0.583
    },
    {
      "t": 49.327,
      "voice": "crotales",
      "pitch_index": 5,
      "duration_seconds": 0.461,
      "amplitude": 0.589
    },
    {
      "t": 49.798,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.491,
      "amplitude": 0.556
    },
    {
      "t": 50.306,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.769,
      "amplitude": 0.528
    },
    {
      "t": 51.076,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.496,
      "amplitude": 0.532
    },
    {
      "t": 51.55,
      "voice": "crotales",
      "pitch_index": 2,
      "duration_seconds": 0.696,
      "amplitude": 0.568
    },
    {
      "t": 52.297,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.455,
      "amplitude": 0.512
    },
    {
      "t": 52.811,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.454,
      "amplitude": 0.571
    },
    {
      "t": 53.293,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.719,
      "amplitude": 0.535
    },
    {
      "t": 54.001,
      "voice": "crotales",
      "pitch_index": 10,
      "duration_seconds": 0.685,
      "amplitude": 0.545
    },
    {
      "t": 54.722,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.469,
      "amplitude": 0.532
    },
    {
      "t": 55.234,
      "voice": "crotales",
      "pitch_index": 5,
      "duration_seconds": 0.496,
      "amplitude": 0.495
    },
    {
      "t": 55.725,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.459,
      "amplitude": 0.571
    },
    {
      "t": 56.224,
      "voice": "crotales",
      "pitch_index": 2,
      "duration_seconds": 0.766,
      "amplitude": 0.522
    },
    {
      "t": 56.993,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.504,
      "amplitude": 0.563
    },
    {
      "t": 57.487,
      "voice": "crotales",
      "pitch_index": 6,
      "duration_seconds": 0.679,
      "amplitude": 0.529
    },
    {
      "t": 58.249,
      "voice": "crotales",
      "pitch_index": 4,
      "duration_seconds": 0.451,
      "amplitude": 0.553
    },
    {
      "t": 58.74,
      "voice": "crotales",
      "pitch_index": 2,
      "duration_seconds": 1.013,
      "amplitude": 0.582
    },
    {
      "t": 45.343,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 45.868,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 46.218,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 46.743,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 47.093,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 45.343,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 45.693,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 46.043,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 46.393,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 46.743,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 47.093,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 45.518,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 45.868,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 46.218,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 46.568,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 46.918,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 47.268,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 45.343,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 45.693,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 46.043,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 46.218,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 46.568,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 46.918,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 47.443,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.232
    },
    {
      "t": 47.968,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 48.318,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 48.843,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 49.193,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.232
    },
    {
      "t": 47.443,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 47.793,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 48.143,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 48.493,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 48.843,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 49.193,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 47.618,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 47.968,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 48.318,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 48.668,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 49.018,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 49.368,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 47.443,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 47.793,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 48.143,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 48.318,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 48.668,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 49.018,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 49.543,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 50.068,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 50.418,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 50.943,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.232
    },
    {
      "t": 51.293,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 49.543,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 49.893,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 50.243,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 50.593,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 50.943,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 51.293,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 49.718,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 50.068,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 50.418,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 50.768,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 51.118,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 51.468,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 49.543,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 49.893,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 50.243,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 50.418,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 50.768,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 51.118,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 51.643,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 52.168,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 52.518,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 53.043,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 53.393,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.232
    },
    {
      "t": 51.643,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 51.993,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 52.343,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 52.693,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 53.043,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 53.393,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 51.818,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 52.168,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 52.518,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 52.868,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 53.218,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 53.568,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 51.643,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 51.993,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 52.343,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 52.518,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 52.868,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 53.218,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 53.743,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 54.268,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.232
    },
    {
      "t": 54.618,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 55.143,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 55.493,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 53.743,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 54.093,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 54.443,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 54.793,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 55.143,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 55.493,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 53.918,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 54.268,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 54.618,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 54.968,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 55.318,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 55.668,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 53.743,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 54.093,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 54.443,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 54.618,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 54.968,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 55.318,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 55.843,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.232
    },
    {
      "t": 56.368,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 56.718,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 57.243,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 57.593,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 55.843,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 56.193,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 56.543,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 56.893,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 57.243,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 57.593,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 56.018,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 56.368,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 56.718,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 57.068,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 57.418,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 57.768,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 55.843,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 56.193,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 56.543,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 56.718,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 57.068,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 57.418,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 57.943,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 58.468,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 58.818,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 59.343,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 59.693,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.35,
      "amplitude": 0.58
    },
    {
      "t": 57.943,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 58.293,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 58.643,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 58.993,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 59.343,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 59.693,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.3
    },
    {
      "t": 58.118,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 58.468,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 58.818,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 59.168,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 59.518,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 59.868,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.28
    },
    {
      "t": 57.943,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 58.293,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 58.643,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 58.818,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 59.168,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 59.518,
      "voice": "marimba_bed",
      "pitch_index": 2,
      "duration_seconds": 0.18,
      "amplitude": 0.4
    },
    {
      "t": 60.053,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.4,
      "amplitude": 0.42
    },
    {
      "t": 60.928,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.4,
      "amplitude": 0.42
    },
    {
      "t": 61.803,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.4,
      "amplitude": 0.42
    },
    {
      "t": 62.153,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.4,
      "amplitude": 0.42
    },
    {
      "t": 63.028,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.4,
      "amplitude": 0.42
    },
    {
      "t": 63.903,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.4,
      "amplitude": 0.42
    },
    {
      "t": 64.253,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.4,
      "amplitude": 0.42
    },
    {
      "t": 65.128,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.4,
      "amplitude": 0.42
    },
    {
      "t": 66.003,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.4,
      "amplitude": 0.42
    },
    {
      "t": 66.653,
      "voice": "crotales",
      "pitch_index": 0,
      "duration_seconds": 4.5,
      "amplitude": 0.42
    }
  ]
}
```

### 10. Field note
The pot is the same every bar. Everything else rhymes with it.
