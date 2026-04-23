# Expedition 021

### 1. System name
Spiral Answer Song

### 2. Pitch organization
Inharmonic spectral tuning, spiral non-closing. 12 pitches derived from a stacked chain of near-fifths (step ratios 1.49 ± 0.03). The scale never closes; repetition of the chain yields new pitches. Reference 180 Hz.

### 3. Rhythmic organization
Additive 3+2+3 at 300 ms. Each phrase is one cycle long (≈2.4 s); call and answer occupy separate cycles with a bell-struck closure between.

### 4. Formal structure
Theme and variation, through-composed. The theme (call + answer) is stated plain, then transformed in three ways: **inversion**, **retrograde**, **augmentation**. A coda merges the two choirs on the home chord. Because formal_repetition is low, no variation restates its predecessor — each is an independent transformation of the original theme.

### 5. Texture and voicing
Homophonic call-response between two choirs:
- **Choir A** (dark, left) — low male vocal × 2 + bowed crotales
- **Choir B** (light, right) — high female vocal × 2 + blown bottle
- **clay_pot** at center-back — the obligatory phrase-closure

Each choir sings a chord as a block.

### 6. Ornament and inflection
Obligatory structural: every phrase (call and answer alike) ends with a clay-pot strike. This is not expressive ornament — it is the grammar's phrase-terminator. A phrase without the pot is incomplete.

### 7. Performance context
Ceremonial / call-response ritual. Two choirs face each other across a space; a separate striker (not in either choir) sounds the pot.

### 8. Relationship to neighboring systems
Shares with Bulgarian women's choir the close homophonic chording in an inharmonic tuning. Shares with Tabla solo the structural importance of percussion accents. Shares with Tuvan khoomei the spiral spectral pitch material. Unique: *theme-and-variation in inharmonic-spiral tuning delivered as two-choir antiphony with an obligatory struck-pot closure at every phrase-end*.

### 9. Audio specification

