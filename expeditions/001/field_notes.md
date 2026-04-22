# Expedition 001

### 1. System name
Nested Solitary Marking

### 2. Pitch organization
A stretched-tuned idiophone with twelve pitches distributed aperiodically across a range of roughly three and a half octaves above a fundamental of 110 Hz. Tuning is derived by taking the natural harmonic series and applying a logarithmic stretch: partial n is multiplied by (1 + 0.06 · log(n)), producing intervals that widen progressively with register. The ratios are 1.00, 2.08, 3.20, 4.33, 5.48, 6.65, 7.82, 9.00, 10.19, 11.38, 12.58, 13.79 — neither octave-equivalent nor periodic at any other interval. Interval hierarchy is strong: the fundamental (ratio 1) anchors everything; the third partial at ratio 3.20 functions as a secondary magnetic pitch. The remaining ten pitches are passing — each is reachable from the fundamental but none sets up a stable relationship of its own.

### 3. Rhythmic organization
Strikes land only on positions within a fixed irrational grid. The grid is computed from the inverse-golden-ratio series: for a piece of duration D, eligible strike moments are at D · (1 − φ⁻ⁿ) for n = 1, 2, 3, …, producing accumulating positions that approach D but never reach it. The grid is mathematically strict (metric periodicity is high, the positions are exact); but the positions are not isochronous, so tempo feels unstable. The performer chooses, at each eligible moment, whether to strike or to withhold. The result is a sparse rhythmic density with maximal polyrhythmic complexity: the grid itself contains multiple nested proportional strata.

### 4. Formal structure
Nested hierarchical. A full work consists of five macro-cycles stacked sequentially; each macro-cycle contains the full golden-series grid; within each macro-cycle, the performer may treat any single grid-eligible moment as the seed of a compressed micro-cycle, inserting a smaller-scale structure at that point. Pieces are typically 45–90 minutes. The macro-arc builds then dissipates — middle cycles are most dense, outer cycles sparse. Openings and endings fade into the silence of the underlying task.

### 5. Texture and voicing
Solo performer, single instrument. The stretched tuning causes sustained strikes to develop audible beating between adjacent partials when two pitches overlap; these beating patterns function as a kind of unintended drone, never foundational but always faintly present.

### 6. Ornament and inflection
Ornament is decorative-optional. The performer may dampen a strike before its natural decay, or immediately double it at the same pitch to produce a compound attack. Neither is required for idiomatic performance.

### 7. Performance context
The music is bound to a long physical task — an all-day repair, a boundary walk, a field-tending cycle. The performer is simultaneously the listener; no external audience is intended. The music structures the performer's attention through the day. Patterns are learned from recorded references rather than from teachers — the system emerged in parallel to recording technology and cannot easily exist without it.

### 8. Relationship to neighboring systems
Sits closest to IDM/glitch in its polyrhythmic proportionality and recorded-reference transmission, but diverges in being solo, acoustic, and task-bound rather than studio-algorithmic. Shares the low rhythmic density and ritual-participant framing of Hasidic nigun, but replaces the communal vocal climax with solitary timekeeping. Shares Noh theater's structural use of silence, but where Noh's silences frame a narrative climax, here silences are durationally equal to sounds and no narrative is underway. The unique combination is: *a solo fractal grid bound to slow manual labor*.

### 9. Audio specification

