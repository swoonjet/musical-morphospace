# Expedition 006

### 1. System name
Environmental Theme-Variation

### 2. Pitch organization
A two-octave Pythagorean diatonic scale above a 220 Hz tonic. The seven pitches of the octave are derived from stacked perfect fifths and reduced: 1, 9/8, 81/64, 4/3, 3/2, 27/16, 243/128, spanning the octave to 2. The scale is near-diatonic to a Western ear but with slightly wide major thirds (~408 cents rather than 386). Interval hierarchy is strong: the tonic and the perfect fifth are structural pillars; the fourth is a secondary landing. Pitch flexibility is moderate — sustained notes receive microtonal inflection (30–50 cents at onset settling toward the target pitch) as the system's signature ornament. The scale is octave-repeating but the octave is not considered interchangeable — the upper-octave versions of each pitch are treated as distinct structural pitches with their own hierarchical roles.

### 3. Rhythmic organization
Environmentally synchronized. The ensemble's rhythmic flow is dictated by the pace of an environmental cue heard during the performance — a regularly dripping spring, a quiet wind pattern through an opening, a nearby bird-call at a certain hour. The ensemble listens and attaches its phrase-beginnings to the environmental cue. Metric periodicity is moderate (the cues themselves have pulse) but tempo_stability is low (the pulse drifts with the environment). Polyrhythmic complexity arises because each voice attaches to a different recurring cue, producing independent rhythmic strata that occasionally coincide.

### 4. Formal structure
Theme-and-variation with strong arc. A single melodic theme of 8–12 notes is stated cleanly at the opening. The body of a performance is a long sequence of variations — dozens to hundreds — each recasting the theme through a different technique: ornamented, inverted, fragmented, augmented, redistributed across voices. Variations build in complexity toward a middle peak, then simplify back toward a final plain restatement. Full performances run for hours; the longest are durational — the cycle ends when the environmental cue itself ends (the bird flies off, the spring runs out).

### 5. Texture and voicing
Four-voice polyphonic independent texture against a continuous tonic drone. The voices are: a lead melodic flute (the "theme voice"), a secondary plucked-string variation voice, a soft sustained-chord pad, and a sparse wooden striker that marks coincidences with the environmental cue. Each voice is rhythmically and melodically independent but all share the same underlying theme material.

### 6. Ornament and inflection
Microtonal inflection is core and obligatory. Every sustained note — from any voice — begins 30–50 cents below its target pitch and slides upward to the target over the first 100–200 ms. This is a fixed ornament of the system, not an expressive choice. The flute voice may additionally ornament with upward grace-notes and trills on structural pitches (tonic and fifth).

### 7. Performance context
The system is narrative: the variations tell a story through a specific recognized theme, and knowledgeable listeners follow the narrative across the sequence. Listeners are ritual participants — they sit or walk with the performers in proximity to the environmental cue for the duration of the performance. Transmission is notated-prescriptive: the theme and a large catalog of variation-techniques are preserved in written form (tablature plus interval-and-ornament notation), and performers study the catalog before a performance, but the order of variations is chosen at the time of performance to match the character of the cue.

### 8. Relationship to neighboring systems
Shares with Wagnerian opera the development-arc-across-a-long-form and prescriptive notation; shares with Western Romantic symphony the theme-and-variation formal lineage; shares with Carnatic RTP the ornament-density, the drone foundation, and the idea that the performance unfolds over a long span. Diverges from all three by binding the rhythmic organization to a real-time environmental sound, and by treating the listener as a ritual participant (co-present with the cue) rather than as an audience. The unique synthesis is: *Pythagorean-diatonic melody, environmentally paced, performed as narrative variation on a theme*.

### 9. Audio specification

```json
{
  "duration_seconds": 85,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 220,
    "pitches": [1.000, 1.125, 1.266, 1.333, 1.500, 1.688, 1.898, 2.000, 2.250, 2.531, 2.667, 3.000, 3.375, 3.797],
    "octave_repeats": true,
    "inflection_rules": [
      {"pitch_index": 0, "inflection_cents_range": [-35, 0], "direction": "up"},
      {"pitch_index": 2, "inflection_cents_range": [-35, 0], "direction": "up"},
      {"pitch_index": 4, "inflection_cents_range": [-35, 0], "direction": "up"},
      {"pitch_index": 7, "inflection_cents_range": [-35, 0], "direction": "up"},
      {"pitch_index": 9, "inflection_cents_range": [-35, 0], "direction": "up"},
      {"pitch_index": 11, "inflection_cents_range": [-35, 0], "direction": "up"}
    ]
  },
  "rhythm_system": {
    "type": "cyclical_nonmetric",
    "cycle_duration_seconds": 14,
    "event_density_per_cycle": 12,
    "cycle_count": 6
  },
  "voices": [
    {"name": "theme_flute", "timbre": "bamboo_flute", "pitch_indices": [5, 6, 7, 8, 9, 10, 11, 12], "rhythm_role": "melodic_lead", "amplitude": 0.75, "spatial_position": [0.0, 0.3]},
    {"name": "variation_gut", "timbre": "plucked_gut", "pitch_indices": [2, 3, 4, 5, 6, 7, 8, 9], "rhythm_role": "ornamental", "amplitude": 0.55, "spatial_position": [-0.4, -0.1]},
    {"name": "drone_pad", "timbre": "soft_pad", "pitch_indices": [0], "rhythm_role": "sustained_drone", "amplitude": 0.38, "spatial_position": [0.0, -0.2]},
    {"name": "env_striker", "timbre": "low_wood", "pitch_indices": [0, 4], "rhythm_role": "percussive", "amplitude": 0.45, "spatial_position": [0.5, 0.0]}
  ],
  "form": {
    "arc_type": "arc_buildup",
    "sections": [
      {"name": "theme_statement", "start_seconds": 0, "duration_seconds": 14, "character": "plain theme on flute over drone"},
      {"name": "variation_1_ornamented", "start_seconds": 14, "duration_seconds": 15, "character": "flute ornaments theme; gut begins tracing"},
      {"name": "variation_2_interleaved", "start_seconds": 29, "duration_seconds": 14, "character": "flute and gut interleave the theme"},
      {"name": "variation_3_dense", "start_seconds": 43, "duration_seconds": 14, "character": "peak density; env-striker emphasizes coincidences"},
      {"name": "variation_4_receding", "start_seconds": 57, "duration_seconds": 14, "character": "variation simplifies; gut voice withdraws"},
      {"name": "theme_return", "start_seconds": 71, "duration_seconds": 14, "character": "plain theme returns, flute alone over drone"}
    ]
  },
  "ornamentation": {
    "density": 0.75,
    "rule": "Every sustained note begins 30-50 cents below its target pitch and slides up over 100-200 ms. Flute may add upward grace-notes on tonic and fifth."
  }
}
```

### 10. Field note
The theme is the same each time it returns, but one hears it differently at the end — as though the environmental cue, by holding steady through the hour, had been the patient one all along.
