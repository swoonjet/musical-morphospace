# Expedition 027

### 1. System name
Spectral Machine

### 2. Pitch organization
Indeterminate tuning, octave-repeating. An 8-tone scale per octave derived from 2^(k/8) with small sinusoidal perturbations (±1%), producing *nearly* 8-EDO but with tuning that subtly reads as "off-grid". Two octaves (17 pitches). The perturbations are fixed — not performer-chosen — so the tuning is reproducibly peculiar.

### 3. Rhythmic organization
Additive 4+4+4+4 at 85 ms — 16-unit bar = 1.36 s (~176 BPM feel). Rhythmic density very high (0.82), tempo stability very high (0.86). The piece is a machine — rigid meter, layered ostinato, no rubato.

### 4. Formal structure
Sectional contrasting, cyclical return arc. Six sections of abrupt change:
- **intro** — drums ramp up
- **groove_A** — sparse groove with bass riff and stereo-doubled rhodes hook
- **contrast_B** — driving, marimba counter-melody, reed chord stabs
- **breakdown** — drums strip, bass continues, reed pad sustains
- **burn** — double-time kick, maximum density, all voices at once
- **stab** — final hit

### 5. Texture and voicing
Layered ostinato, heterophonic group. Twelve voices:
- Drum layer (7): kick, snare, hat closed/open, clap, shaker L/R
- Bass: distorted sawtooth
- Rhodes: stereo-doubled on hard L/R with 12 ms delay
- Marimba: counter-melody
- Reed: chord stabs and pad

### 6. Ornament and inflection
Rhythmic-only — hi-hat ghost notes (20-35% probability, higher in burn section), syncopated clap on 3/11, marimba layered counter-melody against the main hook.

### 7. Performance context
Dance / ceremonial. The piece is *for* movement.

### 8. Relationship to neighboring systems
Shares with **Arabic maqam** and **Turkish classical makam** the tuning indeterminacy — pitches that are not quite 12-TET. Shares with **Peking opera** the abrupt sectional contrasts and the percussion-accent logic. The neighborhood is otherwise empty — most "near-12-TET" traditions are Western, and Western high-energy layered-ostinato is not sectional-contrasting. Unique: *high-energy layered-ostinato groove in near-8-TET tuning with abrupt sectional contrast, driven by a full rhythm section and stereo-doubled melodic hook*.

### 9. Audio specification

