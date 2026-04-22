# Expedition 012

### 1. System name
Theme and Variations on the Golden Line

### 2. Pitch organization
Seven equal logarithmic divisions of the octave (7-TET). Every step is the irrational ratio 2^(1/7) ≈ 1.1041; no two pitches except the octaves form rational simple-integer ratios. The system is octave-repeating (two full octaves used). The *absence* of simple rational intervals is the system's signature — all intervals are irrational, all consonance is perceptual rather than acoustic.

The home pitch at 210 Hz is the tonic. Two other structural pitches function as semi-cadential landings: index 2 (2^(2/7) ≈ 1.219, a "near-minor-third") and index 4 (2^(4/7) ≈ 1.486, a "near-fifth").

### 3. Rhythmic organization
Additive 2+3+2+3+2 = 12 units at 140 ms unit. The irregular grouping produces a shuffled-triplet feel. Rhythmic ornament is dense and is the *only* ornament in the system — melodic ornament (grace notes, pitch bends) is prohibited. Long notes are habitually subdivided into rapid sub-groupings (duplets over triplets, ornaments of 3-against-2) with passing tones that do not belong to the scale-harmonic grammar but serve purely rhythmic function.

### 4. Formal structure
Theme and variations, through-composed. An introduction establishes the meter; the theme is stated plain; five variations transform it (rhythmic ornament, doubled speed, contour inversion, augmentation, fragmentation); a coda restates the theme plain and cadences on home. Each variation is self-contained but references the theme.

### 5. Texture and voicing
Soloist with accompaniment — one melodic lead (sung) and one membrane drum. Voice independence is high within this sparse texture: the soloist carries the pitched material and the drum carries the rhythmic commentary, and they alternate as much as overlap.

### 6. Ornament and inflection
Rhythmic-only. Ornament density is very high (~0.88 of notes receive some form of rhythmic elaboration).

### 7. Performance context
Ritual-religious, call-response. The soloist states material, the drum answers. The listener participates as ritual audience.

### 8. Relationship to neighboring systems
Shares with **Korean Pansori** the solo-voice-with-drum format, and the theme-and-variation (as narrative episodes) structure. Shares with **Tabla solo** the density and precision of rhythmic ornament. Shares with **Sufi Qawwali** the ritual call-response between voice and accompaniment. The unique synthesis: *irrational-interval theme and variations where the only permitted ornament is rhythmic density, and where the accompanist and soloist answer each other as near-equals*.

### 9. Audio specification