```json
{
  "duration_seconds": 70.2,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 180,
    "pitches": [
      1.0,
      1.4775,
      2.2533,
      3.2158,
      3.4462,
      3.6186,
      3.7967,
      4.3003,
      4.7603,
      5.0663,
      5.496,
      5.6383
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
    "base_unit_ms": 300
  },
  "voices": [
    {
      "name": "drone_low",
      "timbre": "bass_drone",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "sustained_drone",
      "amplitude": 0.4,
      "spatial_position": [
        0.0,
        -0.3
      ]
    },
    {
      "name": "A_bass",
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
      "rhythm_role": "sustained_drone",
      "amplitude": 0.55,
      "spatial_position": [
        -0.6,
        0.1
      ]
    },
    {
      "name": "A_tenor",
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
      "rhythm_role": "sustained_drone",
      "amplitude": 0.55,
      "spatial_position": [
        -0.4,
        0.15
      ]
    },
    {
      "name": "A_crotales",
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
      "rhythm_role": "sustained_drone",
      "amplitude": 0.55,
      "spatial_position": [
        -0.55,
        0.25
      ]
    },
    {
      "name": "B_soprano",
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
      "rhythm_role": "sustained_drone",
      "amplitude": 0.55,
      "spatial_position": [
        0.6,
        0.12
      ]
    },
    {
      "name": "B_alto",
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
      "rhythm_role": "sustained_drone",
      "amplitude": 0.55,
      "spatial_position": [
        0.4,
        0.18
      ]
    },
    {
      "name": "B_bottle",
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
      "rhythm_role": "sustained_drone",
      "amplitude": 0.55,
      "spatial_position": [
        0.55,
        0.25
      ]
    },
    {
      "name": "pot",
      "timbre": "clay_pot",
      "pitch_indices": [
        0,
        2
      ],
      "rhythm_role": "ritual_punctuation",
      "amplitude": 0.6,
      "spatial_position": [
        0.0,
        0.35
      ]
    }
  ],
  "form": {
    "arc_type": "through_composed",
    "sections": [
      {
        "name": "theme",
        "start_seconds": 0,
        "duration_seconds": 13,
        "character": "A calls, B answers \u2014 theme stated",
        "chord_tones": [
          0,
          2,
          4
        ]
      },
      {
        "name": "var_inversion",
        "start_seconds": 13,
        "duration_seconds": 14,
        "character": "theme inverted",
        "chord_tones": [
          2,
          4,
          5
        ]
      },
      {
        "name": "var_retrograde",
        "start_seconds": 27,
        "duration_seconds": 13,
        "character": "theme backwards",
        "chord_tones": [
          0,
          3,
          5
        ]
      },
      {
        "name": "var_augmented",
        "start_seconds": 40,
        "duration_seconds": 25,
        "character": "theme doubled in duration, four-voice chords",
        "chord_tones": [
          2,
          3,
          5,
          7
        ]
      },
      {
        "name": "coda",
        "start_seconds": 65,
        "duration_seconds": 12,
        "character": "both choirs merge on home",
        "chord_tones": [
          0,
          2,
          4
        ]
      }
    ]
  },
  "ornamentation": {
    "density": 0.22,
    "rule": "Obligatory structural: every phrase (call and answer alike) ends with a clay_pot strike. Without the strike, the next phrase cannot begin \u2014 it is the grammar's phrase terminator."
  },
  "auto_pedal": false,
  "mix": {
    "reverb_wet": 0.32,
    "reverb_length": 2.5,
    "reverb_decay": 3.2,
    "hf_shelf_gain_db": 1.0,
    "hf_shelf_freq": 3800,
    "lpf_hz": 8500
  },
  "events": [
    {
      "t": 1.0,
      "voice": "A_bass",
      "pitch_index": 0,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 1.0,
      "voice": "A_tenor",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 1.0,
      "voice": "A_crotales",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 1.6,
      "voice": "A_bass",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 1.6,
      "voice": "A_tenor",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 1.6,
      "voice": "A_crotales",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 2.2,
      "voice": "A_bass",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 2.2,
      "voice": "A_tenor",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 2.2,
      "voice": "A_crotales",
      "pitch_index": 8,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 2.8,
      "voice": "A_bass",
      "pitch_index": 2,
      "duration_seconds": 0.276,
      "amplitude": 0.6
    },
    {
      "t": 2.8,
      "voice": "A_tenor",
      "pitch_index": 4,
      "duration_seconds": 0.276,
      "amplitude": 0.55
    },
    {
      "t": 2.8,
      "voice": "A_crotales",
      "pitch_index": 6,
      "duration_seconds": 0.276,
      "amplitude": 0.5
    },
    {
      "t": 3.1,
      "voice": "A_bass",
      "pitch_index": 0,
      "duration_seconds": 0.828,
      "amplitude": 0.6
    },
    {
      "t": 3.1,
      "voice": "A_tenor",
      "pitch_index": 2,
      "duration_seconds": 0.828,
      "amplitude": 0.55
    },
    {
      "t": 3.1,
      "voice": "A_crotales",
      "pitch_index": 4,
      "duration_seconds": 0.828,
      "amplitude": 0.5
    },
    {
      "t": 3.91,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 4.6,
      "voice": "B_soprano",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 4.6,
      "voice": "B_alto",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.56
    },
    {
      "t": 4.6,
      "voice": "B_bottle",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 5.2,
      "voice": "B_soprano",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 5.2,
      "voice": "B_alto",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.56
    },
    {
      "t": 5.2,
      "voice": "B_bottle",
      "pitch_index": 8,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 5.8,
      "voice": "B_soprano",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 5.8,
      "voice": "B_alto",
      "pitch_index": 7,
      "duration_seconds": 0.552,
      "amplitude": 0.56
    },
    {
      "t": 5.8,
      "voice": "B_bottle",
      "pitch_index": 9,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 6.4,
      "voice": "B_soprano",
      "pitch_index": 3,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 6.4,
      "voice": "B_alto",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.56
    },
    {
      "t": 6.4,
      "voice": "B_bottle",
      "pitch_index": 7,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 7.0,
      "voice": "B_soprano",
      "pitch_index": 0,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 7.0,
      "voice": "B_alto",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.56
    },
    {
      "t": 7.0,
      "voice": "B_bottle",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 7.51,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.55
    },
    {
      "t": 14.0,
      "voice": "A_bass",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.58
    },
    {
      "t": 14.0,
      "voice": "A_tenor",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.53
    },
    {
      "t": 14.0,
      "voice": "A_crotales",
      "pitch_index": 8,
      "duration_seconds": 0.552,
      "amplitude": 0.48
    },
    {
      "t": 14.6,
      "voice": "A_bass",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.58
    },
    {
      "t": 14.6,
      "voice": "A_tenor",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.53
    },
    {
      "t": 14.6,
      "voice": "A_crotales",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.48
    },
    {
      "t": 15.2,
      "voice": "A_bass",
      "pitch_index": 0,
      "duration_seconds": 0.552,
      "amplitude": 0.58
    },
    {
      "t": 15.2,
      "voice": "A_tenor",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.53
    },
    {
      "t": 15.2,
      "voice": "A_crotales",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.48
    },
    {
      "t": 15.8,
      "voice": "A_bass",
      "pitch_index": 2,
      "duration_seconds": 0.276,
      "amplitude": 0.58
    },
    {
      "t": 15.8,
      "voice": "A_tenor",
      "pitch_index": 4,
      "duration_seconds": 0.276,
      "amplitude": 0.53
    },
    {
      "t": 15.8,
      "voice": "A_crotales",
      "pitch_index": 6,
      "duration_seconds": 0.276,
      "amplitude": 0.48
    },
    {
      "t": 16.1,
      "voice": "A_bass",
      "pitch_index": 4,
      "duration_seconds": 0.828,
      "amplitude": 0.58
    },
    {
      "t": 16.1,
      "voice": "A_tenor",
      "pitch_index": 6,
      "duration_seconds": 0.828,
      "amplitude": 0.53
    },
    {
      "t": 16.1,
      "voice": "A_crotales",
      "pitch_index": 8,
      "duration_seconds": 0.828,
      "amplitude": 0.48
    },
    {
      "t": 16.91,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.55,
      "amplitude": 0.55
    },
    {
      "t": 17.6,
      "voice": "B_soprano",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 17.6,
      "voice": "B_alto",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 17.6,
      "voice": "B_bottle",
      "pitch_index": 8,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 18.2,
      "voice": "B_soprano",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 18.2,
      "voice": "B_alto",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 18.2,
      "voice": "B_bottle",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 18.8,
      "voice": "B_soprano",
      "pitch_index": 1,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 18.8,
      "voice": "B_alto",
      "pitch_index": 3,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 18.8,
      "voice": "B_bottle",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 19.4,
      "voice": "B_soprano",
      "pitch_index": 3,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 19.4,
      "voice": "B_alto",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 19.4,
      "voice": "B_bottle",
      "pitch_index": 7,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 20.0,
      "voice": "B_soprano",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 20.0,
      "voice": "B_alto",
      "pitch_index": 8,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 20.0,
      "voice": "B_bottle",
      "pitch_index": 10,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 20.51,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.55,
      "amplitude": 0.55
    },
    {
      "t": 27.0,
      "voice": "A_bass",
      "pitch_index": 0,
      "duration_seconds": 0.828,
      "amplitude": 0.6
    },
    {
      "t": 27.0,
      "voice": "A_tenor",
      "pitch_index": 3,
      "duration_seconds": 0.828,
      "amplitude": 0.55
    },
    {
      "t": 27.0,
      "voice": "A_crotales",
      "pitch_index": 5,
      "duration_seconds": 0.828,
      "amplitude": 0.5
    },
    {
      "t": 27.9,
      "voice": "A_bass",
      "pitch_index": 2,
      "duration_seconds": 0.276,
      "amplitude": 0.6
    },
    {
      "t": 27.9,
      "voice": "A_tenor",
      "pitch_index": 5,
      "duration_seconds": 0.276,
      "amplitude": 0.55
    },
    {
      "t": 27.9,
      "voice": "A_crotales",
      "pitch_index": 7,
      "duration_seconds": 0.276,
      "amplitude": 0.5
    },
    {
      "t": 28.2,
      "voice": "A_bass",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 28.2,
      "voice": "A_tenor",
      "pitch_index": 7,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 28.2,
      "voice": "A_crotales",
      "pitch_index": 9,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 28.8,
      "voice": "A_bass",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 28.8,
      "voice": "A_tenor",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 28.8,
      "voice": "A_crotales",
      "pitch_index": 7,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 29.4,
      "voice": "A_bass",
      "pitch_index": 0,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 29.4,
      "voice": "A_tenor",
      "pitch_index": 3,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 29.4,
      "voice": "A_crotales",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 29.91,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.58
    },
    {
      "t": 30.6,
      "voice": "B_soprano",
      "pitch_index": 0,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 30.6,
      "voice": "B_alto",
      "pitch_index": 3,
      "duration_seconds": 0.552,
      "amplitude": 0.57
    },
    {
      "t": 30.6,
      "voice": "B_bottle",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.52
    },
    {
      "t": 31.2,
      "voice": "B_soprano",
      "pitch_index": 3,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 31.2,
      "voice": "B_alto",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.57
    },
    {
      "t": 31.2,
      "voice": "B_bottle",
      "pitch_index": 8,
      "duration_seconds": 0.552,
      "amplitude": 0.52
    },
    {
      "t": 31.8,
      "voice": "B_soprano",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 31.8,
      "voice": "B_alto",
      "pitch_index": 8,
      "duration_seconds": 0.552,
      "amplitude": 0.57
    },
    {
      "t": 31.8,
      "voice": "B_bottle",
      "pitch_index": 10,
      "duration_seconds": 0.552,
      "amplitude": 0.52
    },
    {
      "t": 32.4,
      "voice": "B_soprano",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 32.4,
      "voice": "B_alto",
      "pitch_index": 7,
      "duration_seconds": 0.552,
      "amplitude": 0.57
    },
    {
      "t": 32.4,
      "voice": "B_bottle",
      "pitch_index": 9,
      "duration_seconds": 0.552,
      "amplitude": 0.52
    },
    {
      "t": 33.0,
      "voice": "B_soprano",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.62
    },
    {
      "t": 33.0,
      "voice": "B_alto",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.57
    },
    {
      "t": 33.0,
      "voice": "B_bottle",
      "pitch_index": 7,
      "duration_seconds": 0.552,
      "amplitude": 0.52
    },
    {
      "t": 33.51,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.6,
      "amplitude": 0.58
    },
    {
      "t": 40.0,
      "voice": "A_bass",
      "pitch_index": 0,
      "duration_seconds": 0.828,
      "amplitude": 0.65
    },
    {
      "t": 40.0,
      "voice": "A_tenor",
      "pitch_index": 3,
      "duration_seconds": 0.828,
      "amplitude": 0.6
    },
    {
      "t": 40.0,
      "voice": "A_crotales",
      "pitch_index": 5,
      "duration_seconds": 0.828,
      "amplitude": 0.55
    },
    {
      "t": 40.9,
      "voice": "A_bass",
      "pitch_index": 2,
      "duration_seconds": 0.828,
      "amplitude": 0.65
    },
    {
      "t": 40.9,
      "voice": "A_tenor",
      "pitch_index": 5,
      "duration_seconds": 0.828,
      "amplitude": 0.6
    },
    {
      "t": 40.9,
      "voice": "A_crotales",
      "pitch_index": 7,
      "duration_seconds": 0.828,
      "amplitude": 0.55
    },
    {
      "t": 41.8,
      "voice": "A_bass",
      "pitch_index": 4,
      "duration_seconds": 0.828,
      "amplitude": 0.65
    },
    {
      "t": 41.8,
      "voice": "A_tenor",
      "pitch_index": 7,
      "duration_seconds": 0.828,
      "amplitude": 0.6
    },
    {
      "t": 41.8,
      "voice": "A_crotales",
      "pitch_index": 9,
      "duration_seconds": 0.828,
      "amplitude": 0.55
    },
    {
      "t": 42.7,
      "voice": "A_bass",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.65
    },
    {
      "t": 42.7,
      "voice": "A_tenor",
      "pitch_index": 5,
      "duration_seconds": 0.552,
      "amplitude": 0.6
    },
    {
      "t": 42.7,
      "voice": "A_crotales",
      "pitch_index": 7,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 43.3,
      "voice": "A_bass",
      "pitch_index": 0,
      "duration_seconds": 1.104,
      "amplitude": 0.65
    },
    {
      "t": 43.3,
      "voice": "A_tenor",
      "pitch_index": 3,
      "duration_seconds": 1.104,
      "amplitude": 0.6
    },
    {
      "t": 43.3,
      "voice": "A_crotales",
      "pitch_index": 5,
      "duration_seconds": 1.104,
      "amplitude": 0.55
    },
    {
      "t": 44.41,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.65
    },
    {
      "t": 45.5,
      "voice": "B_soprano",
      "pitch_index": 2,
      "duration_seconds": 0.828,
      "amplitude": 0.68
    },
    {
      "t": 45.5,
      "voice": "B_alto",
      "pitch_index": 5,
      "duration_seconds": 0.828,
      "amplitude": 0.62
    },
    {
      "t": 45.5,
      "voice": "B_bottle",
      "pitch_index": 7,
      "duration_seconds": 0.828,
      "amplitude": 0.56
    },
    {
      "t": 46.4,
      "voice": "B_soprano",
      "pitch_index": 4,
      "duration_seconds": 0.828,
      "amplitude": 0.68
    },
    {
      "t": 46.4,
      "voice": "B_alto",
      "pitch_index": 7,
      "duration_seconds": 0.828,
      "amplitude": 0.62
    },
    {
      "t": 46.4,
      "voice": "B_bottle",
      "pitch_index": 9,
      "duration_seconds": 0.828,
      "amplitude": 0.56
    },
    {
      "t": 47.3,
      "voice": "B_soprano",
      "pitch_index": 5,
      "duration_seconds": 0.828,
      "amplitude": 0.68
    },
    {
      "t": 47.3,
      "voice": "B_alto",
      "pitch_index": 8,
      "duration_seconds": 0.828,
      "amplitude": 0.62
    },
    {
      "t": 47.3,
      "voice": "B_bottle",
      "pitch_index": 10,
      "duration_seconds": 0.828,
      "amplitude": 0.56
    },
    {
      "t": 48.2,
      "voice": "B_soprano",
      "pitch_index": 3,
      "duration_seconds": 0.828,
      "amplitude": 0.68
    },
    {
      "t": 48.2,
      "voice": "B_alto",
      "pitch_index": 6,
      "duration_seconds": 0.828,
      "amplitude": 0.62
    },
    {
      "t": 48.2,
      "voice": "B_bottle",
      "pitch_index": 8,
      "duration_seconds": 0.828,
      "amplitude": 0.56
    },
    {
      "t": 49.1,
      "voice": "B_soprano",
      "pitch_index": 0,
      "duration_seconds": 0.828,
      "amplitude": 0.68
    },
    {
      "t": 49.1,
      "voice": "B_alto",
      "pitch_index": 3,
      "duration_seconds": 0.828,
      "amplitude": 0.62
    },
    {
      "t": 49.1,
      "voice": "B_bottle",
      "pitch_index": 5,
      "duration_seconds": 0.828,
      "amplitude": 0.56
    },
    {
      "t": 49.91,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 0.7,
      "amplitude": 0.65
    },
    {
      "t": 65.0,
      "voice": "A_bass",
      "pitch_index": 0,
      "duration_seconds": 0.828,
      "amplitude": 0.55
    },
    {
      "t": 65.0,
      "voice": "A_tenor",
      "pitch_index": 2,
      "duration_seconds": 0.828,
      "amplitude": 0.5
    },
    {
      "t": 65.0,
      "voice": "A_crotales",
      "pitch_index": 4,
      "duration_seconds": 0.828,
      "amplitude": 0.45
    },
    {
      "t": 65.0,
      "voice": "B_soprano",
      "pitch_index": 0,
      "duration_seconds": 0.828,
      "amplitude": 0.55
    },
    {
      "t": 65.0,
      "voice": "B_alto",
      "pitch_index": 2,
      "duration_seconds": 0.828,
      "amplitude": 0.5
    },
    {
      "t": 65.0,
      "voice": "B_bottle",
      "pitch_index": 4,
      "duration_seconds": 0.828,
      "amplitude": 0.45
    },
    {
      "t": 65.9,
      "voice": "A_bass",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 65.9,
      "voice": "A_tenor",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 65.9,
      "voice": "A_crotales",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.45
    },
    {
      "t": 65.9,
      "voice": "B_soprano",
      "pitch_index": 2,
      "duration_seconds": 0.552,
      "amplitude": 0.55
    },
    {
      "t": 65.9,
      "voice": "B_alto",
      "pitch_index": 4,
      "duration_seconds": 0.552,
      "amplitude": 0.5
    },
    {
      "t": 65.9,
      "voice": "B_bottle",
      "pitch_index": 6,
      "duration_seconds": 0.552,
      "amplitude": 0.45
    },
    {
      "t": 66.5,
      "voice": "A_bass",
      "pitch_index": 0,
      "duration_seconds": 1.104,
      "amplitude": 0.55
    },
    {
      "t": 66.5,
      "voice": "A_tenor",
      "pitch_index": 2,
      "duration_seconds": 1.104,
      "amplitude": 0.5
    },
    {
      "t": 66.5,
      "voice": "A_crotales",
      "pitch_index": 4,
      "duration_seconds": 1.104,
      "amplitude": 0.45
    },
    {
      "t": 66.5,
      "voice": "B_soprano",
      "pitch_index": 0,
      "duration_seconds": 1.104,
      "amplitude": 0.55
    },
    {
      "t": 66.5,
      "voice": "B_alto",
      "pitch_index": 2,
      "duration_seconds": 1.104,
      "amplitude": 0.5
    },
    {
      "t": 66.5,
      "voice": "B_bottle",
      "pitch_index": 4,
      "duration_seconds": 1.104,
      "amplitude": 0.45
    },
    {
      "t": 67.61,
      "voice": "pot",
      "pitch_index": 0,
      "duration_seconds": 1.2,
      "amplitude": 0.7
    }
  ]
}
```

### 10. Field note
The pot is the only sound both choirs share. Without it, they would be two different pieces.
