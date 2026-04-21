# Example Expedition — Reference Output

This is a worked example of the field-note format a model should produce when given an expedition prompt. Use this as the format reference, not as a template to copy parameters from. The coordinates below are hypothetical.

---

## Input that would produce this output

EXPEDITION #001
Date: 2026-04-21
Continuous: {pitch_density: 0.20, microtonality_degree: 0.70, octave_equivalence: 0.20, interval_hierarchy: 0.40, pitch_flexibility: 0.60, metric_periodicity: 0.15, rhythmic_density: 0.35, polyrhythmic_complexity: 0.50, cycle_length: 0.40, tempo_stability: 0.25, piece_duration: 0.50, formal_repetition: 0.40, development_arc: 0.35, voice_count: 0.25, voice_independence: 0.60, drone_presence: 0.85, improvisation_degree: 0.70, ornament_density: 0.60}

Categorical: {tuning_basis: overtone_series, scale_topology: non_octave_repeating, rhythmic_structure: breath_based, formal_type: cyclical_return, texture_type: drone_based, ornament_grammar: obligatory_structural, transmission_mode: oral_only, ensemble_topology: interlocking_parts, social_function: contemplative_personal, listener_role: ritual_participant, silence_treatment: structural_punctuation, temporal_framing: event_duration}

Curiosity score: 0.58

Neighbors:
- Gyütö Tantric Throat Chant (distance 0.51) — shares overtone_series, non_octave_repeating, drone_based. Diverges: pulse_free rather than breath_based; unison ensemble rather than interlocking.
- Tuvan Khoomei (distance 0.56) — shares overtone series, non-octave, drone. Diverges: solo rather than ensemble; isochronous metric rather than breath-based.
- Central African Horn Ensemble (distance 0.68) — shares interlocking_parts, polyphonic voice_independence. Diverges: pitched rather than overtone-series; isochronous rather than breath-based.

---

## Output

### 1. System name
Interlocking Overtone Respiration

### 2. Pitch organization
The system operates on the natural overtone series above a single reference fundamental of approximately 73 Hz (a low vocal fundamental accessible to trained male voices). Accessible overtones are partials 4 through 14 — pitches derived by multiplying the fundamental by small integers. Specifically: 4× (294 Hz), 5× (367), 6× (441), 7× (515), 8× (588), 9× (661), 10× (735), 11× (809), 12× (882), 13× (956), 14× (1029).

Pitches do not repeat at 2:1 — the system is genuinely non-octave. The 4× and 8× partials are exactly an octave apart but behave as distinct structural pitches, not equivalents. Partials 7, 11, and 13 are the most audibly "foreign" to a Western ear and function as the melodic pivots.

Interval hierarchy is moderate. The fundamental (1×) and partial 3 (actually sung below the 4th partial as a faint throat resonance) serve as the foundational pair. Partials 6 and 8 are common landing points. Partials 11 and 13 are always passing.

### 3. Rhythmic organization
There is no pulse. Time is measured in **breath-units** — each performer's inhalation–exhalation cycle serves as their local clock. A typical breath is 4–9 seconds. With 4–8 performers, breath cycles stagger: at any moment, some performers are mid-phrase while others are mid-inhalation. Events occur at breath transitions — the moment a performer begins or ends a sustained overtone.

Ensemble coordination works through a **continuity rule**: the fundamental must never drop below two voices sustaining it. When a performer needs to inhale, they signal (a small throat clearing or a raised finger) and another performer holds the fundamental through the gap. This rule creates emergent polyrhythm: the interlocking of 4–8 independent breath cycles, constrained only by the continuity rule, produces irregular wave patterns that never repeat identically.

### 4. Formal structure
Pieces are organized as **respiratory waves**. Each wave begins with a single performer sounding the fundamental, followed by gradual accumulation as other performers enter on overtones of their choice. The wave reaches peak density (all performers sounding) for a held interval — 20–40 seconds — before performers begin dropping out one by one, leaving a single fundamental. A breath of collective silence follows. Then the next wave begins.

A full piece is 5–9 waves, total duration 15–30 minutes. Waves are not identical — they vary in which overtones are emphasized, in peak density, and in how quickly they build and dissolve. The arc across a full piece is gentle: early waves sparser, middle waves denser, final waves returning to sparseness. No climax.

### 5. Texture and voicing
Drone-based with interlocking overtone voices. The fundamental drone is always present (by the continuity rule) but it is never sung by the same performer continuously — it is a collectively maintained pitch, passed between voices. Above the drone, each performer chooses their own overtone melody within the available partials.

Voices are independent in pitch choice but constrained in density: performers avoid producing the same overtone simultaneously. When two performers find themselves on the same partial, one shifts within two breaths. This anti-coincidence rule turns the ensemble into a slowly rotating distribution of pitches across the overtone palette.

### 6. Ornament and inflection
Ornament is obligatory. Every sustained overtone receives **breath-pressure inflection**: a micro-variation in laryngeal pressure that causes the overtone to waver 10–40 cents. Heavier inflection is used for partials 7, 11, and 13 (the structurally foreign partials). Lighter inflection is used for partials 4, 5, 6, 8. A held overtone without inflection is considered incomplete.