```json
{
  "duration_seconds": 72.0,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 210,
    "pitches": [
      1.0,
      1.1041,
      1.219,
      1.3459,
      1.486,
      1.6407,
      1.8114,
      2.0,
      2.0,
      2.2082,
      2.438,
      2.6918,
      2.972,
      3.2813,
      3.6229,
      4.0
    ],
    "octave_repeats": true
  },
  "rhythm_system": {
    "type": "additive",
    "groupings": [
      2,
      3,
      2,
      3,
      2
    ],
    "base_unit_ms": 140
  },
  "voices": [
    {
      "name": "soloist",
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
        12,
        13
      ],
      "rhythm_role": "melodic_lead",
      "amplitude": 0.85,
      "spatial_position": [
        0.0,
        0.25
      ]
    },
    {
      "name": "drum",
      "timbre": "membrane_drum",
      "pitch_indices": [
        0
      ],
      "rhythm_role": "percussive",
      "amplitude": 0.7,
      "spatial_position": [
        -0.3,
        -0.3
      ]
    }
  ],
  "form": {
    "arc_type": "through_composed",
    "sections": [
      {
        "name": "introduction",
        "start_seconds": 0,
        "duration_seconds": 6,
        "character": "drum alone sets the additive meter",
        "chord_tones": [
          0
        ]
      },
      {
        "name": "theme_statement",
        "start_seconds": 6,
        "duration_seconds": 6,
        "character": "soloist states the theme plain",
        "chord_tones": [
          0,
          2,
          4
        ]
      },
      {
        "name": "var1_rhythmic_ornament",
        "start_seconds": 12,
        "duration_seconds": 11,
        "character": "theme densely ornamented rhythmically; drum triplets",
        "chord_tones": [
          0,
          2,
          4
        ]
      },
      {
        "name": "var2_double_speed",
        "start_seconds": 23,
        "duration_seconds": 11,
        "character": "theme at double speed; drum call-response",
        "chord_tones": [
          0,
          3,
          5
        ]
      },
      {
        "name": "var3_inversion",
        "start_seconds": 34,
        "duration_seconds": 9,
        "character": "theme contour mirrored",
        "chord_tones": [
          2,
          4,
          5
        ]
      },
      {
        "name": "var4_augmentation",
        "start_seconds": 43,
        "duration_seconds": 9,
        "character": "theme doubled in duration; percussion sparse",
        "chord_tones": [
          0,
          2,
          4
        ]
      },
      {
        "name": "var5_fragments",
        "start_seconds": 52,
        "duration_seconds": 11,
        "character": "theme fragments exchanged with drum",
        "chord_tones": [
          0,
          2,
          3,
          4,
          5
        ]
      },
      {
        "name": "coda",
        "start_seconds": 63,
        "duration_seconds": 9,
        "character": "plain theme returns; final drum flourish and tonic",
        "chord_tones": [
          0
        ]
      }
    ]
  },
  "ornamentation": {
    "density": 0.88,
    "rule": "Rhythmic ornament is dense. Long theme notes (\u22652 units) are subdivided into 2-3 rapid subdivisions with alternating passing pitch. The drum mirrors this density with triplets-against-duplets."
  },
  "auto_pedal": false,
  "events": [
    {
      "t": 0.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.85
    },
    {
      "t": 0.28,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 0.7,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 0.98,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 1.4,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 1.68,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.85
    },
    {
      "t": 1.96,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 2.38,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 2.66,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 3.08,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 3.36,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.85
    },
    {
      "t": 3.64,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 4.06,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 4.34,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 4.76,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.55
    },
    {
      "t": 6.0,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.399,
      "amplitude": 0.85
    },
    {
      "t": 6.42,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.266,
      "amplitude": 0.85
    },
    {
      "t": 6.7,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.266,
      "amplitude": 0.85
    },
    {
      "t": 6.98,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 7.12,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.399,
      "amplitude": 0.85
    },
    {
      "t": 7.54,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.266,
      "amplitude": 0.85
    },
    {
      "t": 7.82,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.266,
      "amplitude": 0.85
    },
    {
      "t": 8.1,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 8.24,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.266,
      "amplitude": 0.85
    },
    {
      "t": 8.52,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.532,
      "amplitude": 0.85
    },
    {
      "t": 5.04,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 5.32,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 5.74,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 6.02,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 6.44,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 6.72,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 7.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 7.42,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 7.7,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 8.12,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 8.4,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 8.68,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 9.1,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 9.38,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 9.8,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 10.08,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.7
    },
    {
      "t": 10.36,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 10.78,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.08,
      "amplitude": 0.45
    },
    {
      "t": 12.0,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 12.14,
      "voice": "soloist",
      "pitch_index": 1,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 12.28,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 12.42,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.266,
      "amplitude": 0.82
    },
    {
      "t": 12.7,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 12.84,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 12.98,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 13.12,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 13.26,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 13.4,
      "voice": "soloist",
      "pitch_index": 6,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 13.54,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 13.68,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 13.82,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 13.96,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 14.1,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 14.24,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 14.38,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 14.52,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 14.66,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 14.8,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 14.94,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 15.08,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.266,
      "amplitude": 0.82
    },
    {
      "t": 15.36,
      "voice": "soloist",
      "pitch_index": 1,
      "duration_seconds": 0.266,
      "amplitude": 0.82
    },
    {
      "t": 12.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.092,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.185,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.277,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.37,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.462,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.554,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.647,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.739,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.832,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 12.924,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.016,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.109,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.201,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.294,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.386,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.478,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.571,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.663,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.756,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.848,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 13.94,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.033,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.125,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.218,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.31,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.402,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.495,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.587,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.68,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.772,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.864,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 14.957,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.049,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.142,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.234,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.326,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.419,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.511,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.604,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.696,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.788,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.881,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 15.973,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.066,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.158,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.25,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.343,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.435,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.528,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.62,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.712,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.805,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.897,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 16.99,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.082,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.174,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.267,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.359,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.452,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.544,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.636,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.729,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.821,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 17.914,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.006,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.098,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.191,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.283,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.376,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.468,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.56,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.653,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.745,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.838,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 18.93,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.022,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.115,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.207,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.3,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.392,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.484,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.577,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.669,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.762,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.854,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 19.946,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.55
    },
    {
      "t": 20.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 20.14,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 20.28,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 20.42,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 20.56,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 20.7,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 20.84,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 20.98,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 21.12,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 21.26,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 21.4,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 21.54,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 21.68,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 21.82,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 21.96,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 22.1,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 22.24,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 22.38,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.72
    },
    {
      "t": 23.0,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 23.14,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 23.28,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 23.42,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 23.56,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 23.7,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 23.84,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 23.98,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 24.12,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.85
    },
    {
      "t": 24.26,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.266,
      "amplitude": 0.85
    },
    {
      "t": 23.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.85
    },
    {
      "t": 23.28,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 23.7,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 23.98,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 24.4,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 24.68,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.85
    },
    {
      "t": 24.96,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 25.38,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 25.66,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 26.08,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 26.36,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.85
    },
    {
      "t": 26.64,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 27.06,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 27.34,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 27.76,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 28.04,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.85
    },
    {
      "t": 28.32,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 28.74,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 29.02,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 29.44,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 29.72,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.85
    },
    {
      "t": 30.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 30.42,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 30.7,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 31.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.098,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.196,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.294,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.392,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.49,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.588,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.686,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.784,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.882,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 31.98,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.078,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.176,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.274,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.372,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.47,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.568,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.666,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.764,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.862,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 32.96,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 33.058,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 33.156,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 33.254,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 33.352,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 33.45,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.75
    },
    {
      "t": 34.0,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 34.14,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 34.28,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 34.42,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.266,
      "amplitude": 0.82
    },
    {
      "t": 34.7,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.266,
      "amplitude": 0.82
    },
    {
      "t": 34.98,
      "voice": "soloist",
      "pitch_index": 1,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 35.12,
      "voice": "soloist",
      "pitch_index": 6,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 35.26,
      "voice": "soloist",
      "pitch_index": 7,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 35.4,
      "voice": "soloist",
      "pitch_index": 6,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 35.54,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 35.68,
      "voice": "soloist",
      "pitch_index": 1,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 35.82,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 35.96,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 36.1,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 36.24,
      "voice": "soloist",
      "pitch_index": 1,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 36.38,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 36.52,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.82
    },
    {
      "t": 36.66,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.532,
      "amplitude": 0.82
    },
    {
      "t": 34.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.7
    },
    {
      "t": 34.28,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 34.7,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 34.98,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 35.4,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 35.68,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.7
    },
    {
      "t": 35.96,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 36.38,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 36.66,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 37.08,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 37.36,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.7
    },
    {
      "t": 37.64,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 38.06,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 38.34,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 38.76,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 39.04,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.7
    },
    {
      "t": 39.32,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 39.74,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 40.02,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 40.44,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 40.72,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.7
    },
    {
      "t": 41.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 41.42,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 41.7,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 43.0,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.798,
      "amplitude": 0.88
    },
    {
      "t": 43.84,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.532,
      "amplitude": 0.88
    },
    {
      "t": 44.4,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.532,
      "amplitude": 0.88
    },
    {
      "t": 44.96,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.266,
      "amplitude": 0.88
    },
    {
      "t": 45.24,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.798,
      "amplitude": 0.88
    },
    {
      "t": 46.08,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.532,
      "amplitude": 0.88
    },
    {
      "t": 46.64,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.532,
      "amplitude": 0.88
    },
    {
      "t": 47.2,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.266,
      "amplitude": 0.88
    },
    {
      "t": 47.48,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.532,
      "amplitude": 0.88
    },
    {
      "t": 48.04,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 1.064,
      "amplitude": 0.88
    },
    {
      "t": 43.0,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 44.68,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 46.36,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 48.04,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 49.72,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 51.4,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.1,
      "amplitude": 0.85
    },
    {
      "t": 52.0,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 52.14,
      "voice": "soloist",
      "pitch_index": 1,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 52.28,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 52.42,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 52.56,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 52.7,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 52.84,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 52.98,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 53.263,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 53.382,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 53.501,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 53.62,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 53.839,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 53.979,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 54.119,
      "voice": "soloist",
      "pitch_index": 6,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 54.259,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 54.542,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 54.661,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 54.78,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 54.899,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 55.118,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 55.258,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 55.398,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 55.538,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 55.678,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 55.961,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 56.08,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 56.199,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 56.318,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 56.537,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.266,
      "amplitude": 0.8
    },
    {
      "t": 56.817,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 56.957,
      "voice": "soloist",
      "pitch_index": 1,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 57.097,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 57.237,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 57.52,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 57.639,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 57.758,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 57.877,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.06,
      "amplitude": 0.65
    },
    {
      "t": 63.0,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.399,
      "amplitude": 0.8
    },
    {
      "t": 63.42,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.266,
      "amplitude": 0.8
    },
    {
      "t": 63.7,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.266,
      "amplitude": 0.8
    },
    {
      "t": 63.98,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 64.12,
      "voice": "soloist",
      "pitch_index": 5,
      "duration_seconds": 0.399,
      "amplitude": 0.8
    },
    {
      "t": 64.54,
      "voice": "soloist",
      "pitch_index": 4,
      "duration_seconds": 0.266,
      "amplitude": 0.8
    },
    {
      "t": 64.82,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.266,
      "amplitude": 0.8
    },
    {
      "t": 65.1,
      "voice": "soloist",
      "pitch_index": 3,
      "duration_seconds": 0.133,
      "amplitude": 0.8
    },
    {
      "t": 65.24,
      "voice": "soloist",
      "pitch_index": 2,
      "duration_seconds": 0.266,
      "amplitude": 0.8
    },
    {
      "t": 65.52,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 0.532,
      "amplitude": 0.8
    },
    {
      "t": 68.5,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5
    },
    {
      "t": 68.57,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.52
    },
    {
      "t": 68.64,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.54
    },
    {
      "t": 68.71,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.56
    },
    {
      "t": 68.78,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.07,
      "amplitude": 0.5800000000000001
    },
    {
      "t": 68.85,
      "voice": "drum",
      "pitch_index": 0,
      "duration_seconds": 0.2,
      "amplitude": 0.9
    },
    {
      "t": 70.0,
      "voice": "soloist",
      "pitch_index": 0,
      "duration_seconds": 2.5,
      "amplitude": 0.7
    }
  ]
}
```

### 10. Field note
7-TET has no pure fifth, no pure fourth. The ear hears the piece and gropes for consonance that never quite lands. What resolves the piece is not harmonic arrival but rhythmic arrival: the drum stops on the same beat the voice lands on home, and the ear accepts this coincidence as consonance.
