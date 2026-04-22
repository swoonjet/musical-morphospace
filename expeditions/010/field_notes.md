# Expedition 010

### 1. System name
Nested Breath of the Two Choirs

### 2. Pitch organization
Inharmonic spectral scale, non-octave-repeating. Ten pitches derived from a slightly-detuned harmonic series of a 130 Hz fundamental, with small stretches applied so no pair forms a pure 2:1: [1.0, 2.03, 2.97, 4.11, 5.04, 6.08, 7.03, 8.15, 9.12, 10.24]. The scale has no tonal home in the functional sense; what substitutes for a tonic is the *first pitch* (1/1), which both choirs always converge on at cadences.

Pitches are fixed, but obligatory ornament modifies every held note (see §6).

### 3. Rhythmic organization
Additive metric, 5+4 units × 300 ms base (cycle 2.7 s), but the metric serves only as the substrate for chord-exchange; the piece's pulse is *breath-paced*, slow, with silences weighted as heavily as sounds. The cycle rarely makes itself heard because events are chord-length rather than event-dense.

### 4. Formal structure
Nested hierarchical, three movements:
- **I. Exposition** — three simple call-response exchanges, 2-second silences between
- **II. Development** — three nested calls, each outer statement containing two inner sub-statements in *both* the calling choir and the answering choir (calls within calls)
- **III. Resolution** — the choirs converge, both singing the same chord, finally merging in unison on the home pitch

The hierarchy repeats: an outer call contains inner calls; each inner call is itself a call-response at the sub-level; the whole piece is one large call-response over three movements.

### 5. Texture and voicing
Two antiphonal choirs in stereo — **Left** (low male vocal, reed, bowed string) and **Right** (high female vocal, bamboo flute, bowed string). Each choir sings a three-voice chord as a unit. Voice independence within a choir is zero — each choir moves as a body; independence *between* choirs is the whole point of the form.

### 6. Ornament and inflection
Obligatory structural ornament. Every sustained chord descends 40-70 cents in its final third — a collective "morendo". This is grammar, not expression: a chord without descent is incomplete and the answering choir cannot enter until the descent has happened. Ornament density is therefore high (0.85 of events carry the obligatory ornament).

### 7. Performance context
Ritual religious. The two choirs stand on opposite walls of an enclosed space; the silence between calls is understood as the sound's "foundational ground" — the acoustic space itself speaking the interval between the choirs. Transmission is environmental-imitative: singers learn by listening to the resonant response of the room.

### 8. Relationship to neighboring systems
Shares with **Bulgarian women's choir** the close-interval choral harmony and the gradually-descending phrase endings. Shares with **Arabic takht maqam** the microtonal inflection as obligatory grammar. Shares with **Tuvan khoomei** the inharmonic spectral pitch material. The unique synthesis: *nested antiphonal call-response in an inharmonic non-octave scale, where silence between exchanges is the foundational ground and phrase-closure is a collective downward slide*.

### 9. Audio specification