```json
{
  "duration_seconds": 32.7,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 140,
    "pitches": [
      1.0,
      1.1013,
      1.1862,
      1.2848,
      1.4212,
      1.5545,
      1.67,
      1.8227,
      2.0,
      2.0,
      2.2026,
      2.3724,
      2.5696,
      2.8424,
      3.109,
      3.34,
      3.6454
    ],
    "octave_repeats": true
  },
  "rhythm_system": {
    "type": "additive",
    "groupings": [
      4,
      4,
      4,
      4
    ],
    "base_unit_ms": 85
  },
  "voices": [
    {
      "name": "kick",
      "timbre": "kick_synth",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.85,
      "spatial_position": [
        0.0,
        -0.2
      ]
    },
    {
      "name": "snare",
      "timbre": "snare_synth",
      "pitch_indices": [
        2
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.75,
      "spatial_position": [
        -0.1,
        0.15
      ]
    },
    {
      "name": "hat_c",
      "timbre": "hat_closed",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.45,
      "spatial_position": [
        0.5,
        0.2
      ]
    },
    {
      "name": "hat_o",
      "timbre": "hat_open",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.55,
      "spatial_position": [
        0.55,
        0.25
      ]
    },
    {
      "name": "clap",
      "timbre": "clap",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.65,
      "spatial_position": [
        -0.5,
        0.1
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
        0.0
      ]
    },
    {
      "name": "shaker_R",
      "timbre": "shaker",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.3,
      "spatial_position": [
        0.7,
        0.0
      ]
    },
    {
      "name": "bass",
      "timbre": "distorted_bass",
      "pitch_indices": [
        0,
        1,
        2,
        3,
        4,
        5,
        6
      ],
      "rhythm_role": "ostinato",
      "amplitude": 0.78,
      "spatial_position": [
        0.0,
        -0.35
      ]
    },
    {
      "name": "rhodes_L",
      "timbre": "rhodes_electric",
      "pitch_indices": [
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.58,
      "spatial_position": [
        -0.4,
        0.2
      ]
    },
    {
      "name": "rhodes_R",
      "timbre": "rhodes_electric",
      "pitch_indices": [
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.5,
      "spatial_position": [
        0.4,
        0.2
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
        11,
        12,
        13,
        14,
        15,
        16
      ],
      "rhythm_role": "ornamental",
      "amplitude": 0.5,
      "spatial_position": [
        0.25,
        0.3
      ]
    },
    {
      "name": "reed",
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
        12,
        13,
        14,
        15,
        16
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.6,
      "spatial_position": [
        -0.25,
        0.35
      ]
    }
  ],
  "form": {
    "arc_type": "cyclical",
    "sections": [
      {
        "name": "intro",
        "start_seconds": 0,
        "duration_seconds": 2.7,
        "character": "drums ramp up",
        "chord_tones": [
          0,
          4
        ]
      },
      {
        "name": "groove_A",
        "start_seconds": 3.0,
        "duration_seconds": 5.4,
        "character": "sparse groove, bass + hook",
        "chord_tones": [
          0,
          2,
          4,
          7
        ]
      },
      {
        "name": "contrast_B",
        "start_seconds": 8.5,
        "duration_seconds": 5.4,
        "character": "driving \u2014 marimba + reed stabs + fuller drums",
        "chord_tones": [
          2,
          4,
          6,
          9
        ]
      },
      {
        "name": "breakdown",
        "start_seconds": 13.9,
        "duration_seconds": 2.7,
        "character": "drums strip back, reed pad sustains",
        "chord_tones": [
          4,
          7,
          11
        ]
      },
      {
        "name": "burn",
        "start_seconds": 16.6,
        "duration_seconds": 5.4,
        "character": "maximum density, double-time kicks",
        "chord_tones": [
          0,
          2,
          4,
          7,
          11
        ]
      },
      {
        "name": "stab",
        "start_seconds": 22.1,
        "duration_seconds": 2.5,
        "character": "final hit",
        "chord_tones": [
          0,
          4,
          7
        ]
      }
    ]
  },
  "ornamentation": {
    "density": 0.55,
    "rule": "Rhythmic-only: hi-hat ghost notes (20-35% probability depending on section), syncopated clap, marimba layered counter-melody."
  },
  "auto_pedal": false,
  "mix": {
    "reverb_wet": 0.1,
    "reverb_length": 0.9,
    "reverb_decay": 6.0,
    "hpf_hz": 35,
    "lpf_hz": 14000,
    "hf_shelf_gain_db": 2.0,
    "hf_shelf_freq": 6000,
    "master_punch": {
      "comp_threshold": 0.45,
      "comp_ratio": 4.5,
      "comp_attack_ms": 2.5,
      "comp_release_ms": 60.0,
      "comp_makeup_db": 3.5,
      "sat_drive": 1.55
    }
  },
  "events": [
    {
      "t": 0.3,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.65
    },
    {
      "t": 0.98,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.65
    },
    {
      "t": 0.3,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 0.47,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 0.64,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 0.81,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 0.98,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 1.15,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 1.32,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 1.49,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 0.3,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 0.47,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 0.64,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 0.81,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 0.98,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 1.15,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 1.32,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 1.49,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 1.66,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.65
    },
    {
      "t": 2.34,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.65
    },
    {
      "t": 1.66,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 1.83,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 2.0,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 2.17,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 2.34,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 2.51,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 2.68,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 2.85,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 1.66,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 1.83,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 2.0,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 2.17,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 2.34,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 2.51,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 2.68,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 2.85,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 3.02,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 3.53,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 3.87,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 3.36,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 4.04,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 3.02,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 3.19,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 3.36,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 3.53,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 3.7,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 3.87,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 4.04,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 4.21,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 4.21,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 3.275,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 3.955,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 3.02,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 3.19,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 3.36,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 3.53,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 3.7,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 3.87,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 4.04,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 4.21,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 3.105,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 3.275,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 3.445,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 3.615,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 3.785,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 3.955,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 4.125,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 4.295,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 4.38,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 4.89,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 5.23,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 4.72,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 5.4,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 4.38,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 4.55,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 4.72,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 4.89,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 5.06,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 5.23,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 5.4,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 5.57,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 5.57,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 4.635,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 5.315,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 4.38,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 4.55,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 4.72,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 4.89,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 5.06,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 5.23,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 5.4,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 5.57,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 4.465,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 4.635,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 4.805,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 4.975,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 5.145,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 5.315,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 5.485,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 5.655,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 5.74,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 6.25,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 6.59,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 6.08,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 6.76,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 5.74,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 5.91,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 6.08,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 6.25,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 6.42,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 6.59,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 6.76,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 6.93,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 6.93,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 5.995,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 6.675,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 5.74,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 5.91,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 6.08,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 6.25,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 6.42,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 6.59,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 6.76,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 6.93,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 5.825,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 5.995,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 6.165,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 6.335,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 6.505,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 6.675,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 6.845,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 7.015,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 7.1,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 7.61,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 7.95,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 7.44,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 8.12,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 7.1,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 7.27,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 7.44,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 7.61,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 7.78,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 7.95,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 8.12,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 8.29,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 8.29,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 7.355,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 8.035,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 7.1,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 7.27,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 7.44,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 7.61,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 7.78,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 7.95,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 8.12,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 8.29,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 7.185,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 7.355,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 7.525,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 7.695,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 7.865,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 8.035,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 8.205,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 8.375,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 8.46,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 8.97,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 9.31,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 8.8,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 9.48,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 8.46,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 8.63,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 8.8,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 8.97,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 9.14,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 9.31,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 9.48,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 9.65,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 9.65,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 8.715,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 9.395,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 8.46,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 8.63,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 8.8,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 8.97,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 9.14,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 9.31,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 9.48,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 9.65,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 8.545,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 8.715,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 8.885,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 9.055,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 9.225,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 9.395,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 9.565,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 9.735,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 9.82,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 10.33,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 10.67,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.8
    },
    {
      "t": 10.16,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 10.84,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.7
    },
    {
      "t": 9.82,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 9.99,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 10.16,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 10.33,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.16
    },
    {
      "t": 10.5,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 10.67,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 10.84,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 11.01,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.4
    },
    {
      "t": 11.01,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 10.075,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 10.755,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.6
    },
    {
      "t": 9.82,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 9.99,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 10.16,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 10.33,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 10.5,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 10.67,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 10.84,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 11.01,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 9.905,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 10.075,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 10.245,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 10.415,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 10.585,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 10.755,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 10.925,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 11.095,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.26
    },
    {
      "t": 3.02,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.7
    },
    {
      "t": 3.275,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.7
    },
    {
      "t": 3.36,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 3.53,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 3.7,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 3.87,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 4.04,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 4.21,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 4.38,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.7
    },
    {
      "t": 4.72,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 4.89,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 5.06,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.7
    },
    {
      "t": 5.4,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.7
    },
    {
      "t": 5.74,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.7
    },
    {
      "t": 5.995,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.7
    },
    {
      "t": 6.08,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 6.25,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 6.42,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 6.59,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 6.76,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 6.93,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 7.1,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.7
    },
    {
      "t": 7.44,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 7.61,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 7.78,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.7
    },
    {
      "t": 8.12,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.7
    },
    {
      "t": 8.46,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.7
    },
    {
      "t": 8.715,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.7
    },
    {
      "t": 8.8,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 8.97,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 9.14,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 9.31,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 9.48,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 9.65,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 9.82,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.7
    },
    {
      "t": 10.16,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 10.33,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.7
    },
    {
      "t": 10.5,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.7
    },
    {
      "t": 10.84,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.7
    },
    {
      "t": 5.74,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 5.752,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 5.91,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 5.922,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 6.08,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 6.092,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 6.25,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 6.262,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 6.42,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 6.432,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 6.59,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 6.602,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 6.76,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 6.772,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 6.93,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 6.942,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 7.1,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 7.112,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 7.27,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 7.282,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 7.44,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 7.452,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 7.61,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 7.622,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 7.78,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 7.792,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 7.95,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 7.962,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 8.12,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 8.132,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 8.29,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 8.302,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 8.46,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 8.472,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 8.63,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 8.642,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 8.8,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 8.812,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 8.97,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 8.982,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 9.14,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 9.152,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 9.31,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 9.322,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 9.48,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 9.492,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 9.65,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 9.662,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 9.82,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 9.832,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 9.99,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 10.002,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 10.16,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 10.172,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 10.33,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 10.342,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 10.5,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 10.512,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 10.67,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 10.682,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 10.84,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 10.852,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 11.01,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.55
    },
    {
      "t": 11.022,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.45
    },
    {
      "t": 11.18,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 11.52,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 11.69,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 12.03,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 12.37,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 11.52,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 11.775,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 12.2,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 11.18,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 11.35,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 11.52,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 11.69,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 11.86,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 12.03,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 12.2,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 12.37,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 12.37,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.6
    },
    {
      "t": 11.435,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 12.115,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 11.18,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 11.35,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 11.52,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 11.69,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 11.86,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 12.03,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 12.2,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 12.37,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 11.265,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 11.435,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 11.605,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 11.775,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 11.945,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 12.115,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 12.285,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 12.455,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 12.54,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 12.88,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 13.05,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 13.39,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 13.73,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 12.88,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 13.135,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 13.56,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 12.54,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 12.71,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 12.88,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 13.05,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 13.22,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 13.39,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 13.56,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 13.73,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 13.73,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.6
    },
    {
      "t": 12.795,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 13.475,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 12.54,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 12.71,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 12.88,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 13.05,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 13.22,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 13.39,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 13.56,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 13.73,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 12.625,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 12.795,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 12.965,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 13.135,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 13.305,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 13.475,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 13.645,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 13.815,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 13.9,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 14.24,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 14.41,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 14.75,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 15.09,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 14.24,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 14.495,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 14.92,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 13.9,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 14.07,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 14.24,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 14.41,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 14.58,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 14.75,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 14.92,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 15.09,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 15.09,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.6
    },
    {
      "t": 14.155,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 14.835,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 13.9,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 14.07,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 14.24,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 14.41,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 14.58,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 14.75,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 14.92,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 15.09,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 13.985,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 14.155,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 14.325,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 14.495,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 14.665,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 14.835,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 15.005,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 15.175,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 15.26,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 15.6,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 15.77,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 16.11,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 16.45,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 15.6,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 15.855,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 16.28,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 15.26,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 15.43,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 15.6,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 15.77,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 15.94,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 16.11,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 16.28,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 16.45,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 16.45,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.6
    },
    {
      "t": 15.515,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 16.195,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 15.26,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 15.43,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 15.6,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 15.77,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 15.94,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 16.11,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 16.28,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 16.45,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 15.345,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 15.515,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 15.685,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 15.855,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 16.025,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 16.195,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 16.365,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 16.535,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 16.62,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 16.96,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 17.13,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 17.47,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 17.81,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 16.96,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 17.215,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 17.64,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 16.62,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 16.79,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 16.96,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 17.13,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 17.3,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 17.47,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 17.64,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 17.81,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 17.81,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.6
    },
    {
      "t": 16.875,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 17.555,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 16.62,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 16.79,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 16.96,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 17.13,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 17.3,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 17.47,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 17.64,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 17.81,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 16.705,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 16.875,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 17.045,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 17.215,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 17.385,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 17.555,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 17.725,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 17.895,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 17.98,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 18.32,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 18.49,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 18.83,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 19.17,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.88
    },
    {
      "t": 18.32,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 18.575,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 19.0,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.15,
      "amplitude": 0.76
    },
    {
      "t": 17.98,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 18.15,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 18.32,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 18.49,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 18.66,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 18.83,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 19.0,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.18
    },
    {
      "t": 19.17,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.45
    },
    {
      "t": 19.17,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.6
    },
    {
      "t": 18.235,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 18.915,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 17.98,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 18.15,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 18.32,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 18.49,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 18.66,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 18.83,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 19.0,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 19.17,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 18.065,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 18.235,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 18.405,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 18.575,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 18.745,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 18.915,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 19.085,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 19.255,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.28
    },
    {
      "t": 11.18,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.78
    },
    {
      "t": 11.435,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.78
    },
    {
      "t": 11.52,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 11.69,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 11.86,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 12.03,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 12.2,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 12.37,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 12.54,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.78
    },
    {
      "t": 12.88,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 13.05,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 13.22,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.78
    },
    {
      "t": 13.56,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.78
    },
    {
      "t": 13.9,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.78
    },
    {
      "t": 14.155,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.78
    },
    {
      "t": 14.24,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 14.41,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 14.58,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 14.75,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 14.92,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 15.09,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 15.26,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.78
    },
    {
      "t": 15.6,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 15.77,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 15.94,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.78
    },
    {
      "t": 16.28,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.78
    },
    {
      "t": 16.62,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.78
    },
    {
      "t": 16.875,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.78
    },
    {
      "t": 16.96,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 17.13,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 17.3,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 17.47,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 17.64,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 17.81,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 17.98,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.78
    },
    {
      "t": 18.32,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 18.49,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.78
    },
    {
      "t": 18.66,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.78
    },
    {
      "t": 19.0,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.78
    },
    {
      "t": 11.18,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 11.192,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 11.35,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 11.362,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 11.52,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 11.532,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 11.69,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 11.702,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 11.86,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 11.872,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 12.03,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 12.042,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 12.2,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 12.212,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 12.37,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 12.382,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 12.54,
      "voice": "rhodes_L",
      "pitch_index": 10,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 12.552,
      "voice": "rhodes_R",
      "pitch_index": 10,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 12.71,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 12.722,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 12.88,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 12.892,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 13.05,
      "voice": "rhodes_L",
      "pitch_index": 13,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 13.062,
      "voice": "rhodes_R",
      "pitch_index": 13,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 13.22,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 13.232,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 13.39,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 13.402,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 13.56,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 13.572,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 13.73,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 13.742,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 11.52,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 11.69,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 11.86,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 12.03,
      "voice": "marimba",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 12.2,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 12.37,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 12.54,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 12.71,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 12.54,
      "voice": "reed",
      "pitch_index": 4,
      "duration_seconds": 0.306,
      "amplitude": 0.58
    },
    {
      "t": 12.54,
      "voice": "reed",
      "pitch_index": 7,
      "duration_seconds": 0.306,
      "amplitude": 0.58
    },
    {
      "t": 12.54,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 0.306,
      "amplitude": 0.58
    },
    {
      "t": 13.9,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 13.912,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 14.07,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 14.082,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 14.24,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 14.252,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 14.41,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 14.422,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 14.58,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 14.592,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 14.75,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 14.762,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 14.92,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 14.932,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 15.09,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 15.102,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 15.26,
      "voice": "rhodes_L",
      "pitch_index": 10,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 15.272,
      "voice": "rhodes_R",
      "pitch_index": 10,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 15.43,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 15.442,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 15.6,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 15.612,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 15.77,
      "voice": "rhodes_L",
      "pitch_index": 13,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 15.782,
      "voice": "rhodes_R",
      "pitch_index": 13,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 15.94,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 15.952,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 16.11,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 16.122,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 16.28,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 16.292,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 16.45,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 16.462,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 14.24,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 14.41,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 14.58,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 14.75,
      "voice": "marimba",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 14.92,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 15.09,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 15.26,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 15.43,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 15.26,
      "voice": "reed",
      "pitch_index": 4,
      "duration_seconds": 0.306,
      "amplitude": 0.58
    },
    {
      "t": 15.26,
      "voice": "reed",
      "pitch_index": 7,
      "duration_seconds": 0.306,
      "amplitude": 0.58
    },
    {
      "t": 15.26,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 0.306,
      "amplitude": 0.58
    },
    {
      "t": 16.62,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 16.632,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 16.79,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 16.802,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 16.96,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 16.972,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 17.13,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 17.142,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 17.3,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 17.312,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 17.47,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 17.482,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 17.64,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 17.652,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 17.81,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 17.822,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 17.98,
      "voice": "rhodes_L",
      "pitch_index": 10,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 17.992,
      "voice": "rhodes_R",
      "pitch_index": 10,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 18.15,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 18.162,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 18.32,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 18.332,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 18.49,
      "voice": "rhodes_L",
      "pitch_index": 13,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 18.502,
      "voice": "rhodes_R",
      "pitch_index": 13,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 18.66,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 18.672,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 18.83,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 18.842,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 19.0,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 19.012,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 19.17,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.6
    },
    {
      "t": 19.182,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.5
    },
    {
      "t": 16.96,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 17.13,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 17.3,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 17.47,
      "voice": "marimba",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 17.64,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 17.81,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 17.98,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 18.15,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.48
    },
    {
      "t": 17.98,
      "voice": "reed",
      "pitch_index": 4,
      "duration_seconds": 0.306,
      "amplitude": 0.58
    },
    {
      "t": 17.98,
      "voice": "reed",
      "pitch_index": 7,
      "duration_seconds": 0.306,
      "amplitude": 0.58
    },
    {
      "t": 17.98,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 0.306,
      "amplitude": 0.58
    },
    {
      "t": 19.34,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.72
    },
    {
      "t": 20.02,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.72
    },
    {
      "t": 19.34,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 19.68,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 20.02,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 20.36,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 19.34,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 19.68,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 20.02,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 20.36,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 20.7,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.72
    },
    {
      "t": 21.38,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.12,
      "amplitude": 0.72
    },
    {
      "t": 20.7,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 21.04,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 21.38,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 21.72,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.35
    },
    {
      "t": 20.7,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 21.04,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 21.38,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 21.72,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.22
    },
    {
      "t": 19.34,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.65
    },
    {
      "t": 19.595,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.65
    },
    {
      "t": 19.68,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.65
    },
    {
      "t": 19.85,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.65
    },
    {
      "t": 20.02,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.65
    },
    {
      "t": 20.19,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.65
    },
    {
      "t": 20.36,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.65
    },
    {
      "t": 20.53,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.65
    },
    {
      "t": 20.7,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.65
    },
    {
      "t": 21.04,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.65
    },
    {
      "t": 21.21,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.65
    },
    {
      "t": 21.38,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.65
    },
    {
      "t": 21.72,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.65
    },
    {
      "t": 19.34,
      "voice": "reed",
      "pitch_index": 4,
      "duration_seconds": 2.448,
      "amplitude": 0.48
    },
    {
      "t": 19.34,
      "voice": "reed",
      "pitch_index": 7,
      "duration_seconds": 2.448,
      "amplitude": 0.48
    },
    {
      "t": 19.34,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 2.448,
      "amplitude": 0.48
    },
    {
      "t": 22.06,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 22.23,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 22.4,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 22.57,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 22.74,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 22.91,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 23.08,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 23.25,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 22.23,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 22.4,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 22.57,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 22.91,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 23.08,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 23.25,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 22.06,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 22.23,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 22.4,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 22.57,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 22.74,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 22.91,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 23.08,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 23.25,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 23.25,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 22.57,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 22.315,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 22.655,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 22.995,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 22.06,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 22.23,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 22.4,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 22.57,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 22.74,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 22.91,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 23.08,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 23.25,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 22.145,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 22.315,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 22.485,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 22.655,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 22.825,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 22.995,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 23.165,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 23.335,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 23.42,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 23.59,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 23.76,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 23.93,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 24.1,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 24.27,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 24.44,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 24.61,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 23.59,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 23.76,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 23.93,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 24.27,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 24.44,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 24.61,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 23.42,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 23.59,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 23.76,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 23.93,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 24.1,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 24.27,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 24.44,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 24.61,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 24.61,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 23.93,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 23.675,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 24.015,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 24.355,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 23.42,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 23.59,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 23.76,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 23.93,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 24.1,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 24.27,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 24.44,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 24.61,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 23.505,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 23.675,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 23.845,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 24.015,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 24.185,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 24.355,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 24.525,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 24.695,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 24.78,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 24.95,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 25.12,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 25.29,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 25.46,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 25.63,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 25.8,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 25.97,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 24.95,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 25.12,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 25.29,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 25.63,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 25.8,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 25.97,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 24.78,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 24.95,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 25.12,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 25.29,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 25.46,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 25.63,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 25.8,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 25.97,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 25.97,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 25.29,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 25.035,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 25.375,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 25.715,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 24.78,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 24.95,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 25.12,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 25.29,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 25.46,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 25.63,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 25.8,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 25.97,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 24.865,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 25.035,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 25.205,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 25.375,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 25.545,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 25.715,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 25.885,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 26.055,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 26.14,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 26.31,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 26.48,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 26.65,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 26.82,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 26.99,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 27.16,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 27.33,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 26.31,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 26.48,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 26.65,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 26.99,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 27.16,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 27.33,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 26.14,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 26.31,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 26.48,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 26.65,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 26.82,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 26.99,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 27.16,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 27.33,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 27.33,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 26.65,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 26.395,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 26.735,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 27.075,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 26.14,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 26.31,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 26.48,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 26.65,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 26.82,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 26.99,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 27.16,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 27.33,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 26.225,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 26.395,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 26.565,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 26.735,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 26.905,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 27.075,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 27.245,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 27.415,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 27.5,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 27.67,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 27.84,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 28.01,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 28.18,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 28.35,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 28.52,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 28.69,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 27.67,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 27.84,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 28.01,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 28.35,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 28.52,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 28.69,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 27.5,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 27.67,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 27.84,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 28.01,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 28.18,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 28.35,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 28.52,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 28.69,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 28.69,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 28.01,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 27.755,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 28.095,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 28.435,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 27.5,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 27.67,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 27.84,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 28.01,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 28.18,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 28.35,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 28.52,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 28.69,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 27.585,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 27.755,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 27.925,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 28.095,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 28.265,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 28.435,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 28.605,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 28.775,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 28.86,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 29.03,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 29.2,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 29.37,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 29.54,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 29.71,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 29.88,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 30.05,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 29.03,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 29.2,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 29.37,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 29.71,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 29.88,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 30.05,
      "voice": "snare",
      "pitch_index": 0,
      "duration_seconds": 0.13,
      "amplitude": 0.78
    },
    {
      "t": 28.86,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 29.03,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.192
    },
    {
      "t": 29.2,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 29.37,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 29.54,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 29.71,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 29.88,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 30.05,
      "voice": "hat_c",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.48
    },
    {
      "t": 30.05,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 29.37,
      "voice": "hat_o",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.55
    },
    {
      "t": 29.115,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 29.455,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 29.795,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.68
    },
    {
      "t": 28.86,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 29.03,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 29.2,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 29.37,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 29.54,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 29.71,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 29.88,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 30.05,
      "voice": "shaker_L",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.32
    },
    {
      "t": 28.945,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 29.115,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 29.285,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 29.455,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 29.625,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 29.795,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 29.965,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 30.135,
      "voice": "shaker_R",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.3
    },
    {
      "t": 22.06,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.8
    },
    {
      "t": 22.315,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.8
    },
    {
      "t": 22.4,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 22.57,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 22.74,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 22.91,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 23.08,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 23.25,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 23.42,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.8
    },
    {
      "t": 23.76,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 23.93,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 24.1,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.8
    },
    {
      "t": 24.44,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.8
    },
    {
      "t": 24.78,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.8
    },
    {
      "t": 25.035,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.8
    },
    {
      "t": 25.12,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 25.29,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 25.46,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 25.63,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 25.8,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 25.97,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 26.14,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.8
    },
    {
      "t": 26.48,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 26.65,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 26.82,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.8
    },
    {
      "t": 27.16,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.8
    },
    {
      "t": 27.5,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.242,
      "amplitude": 0.8
    },
    {
      "t": 27.755,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.081,
      "amplitude": 0.8
    },
    {
      "t": 27.84,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 28.01,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 28.18,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 28.35,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 28.52,
      "voice": "bass",
      "pitch_index": 5,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 28.69,
      "voice": "bass",
      "pitch_index": 2,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 28.86,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.323,
      "amplitude": 0.8
    },
    {
      "t": 29.2,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 29.37,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 0.162,
      "amplitude": 0.8
    },
    {
      "t": 29.54,
      "voice": "bass",
      "pitch_index": 4,
      "duration_seconds": 0.323,
      "amplitude": 0.8
    },
    {
      "t": 29.88,
      "voice": "bass",
      "pitch_index": 3,
      "duration_seconds": 0.323,
      "amplitude": 0.8
    },
    {
      "t": 22.06,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 22.072,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 22.23,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 22.242,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 22.4,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 22.412,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 22.57,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 22.582,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 22.74,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 22.752,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 22.91,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 22.922,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 23.08,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 23.092,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 23.25,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 23.262,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 23.42,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 23.432,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 23.59,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 23.602,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 23.76,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 23.772,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 23.93,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 23.942,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 24.1,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 24.112,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 24.27,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 24.282,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 24.44,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 24.452,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 24.61,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 24.622,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 22.06,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 22.23,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 22.4,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 22.57,
      "voice": "marimba",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 22.74,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 22.91,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 23.08,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 23.25,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 23.42,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 23.59,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 23.76,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 23.93,
      "voice": "marimba",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 24.1,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 24.27,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 24.44,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 24.61,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 23.42,
      "voice": "reed",
      "pitch_index": 4,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 23.42,
      "voice": "reed",
      "pitch_index": 7,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 23.42,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 23.42,
      "voice": "reed",
      "pitch_index": 14,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 24.1,
      "voice": "reed",
      "pitch_index": 6,
      "duration_seconds": 0.23,
      "amplitude": 0.58
    },
    {
      "t": 24.1,
      "voice": "reed",
      "pitch_index": 9,
      "duration_seconds": 0.23,
      "amplitude": 0.58
    },
    {
      "t": 24.1,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 0.23,
      "amplitude": 0.58
    },
    {
      "t": 24.78,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 24.792,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 24.95,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 24.962,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 25.12,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 25.132,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 25.29,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 25.302,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 25.46,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 25.472,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 25.63,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 25.642,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 25.8,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 25.812,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 25.97,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 25.982,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 26.14,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 26.152,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 26.31,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 26.322,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 26.48,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 26.492,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 26.65,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 26.662,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 26.82,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 26.832,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 26.99,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 27.002,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 27.16,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 27.172,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 27.33,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 27.342,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 24.78,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 24.95,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 25.12,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 25.29,
      "voice": "marimba",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 25.46,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 25.63,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 25.8,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 25.97,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 26.14,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 26.31,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 26.48,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 26.65,
      "voice": "marimba",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 26.82,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 26.99,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 27.16,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 27.33,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 26.14,
      "voice": "reed",
      "pitch_index": 4,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 26.14,
      "voice": "reed",
      "pitch_index": 7,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 26.14,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 26.14,
      "voice": "reed",
      "pitch_index": 14,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 26.82,
      "voice": "reed",
      "pitch_index": 6,
      "duration_seconds": 0.23,
      "amplitude": 0.58
    },
    {
      "t": 26.82,
      "voice": "reed",
      "pitch_index": 9,
      "duration_seconds": 0.23,
      "amplitude": 0.58
    },
    {
      "t": 26.82,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 0.23,
      "amplitude": 0.58
    },
    {
      "t": 27.5,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 27.512,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 27.67,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 27.682,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 27.84,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 27.852,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 28.01,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 28.022,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 28.18,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 28.192,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 28.35,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 28.362,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 28.52,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 28.532,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 28.69,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 28.702,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 28.86,
      "voice": "rhodes_L",
      "pitch_index": 8,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 28.872,
      "voice": "rhodes_R",
      "pitch_index": 8,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 29.03,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 29.042,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 29.2,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 29.212,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 29.37,
      "voice": "rhodes_L",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 29.382,
      "voice": "rhodes_R",
      "pitch_index": 11,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 29.54,
      "voice": "rhodes_L",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 29.552,
      "voice": "rhodes_R",
      "pitch_index": 9,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 29.71,
      "voice": "rhodes_L",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 29.722,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 29.88,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 29.892,
      "voice": "rhodes_R",
      "pitch_index": 4,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 30.05,
      "voice": "rhodes_L",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.62
    },
    {
      "t": 30.062,
      "voice": "rhodes_R",
      "pitch_index": 6,
      "duration_seconds": 0.15,
      "amplitude": 0.52
    },
    {
      "t": 27.5,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 27.67,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 27.84,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 28.01,
      "voice": "marimba",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 28.18,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 28.35,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 28.52,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 28.69,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 28.86,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 29.03,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 29.2,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 29.37,
      "voice": "marimba",
      "pitch_index": 11,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 29.54,
      "voice": "marimba",
      "pitch_index": 9,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 29.71,
      "voice": "marimba",
      "pitch_index": 7,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 29.88,
      "voice": "marimba",
      "pitch_index": 6,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 30.05,
      "voice": "marimba",
      "pitch_index": 4,
      "duration_seconds": 0.153,
      "amplitude": 0.52
    },
    {
      "t": 28.86,
      "voice": "reed",
      "pitch_index": 4,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 28.86,
      "voice": "reed",
      "pitch_index": 7,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 28.86,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 28.86,
      "voice": "reed",
      "pitch_index": 14,
      "duration_seconds": 0.23,
      "amplitude": 0.62
    },
    {
      "t": 29.54,
      "voice": "reed",
      "pitch_index": 6,
      "duration_seconds": 0.23,
      "amplitude": 0.58
    },
    {
      "t": 29.54,
      "voice": "reed",
      "pitch_index": 9,
      "duration_seconds": 0.23,
      "amplitude": 0.58
    },
    {
      "t": 29.54,
      "voice": "reed",
      "pitch_index": 11,
      "duration_seconds": 0.23,
      "amplitude": 0.58
    },
    {
      "t": 30.22,
      "voice": "kick",
      "pitch_index": 0,
      "duration_seconds": 0.3,
      "amplitude": 0.95
    },
    {
      "t": 30.22,
      "voice": "snare",
      "pitch_index": 2,
      "duration_seconds": 0.3,
      "amplitude": 0.9
    },
    {
      "t": 30.22,
      "voice": "clap",
      "pitch_index": 0,
      "duration_seconds": 0.3,
      "amplitude": 0.85
    },
    {
      "t": 30.22,
      "voice": "bass",
      "pitch_index": 0,
      "duration_seconds": 1.5,
      "amplitude": 0.85
    },
    {
      "t": 30.22,
      "voice": "rhodes_L",
      "pitch_index": 4,
      "duration_seconds": 1.3,
      "amplitude": 0.65
    },
    {
      "t": 30.232,
      "voice": "rhodes_R",
      "pitch_index": 7,
      "duration_seconds": 1.3,
      "amplitude": 0.55
    },
    {
      "t": 30.22,
      "voice": "reed",
      "pitch_index": 4,
      "duration_seconds": 1.5,
      "amplitude": 0.7
    }
  ]
}
```

### 10. Field note
The pitch is slightly wrong and the groove is exactly right. The ear forgives the first for the second.