A second obligatory ornament is the **transition slide**: when moving between overtones, the performer slides audibly through intermediate partials rather than jumping. This slide is what makes the ensemble texture feel "woven" rather than chordal.

### 7. Performance context
The system is contemplative — performers cultivate it for internal practice as much as external listening. Listeners, if present, participate by sitting inside the ensemble's circle and breathing at whatever rate suits them; the irregular wave structure makes passive listening difficult and drifting attention expected.

Transmission is oral. The continuity rule, the anti-coincidence rule, and the two ornament requirements are taught by apprenticeship with experienced practitioners — there is no notation. A performer is considered trained when they can sustain the fundamental through another's inhalation without the collective feeling it as a rupture.

### 8. Relationship to neighboring systems
The system inherits its **pitch basis** from Tuvan khoomei and Gyütö tantric chant — both draw on the overtone series above a low vocal fundamental. It inherits its **interlocking ensemble structure** from Central African horn ensembles, where each performer sounds a limited pitch set and melody emerges from the interlocking.

It diverges from Gyütö by being pulsed — but pulsed by breath, not by meter. It diverges from khoomei by being ensemble-based and by treating the ensemble as the clock. It diverges from the Central African horn ensemble by substituting the overtone series for a tuned pitch set, and by replacing isochronous meter with staggered respiration.

The genuinely novel parameter is the **continuity rule** — the constraint that the fundamental must be collectively sustained. No known tradition uses this as a structural requirement, though it is an emergent property of some sustained-tone practices.

### 9. Audio specification

```json
{
  "duration_seconds": 75,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 73,
    "pitches": [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "octave_repeats": false,
    "inflection_rules": [
      {"pitch_index": 0, "inflection_cents_range": [-8, 8], "direction": "both"},
      {"pitch_index": 4, "inflection_cents_range": [-40, 40], "direction": "both"},
      {"pitch_index": 8, "inflection_cents_range": [-40, 40], "direction": "both"},
      {"pitch_index": 10, "inflection_cents_range": [-40, 40], "direction": "both"},
      {"pitch_index": 1, "inflection_cents_range": [-15, 15], "direction": "both"},
      {"pitch_index": 2, "inflection_cents_range": [-15, 15], "direction": "both"},
      {"pitch_index": 3, "inflection_cents_range": [-15, 15], "direction": "both"},
      {"pitch_index": 5, "inflection_cents_range": [-15, 15], "direction": "both"}
    ]
  },
  "rhythm_system": {
    "type": "breath_based",
    "breath_count": 32,
    "breath_duration_range_seconds": [4.0, 9.0],
    "between_breaths_seconds": [0.4, 1.2]
  },
  "voices": [
    {"name": "v1", "timbre": "vocal_male_low", "pitch_indices": [0], "rhythm_role": "sustained_drone", "amplitude": 0.6, "spatial_position": [-0.6, 0.2], "active_sections": ["wave_1", "wave_2", "wave_3"]},
    {"name": "v2", "timbre": "vocal_male_low", "pitch_indices": [0, 3, 4, 6], "rhythm_role": "breath_phrase", "amplitude": 0.65, "spatial_position": [-0.2, -0.1], "active_sections": ["wave_1", "wave_2", "wave_3"]},
    {"name": "v3", "timbre": "vocal_male_low", "pitch_indices": [2, 4, 6, 8, 10], "rhythm_role": "breath_phrase", "amplitude": 0.6, "spatial_position": [0.2, 0.3], "active_sections": ["wave_2", "wave_3"]},
    {"name": "v4", "timbre": "vocal_male_low", "pitch_indices": [1, 3, 5, 7, 9, 11], "rhythm_role": "breath_phrase", "amplitude": 0.55, "spatial_position": [0.6, -0.2], "active_sections": ["wave_2"]}
  ],
  "form": {
    "arc_type": "cyclical",
    "sections": [
      {"name": "wave_1", "start_seconds": 0, "duration_seconds": 18, "character": "single fundamental, two overtones enter"},
      {"name": "silence_1", "start_seconds": 18, "duration_seconds": 2, "character": "collective inhalation"},
      {"name": "wave_2", "start_seconds": 20, "duration_seconds": 28, "character": "full four-voice density, rotating overtones"},
      {"name": "silence_2", "start_seconds": 48, "duration_seconds": 2, "character": "collective inhalation"},
      {"name": "wave_3", "start_seconds": 50, "duration_seconds": 25, "character": "two voices remaining, fundamental re-exposed"}
    ]
  },
  "ornamentation": {
    "density": 0.6,
    "rule": "Every overtone sustained longer than 1.5 seconds receives breath-pressure inflection within the partial-specific cents range. Transitions between overtones slide through intermediate partials rather than jumping."
  }
}
```

### 10. Field note
On the first listening, the most striking thing is that the fundamental never stops — even as individual voices come and go, a low tone runs under everything, carried like a handoff between runners in a relay.