```json
{
  "duration_seconds": 84.9,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 130,
    "pitches": [
      1.0,
      2.03,
      2.97,
      4.11,
      5.04,
      6.08,
      7.03,
      8.15,
      9.12,
      10.24
    ],
    "octave_repeats": false,
    "inflection_rules": [
      {
        "pitch_index": 0,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      },
      {
        "pitch_index": 1,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      },
      {
        "pitch_index": 2,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      },
      {
        "pitch_index": 3,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      },
      {
        "pitch_index": 4,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      },
      {
        "pitch_index": 5,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      },
      {
        "pitch_index": 6,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      },
      {
        "pitch_index": 7,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      },
      {
        "pitch_index": 8,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      },
      {
        "pitch_index": 9,
        "inflection_cents_range": [
          -55,
          0
        ],
        "direction": "down"
      }
    ]
  },
  "rhythm_system": {
    "type": "additive",
    "groupings": [
      5,
      4
    ],
    "base_unit_ms": 300
  },
  "voices": [
    {
      "name": "L_low",
      "timbre": "vocal_male_low",
      "pitch_indices": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7
      ],
      "rhythm_role": "sustained_drone",
      "amplitude": 0.7,
      "spatial_position": [
        -0.7,
        0.1
      ]
    },
    {
      "name": "L_reed",
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
        8
      ],
      "rhythm_role": "sustained_drone",
      "amplitude": 0.6,
      "spatial_position": [
        -0.55,
        0.2
      ]
    },
    {
      "name": "L_bow",
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
        8
      ],
      "rhythm_role": "sustained_drone",
      "amplitude": 0.55,
      "spatial_position": [
        -0.65,
        -0.05
      ]
    },
    {
      "name": "R_high",
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
        9
      ],
      "rhythm_role": "sustained_drone",
      "amplitude": 0.7,
      "spatial_position": [
        0.7,
        0.15
      ]
    },
    {
      "name": "R_flute",
      "timbre": "bamboo_flute",
      "pitch_indices": [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
      ],
      "rhythm_role": "sustained_drone",
      "amplitude": 0.6,
      "spatial_position": [
        0.55,
        0.2
      ]
    },
    {
      "name": "R_bow",
      "timbre": "bowed_string",
      "pitch_indices": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
      ],
      "rhythm_role": "sustained_drone",
      "amplitude": 0.55,
      "spatial_position": [
        0.6,
        0.0
      ]
    }
  ],
  "form": {
    "arc_type": "through_composed",
    "sections": [
      {
        "name": "movement_I_exposition",
        "start_seconds": 0,
        "duration_seconds": 22,
        "character": "three call-response exchanges, silences between",
        "chord_tones": [
          0,
          2,
          4
        ]
      },
      {
        "name": "movement_II_development",
        "start_seconds": 25,
        "duration_seconds": 33,
        "character": "nested calls within calls, expanding registers",
        "chord_tones": [
          0,
          3,
          6
        ]
      },
      {
        "name": "movement_III_resolution",
        "start_seconds": 62,
        "duration_seconds": 18,
        "character": "converging answers, final unison on home",
        "chord_tones": [
          0
        ]
      }
    ]
  },
  "ornamentation": {
    "density": 0.85,
    "rule": "Obligatory structural ornament: every sustained chord descends 40-70 cents over its final third ('morendo'). The descent is not expressive \u2014 it is a required phrase-closure. All voices descend together."
  },
  "auto_pedal": false,
  "events": [
    {
      "t": 1.0,
      "voice": "L_low",
      "pitch_index": 0,
      "duration_seconds": 2.4,
      "amplitude": 0.7
    },
    {
      "t": 1.0,
      "voice": "L_reed",
      "pitch_index": 2,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 1.0,
      "voice": "L_bow",
      "pitch_index": 4,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 5.4,
      "voice": "R_high",
      "pitch_index": 1,
      "duration_seconds": 2.4,
      "amplitude": 0.7
    },
    {
      "t": 5.4,
      "voice": "R_flute",
      "pitch_index": 3,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 5.4,
      "voice": "R_bow",
      "pitch_index": 5,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 9.8,
      "voice": "L_low",
      "pitch_index": 0,
      "duration_seconds": 2.4,
      "amplitude": 0.7
    },
    {
      "t": 9.8,
      "voice": "L_reed",
      "pitch_index": 3,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 9.8,
      "voice": "L_bow",
      "pitch_index": 5,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 14.2,
      "voice": "R_high",
      "pitch_index": 2,
      "duration_seconds": 2.4,
      "amplitude": 0.7
    },
    {
      "t": 14.2,
      "voice": "R_flute",
      "pitch_index": 4,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 14.2,
      "voice": "R_bow",
      "pitch_index": 6,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 18.6,
      "voice": "L_low",
      "pitch_index": 1,
      "duration_seconds": 2.4,
      "amplitude": 0.7
    },
    {
      "t": 18.6,
      "voice": "L_reed",
      "pitch_index": 2,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 18.6,
      "voice": "L_bow",
      "pitch_index": 4,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 23.0,
      "voice": "R_high",
      "pitch_index": 3,
      "duration_seconds": 2.4,
      "amplitude": 0.7
    },
    {
      "t": 23.0,
      "voice": "R_flute",
      "pitch_index": 5,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 23.0,
      "voice": "R_bow",
      "pitch_index": 7,
      "duration_seconds": 2.4,
      "amplitude": 0.6
    },
    {
      "t": 25.0,
      "voice": "L_low",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.65
    },
    {
      "t": 25.0,
      "voice": "L_reed",
      "pitch_index": 2,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 25.0,
      "voice": "L_bow",
      "pitch_index": 5,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 27.2,
      "voice": "L_low",
      "pitch_index": 1,
      "duration_seconds": 1.2,
      "amplitude": 0.55
    },
    {
      "t": 27.2,
      "voice": "L_reed",
      "pitch_index": 3,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 27.2,
      "voice": "L_bow",
      "pitch_index": 5,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 28.5,
      "voice": "L_low",
      "pitch_index": 2,
      "duration_seconds": 1.2,
      "amplitude": 0.55
    },
    {
      "t": 28.5,
      "voice": "L_reed",
      "pitch_index": 4,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 28.5,
      "voice": "L_bow",
      "pitch_index": 6,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 30.3,
      "voice": "R_high",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.7
    },
    {
      "t": 30.3,
      "voice": "R_flute",
      "pitch_index": 3,
      "duration_seconds": 3.0,
      "amplitude": 0.6
    },
    {
      "t": 30.3,
      "voice": "R_bow",
      "pitch_index": 6,
      "duration_seconds": 3.0,
      "amplitude": 0.6
    },
    {
      "t": 32.5,
      "voice": "R_high",
      "pitch_index": 1,
      "duration_seconds": 1.2,
      "amplitude": 0.58
    },
    {
      "t": 32.5,
      "voice": "R_flute",
      "pitch_index": 4,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 32.5,
      "voice": "R_bow",
      "pitch_index": 6,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 33.8,
      "voice": "R_high",
      "pitch_index": 2,
      "duration_seconds": 1.2,
      "amplitude": 0.58
    },
    {
      "t": 33.8,
      "voice": "R_flute",
      "pitch_index": 5,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 33.8,
      "voice": "R_bow",
      "pitch_index": 7,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 35.8,
      "voice": "L_low",
      "pitch_index": 1,
      "duration_seconds": 3.0,
      "amplitude": 0.65
    },
    {
      "t": 35.8,
      "voice": "L_reed",
      "pitch_index": 4,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 35.8,
      "voice": "L_bow",
      "pitch_index": 6,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 38.0,
      "voice": "L_low",
      "pitch_index": 2,
      "duration_seconds": 1.2,
      "amplitude": 0.55
    },
    {
      "t": 38.0,
      "voice": "L_reed",
      "pitch_index": 5,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 38.0,
      "voice": "L_bow",
      "pitch_index": 7,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 39.3,
      "voice": "L_low",
      "pitch_index": 3,
      "duration_seconds": 1.2,
      "amplitude": 0.55
    },
    {
      "t": 39.3,
      "voice": "L_reed",
      "pitch_index": 6,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 39.3,
      "voice": "L_bow",
      "pitch_index": 8,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 41.1,
      "voice": "R_high",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.7
    },
    {
      "t": 41.1,
      "voice": "R_flute",
      "pitch_index": 3,
      "duration_seconds": 3.0,
      "amplitude": 0.6
    },
    {
      "t": 41.1,
      "voice": "R_bow",
      "pitch_index": 7,
      "duration_seconds": 3.0,
      "amplitude": 0.6
    },
    {
      "t": 43.3,
      "voice": "R_high",
      "pitch_index": 1,
      "duration_seconds": 1.2,
      "amplitude": 0.58
    },
    {
      "t": 43.3,
      "voice": "R_flute",
      "pitch_index": 4,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 43.3,
      "voice": "R_bow",
      "pitch_index": 8,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 44.6,
      "voice": "R_high",
      "pitch_index": 2,
      "duration_seconds": 1.2,
      "amplitude": 0.58
    },
    {
      "t": 44.6,
      "voice": "R_flute",
      "pitch_index": 5,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 44.6,
      "voice": "R_bow",
      "pitch_index": 9,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 46.6,
      "voice": "L_low",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.65
    },
    {
      "t": 46.6,
      "voice": "L_reed",
      "pitch_index": 3,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 46.6,
      "voice": "L_bow",
      "pitch_index": 7,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 48.8,
      "voice": "L_low",
      "pitch_index": 1,
      "duration_seconds": 1.2,
      "amplitude": 0.55
    },
    {
      "t": 48.8,
      "voice": "L_reed",
      "pitch_index": 4,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 48.8,
      "voice": "L_bow",
      "pitch_index": 8,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 50.1,
      "voice": "L_low",
      "pitch_index": 2,
      "duration_seconds": 1.2,
      "amplitude": 0.55
    },
    {
      "t": 50.1,
      "voice": "L_reed",
      "pitch_index": 5,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 50.1,
      "voice": "L_bow",
      "pitch_index": 9,
      "duration_seconds": 1.2,
      "amplitude": 0.5
    },
    {
      "t": 51.9,
      "voice": "R_high",
      "pitch_index": 3,
      "duration_seconds": 3.0,
      "amplitude": 0.7
    },
    {
      "t": 51.9,
      "voice": "R_flute",
      "pitch_index": 6,
      "duration_seconds": 3.0,
      "amplitude": 0.6
    },
    {
      "t": 51.9,
      "voice": "R_bow",
      "pitch_index": 9,
      "duration_seconds": 3.0,
      "amplitude": 0.6
    },
    {
      "t": 54.1,
      "voice": "R_high",
      "pitch_index": 4,
      "duration_seconds": 1.2,
      "amplitude": 0.58
    },
    {
      "t": 54.1,
      "voice": "R_flute",
      "pitch_index": 7,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 54.1,
      "voice": "R_bow",
      "pitch_index": 9,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 55.4,
      "voice": "R_high",
      "pitch_index": 5,
      "duration_seconds": 1.2,
      "amplitude": 0.58
    },
    {
      "t": 55.4,
      "voice": "R_flute",
      "pitch_index": 8,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 55.4,
      "voice": "R_bow",
      "pitch_index": 9,
      "duration_seconds": 1.2,
      "amplitude": 0.52
    },
    {
      "t": 62.0,
      "voice": "L_low",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.6
    },
    {
      "t": 62.0,
      "voice": "L_reed",
      "pitch_index": 3,
      "duration_seconds": 3.0,
      "amplitude": 0.5
    },
    {
      "t": 62.0,
      "voice": "L_bow",
      "pitch_index": 5,
      "duration_seconds": 3.0,
      "amplitude": 0.5
    },
    {
      "t": 63.8,
      "voice": "R_high",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.65
    },
    {
      "t": 63.8,
      "voice": "R_flute",
      "pitch_index": 3,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 63.8,
      "voice": "R_bow",
      "pitch_index": 5,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 67.3,
      "voice": "L_low",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.6
    },
    {
      "t": 67.3,
      "voice": "L_reed",
      "pitch_index": 2,
      "duration_seconds": 3.0,
      "amplitude": 0.5
    },
    {
      "t": 67.3,
      "voice": "L_bow",
      "pitch_index": 4,
      "duration_seconds": 3.0,
      "amplitude": 0.5
    },
    {
      "t": 69.1,
      "voice": "R_high",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.65
    },
    {
      "t": 69.1,
      "voice": "R_flute",
      "pitch_index": 2,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 69.1,
      "voice": "R_bow",
      "pitch_index": 4,
      "duration_seconds": 3.0,
      "amplitude": 0.55
    },
    {
      "t": 72.6,
      "voice": "L_low",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.6
    },
    {
      "t": 74.4,
      "voice": "R_high",
      "pitch_index": 0,
      "duration_seconds": 3.0,
      "amplitude": 0.65
    },
    {
      "t": 77.9,
      "voice": "L_low",
      "pitch_index": 0,
      "duration_seconds": 5.0,
      "amplitude": 0.5
    },
    {
      "t": 77.9,
      "voice": "L_reed",
      "pitch_index": 0,
      "duration_seconds": 5.0,
      "amplitude": 0.45
    },
    {
      "t": 77.9,
      "voice": "L_bow",
      "pitch_index": 0,
      "duration_seconds": 5.0,
      "amplitude": 0.45
    },
    {
      "t": 77.9,
      "voice": "R_high",
      "pitch_index": 0,
      "duration_seconds": 5.0,
      "amplitude": 0.55
    },
    {
      "t": 77.9,
      "voice": "R_flute",
      "pitch_index": 0,
      "duration_seconds": 5.0,
      "amplitude": 0.5
    },
    {
      "t": 77.9,
      "voice": "R_bow",
      "pitch_index": 0,
      "duration_seconds": 5.0,
      "amplitude": 0.45
    }
  ]
}
```

### 10. Field note
The piece is not heard; it is listened *to*. The silences are not pauses — they are where the room says back what the choir has just sung, slightly changed.