```json
{
  "duration_seconds": 75,
  "pitch_system": {
    "encoding": "ratio",
    "reference_hz": 110,
    "pitches": [1.000, 2.083, 3.198, 4.333, 5.483, 6.645, 7.817, 8.998, 10.186, 11.382, 12.583, 13.789],
    "octave_repeats": false
  },
  "rhythm_system": {
    "type": "indeterminate_proportional",
    "notation_note": "Strikes at D*(1 - phi^-n) for n = 1..13 within each macro-cycle; performer chooses which moments to play."
  },
  "voices": [
    {"name": "marker", "timbre": "struck_metal", "pitch_indices": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "rhythm_role": "ritual_punctuation", "amplitude": 0.75, "spatial_position": [0.0, 0.0]}
  ],
  "form": {
    "arc_type": "nested_hierarchical",
    "sections": [
      {"name": "cycle_1_sparse", "start_seconds": 0, "duration_seconds": 15, "character": "opening, only lowest partials, wide gaps"},
      {"name": "cycle_2_building", "start_seconds": 15, "duration_seconds": 20, "character": "upper partials entering, gaps shortening"},
      {"name": "cycle_3_dense", "start_seconds": 35, "duration_seconds": 15, "character": "full stretched-partial range, micro-cycles inserted"},
      {"name": "cycle_4_receding", "start_seconds": 50, "duration_seconds": 15, "character": "upper partials withdrawing, gaps lengthening"},
      {"name": "cycle_5_closing", "start_seconds": 65, "duration_seconds": 10, "character": "fundamental + partial 2 only, fade into the task"}
    ]
  },
  "events": [
    {"t": 2.8, "voice": "marker", "pitch_index": 0, "duration_seconds": 6.5, "amplitude": 0.8},
    {"t": 9.5, "voice": "marker", "pitch_index": 2, "duration_seconds": 4.2, "amplitude": 0.6},
    {"t": 15.4, "voice": "marker", "pitch_index": 1, "duration_seconds": 5.0, "amplitude": 0.7},
    {"t": 19.8, "voice": "marker", "pitch_index": 4, "duration_seconds": 3.5, "amplitude": 0.65},
    {"t": 22.9, "voice": "marker", "pitch_index": 0, "duration_seconds": 4.0, "amplitude": 0.75},
    {"t": 26.5, "voice": "marker", "pitch_index": 6, "duration_seconds": 2.8, "amplitude": 0.6},
    {"t": 28.8, "voice": "marker", "pitch_index": 2, "duration_seconds": 3.2, "amplitude": 0.7},
    {"t": 31.6, "voice": "marker", "pitch_index": 8, "duration_seconds": 2.4, "amplitude": 0.55},
    {"t": 35.3, "voice": "marker", "pitch_index": 3, "duration_seconds": 2.8, "amplitude": 0.8},
    {"t": 37.4, "voice": "marker", "pitch_index": 10, "duration_seconds": 1.9, "amplitude": 0.5},
    {"t": 38.9, "voice": "marker", "pitch_index": 5, "duration_seconds": 2.4, "amplitude": 0.7},
    {"t": 40.8, "voice": "marker", "pitch_index": 11, "duration_seconds": 1.8, "amplitude": 0.5},
    {"t": 42.2, "voice": "marker", "pitch_index": 7, "duration_seconds": 2.2, "amplitude": 0.65},
    {"t": 44.1, "voice": "marker", "pitch_index": 1, "duration_seconds": 3.2, "amplitude": 0.75},
    {"t": 46.8, "voice": "marker", "pitch_index": 9, "duration_seconds": 1.7, "amplitude": 0.55},
    {"t": 48.3, "voice": "marker", "pitch_index": 0, "duration_seconds": 3.8, "amplitude": 0.85},
    {"t": 52.9, "voice": "marker", "pitch_index": 3, "duration_seconds": 3.0, "amplitude": 0.65},
    {"t": 56.4, "voice": "marker", "pitch_index": 2, "duration_seconds": 3.5, "amplitude": 0.7},
    {"t": 61.2, "voice": "marker", "pitch_index": 1, "duration_seconds": 4.0, "amplitude": 0.6},
    {"t": 67.0, "voice": "marker", "pitch_index": 0, "duration_seconds": 5.5, "amplitude": 0.55}
  ]
}
```

### 10. Field note
The strikes do not feel measured — they feel consulted, as though the performer were asking an instrument what time it is and receiving, each time, a slightly different answer.
