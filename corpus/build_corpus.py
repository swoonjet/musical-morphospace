"""
Build corpus.json from the 20 existing anchors + additional traditions.
Validates all traditions against the schema's hard coherence constraints before writing.

Usage: python3 build_corpus.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
from coherence import check, check_schema_values  # noqa: E402
ANCHORS_PATH = ROOT / "corpus" / "anchors.json"
SCHEMA_PATH = ROOT / "schema" / "schema.json"
OUT_PATH = ROOT / "corpus" / "corpus.json"

CONT_DIMS = [
    "pitch_density", "microtonality_degree", "octave_equivalence", "interval_hierarchy", "pitch_flexibility",
    "metric_periodicity", "rhythmic_density", "polyrhythmic_complexity", "cycle_length", "tempo_stability",
    "piece_duration", "formal_repetition", "development_arc",
    "voice_count", "voice_independence", "drone_presence",
    "improvisation_degree", "ornament_density",
]

CAT_DIMS = [
    "tuning_basis", "scale_topology", "rhythmic_structure", "formal_type",
    "texture_type", "ornament_grammar", "transmission_mode", "ensemble_topology",
    "social_function", "listener_role", "silence_treatment", "temporal_framing",
]


def T(id_, name, region, example, c, g, notes, anchor=False):
    """Compact tradition constructor. c = 18 continuous, g = 12 categorical."""
    assert len(c) == 18, f"{id_}: expected 18 continuous, got {len(c)}"
    assert len(g) == 12, f"{id_}: expected 12 categorical, got {len(g)}"
    return {
        "id": id_,
        "name": name,
        "region": region,
        "example": example,
        "is_anchor": anchor,
        "continuous": dict(zip(CONT_DIMS, c)),
        "categorical": dict(zip(CAT_DIMS, g)),
        "notes": notes,
    }


# Load existing anchors and flag them
with open(ANCHORS_PATH) as f:
    anchors_data = json.load(f)
anchors = []
for t in anchors_data["traditions"]:
    t["is_anchor"] = True
    anchors.append(t)


# ============================================================
# 60 additional traditions
# ============================================================

NEW = [
    # -------------------- Western art music --------------------
    T("bach_fugue", "Bach Fugue (Well-Tempered Clavier)", "Germany, 18th c.",
      "The Art of Fugue, BWV 846 fugue in C major",
      c=(0.16, 0.0, 1.0, 0.85, 0.25, 0.9, 0.7, 0.5, 0.25, 0.75, 0.2, 0.5, 0.7, 0.15, 0.95, 0.05, 0.02, 0.3),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "nested_hierarchical",
         "polyphonic_independent", "decorative_optional", "notated_prescriptive", "solo",
         "didactic_pedagogical", "evaluator_connoisseur", "structural_punctuation", "clock_time_bounded"),
      notes="Solo keyboard fugue — voice_count low because single instrument, but voice_independence near max (4 real voices). didactic_pedagogical because WTC is explicitly pedagogical but also cosmologically ordered."),

    T("mozart_piano_sonata", "Mozart Classical Piano Sonata", "Vienna, late 18th c.",
      "Piano Sonata K. 310 in A minor",
      c=(0.16, 0.0, 1.0, 0.8, 0.3, 0.9, 0.5, 0.2, 0.3, 0.7, 0.3, 0.55, 0.75, 0.05, 0.3, 0.05, 0.1, 0.35),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "sectional_contrasting",
         "homophonic", "decorative_optional", "notated_prescriptive", "solo",
         "entertainment_display", "passive_audience", "structural_punctuation", "clock_time_bounded"),
      notes="Calibrates mid-range Western tonal solo against symphony/Bach. Lower pitch_flexibility than Romantic era; lower ornament than Baroque ornament tradition would have."),

    T("wagner_ring_opera", "Wagnerian Opera (Music-Drama)", "Germany, mid-late 19th c.",
      "Der Ring des Nibelungen",
      c=(0.18, 0.05, 1.0, 0.8, 0.5, 0.65, 0.5, 0.45, 0.5, 0.4, 0.95, 0.25, 0.98, 0.85, 0.85, 0.15, 0.02, 0.4),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "through_composed_narrative",
         "polyphonic_independent", "decorative_optional", "notated_prescriptive", "soloist_with_accompaniment",
         "narrative_storytelling", "passive_audience", "structural_punctuation", "clock_time_bounded"),
      notes="piece_duration near max — 4 operas, ~15 hours. Leitmotif construction pushes development_arc very high. Voice_count large orchestra + singers."),

    T("schoenberg_twelve_tone", "Schoenberg 12-Tone Composition", "Vienna, 1920s-",
      "Pierrot Lunaire / Piano Concerto",
      c=(0.16, 0.0, 1.0, 0.05, 0.4, 0.6, 0.55, 0.5, 0.2, 0.5, 0.35, 0.15, 0.55, 0.4, 0.9, 0.05, 0.05, 0.3),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "through_composed_narrative",
         "polyphonic_independent", "decorative_optional", "notated_prescriptive", "unison_ensemble",
         "contemplative_personal", "evaluator_connoisseur", "structural_punctuation", "clock_time_bounded"),
      notes="interval_hierarchy near zero (all 12 tones equal by construction — a defining feature). Sprechstimme pushes pitch_flexibility modestly above Bach/Mozart."),

    T("cage_chance_operations", "Cage Chance-Operation Composition", "USA, 1950s",
      "Music of Changes; Atlas Eclipticalis",
      c=(0.2, 0.1, 0.7, 0.05, 0.35, 0.3, 0.35, 0.4, 0.1, 0.4, 0.45, 0.05, 0.15, 0.3, 0.85, 0.15, 0.1, 0.15),
      g=("equal_temperament", "octave_repeating", "indeterminate_proportional", "modular_combinatorial",
         "polyphonic_independent", "decorative_optional", "notated_prescriptive", "unison_ensemble",
         "contemplative_personal", "passive_audience", "equal_to_sound", "clock_time_bounded"),
      notes="Notated prescriptive (I-Ching derived scores) but content is chance-generated. development_arc near zero — anti-arc. silence_treatment=equal_to_sound is the Cage signature."),

    T("stockhausen_gruppen", "Stockhausen Gruppen (spatial composition)", "Germany, 1955-57",
      "Gruppen for three orchestras",
      c=(0.3, 0.25, 0.6, 0.1, 0.5, 0.5, 0.75, 0.95, 0.15, 0.45, 0.45, 0.1, 0.75, 0.9, 0.95, 0.1, 0.05, 0.4),
      g=("equal_temperament", "octave_repeating", "indeterminate_proportional", "through_composed_narrative",
         "polyphonic_independent", "decorative_optional", "notated_prescriptive", "spatially_distributed",
         "entertainment_display", "passive_audience", "structural_punctuation", "clock_time_bounded"),
      notes="Anchor for spatially_distributed ensemble_topology — three physically separated orchestras with independent conductors. Polyrhythmic_complexity near max from three tempo streams."),

    T("feldman_late_chamber", "Feldman Late Chamber Work", "USA, 1970s-80s",
      "For Samuel Beckett; Piano and String Quartet",
      c=(0.16, 0.05, 1.0, 0.15, 0.3, 0.4, 0.15, 0.2, 0.1, 0.4, 0.85, 0.4, 0.02, 0.3, 0.5, 0.3, 0.0, 0.1),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "static_contemplation",
         "polyphonic_independent", "forbidden", "notated_prescriptive", "unison_ensemble",
         "contemplative_personal", "passive_audience", "foundational_ground", "clock_time_bounded"),
      notes="piece_duration high (80 min+), rhythmic_density very low, development_arc near zero. static_contemplation is the canonical fit. ornament_grammar=forbidden (Feldman's bare surface)."),

    T("xenakis_stochastic", "Xenakis Stochastic Composition", "Greece/France, 1950s-70s",
      "Metastaseis; Pithoprakta",
      c=(0.8, 0.55, 0.2, 0.1, 0.6, 0.4, 0.9, 0.9, 0.1, 0.4, 0.3, 0.05, 0.8, 0.9, 0.9, 0.25, 0.02, 0.2),
      g=("equal_temperament", "octave_repeating", "indeterminate_proportional", "through_composed_narrative",
         "spectral_cloud", "decorative_optional", "notated_prescriptive", "unison_ensemble",
         "contemplative_personal", "passive_audience", "structural_punctuation", "clock_time_bounded"),
      notes="Mass sonic events generated by probability distributions. texture_type=spectral_cloud fits — glissando masses, stochastic clouds. pitch_density very high."),

    T("la_monte_young_drone", "La Monte Young Drone (Well-Tuned Piano)", "USA, 1960s-",
      "The Well-Tuned Piano; Dream House installations",
      c=(0.3, 0.95, 0.25, 0.95, 0.0, 0.2, 0.25, 0.1, 0.0, 0.15, 1.0, 0.4, 0.0, 0.1, 0.3, 1.0, 0.15, 0.05),
      g=("just_intonation", "non_octave_repeating", "indeterminate_proportional", "static_contemplation",
         "drone_based", "forbidden", "notated_skeletal", "solo",
         "contemplative_personal", "passive_audience", "foundational_ground", "indeterminate_open"),
      notes="Just-intonation extended to complex rational-ratio pitch grid. Well-Tuned Piano performances run 5+ hours. drone_presence absolute; piece_duration max. Anchor for contemporary drone art."),

    T("radigue_electronic_drone", "Éliane Radigue Electronic Drone", "France, 1970s-",
      "Trilogie de la Mort; Adnos series",
      c=(0.2, 0.7, 0.3, 0.5, 0.1, 0.1, 0.2, 0.1, 0.0, 0.3, 0.9, 0.2, 0.1, 0.05, 0.3, 1.0, 0.1, 0.05),
      g=("overtone_series", "non_octave_repeating", "pulse_free", "static_contemplation",
         "drone_based", "forbidden", "recorded_reference", "solo",
         "contemplative_personal", "passive_audience", "foundational_ground", "clock_time_bounded"),
      notes="ARP 2500 synthesizer drones. Recorded fixed works. Sits near La Monte Young but electronic transmission_mode and shorter piece_duration."),

    # -------------------- Western popular --------------------
    T("swing_big_band", "Swing-Era Big Band", "USA, 1930s-40s",
      "Duke Ellington Orchestra; Count Basie",
      c=(0.16, 0.1, 1.0, 0.7, 0.5, 0.95, 0.65, 0.45, 0.2, 0.9, 0.15, 0.8, 0.4, 0.55, 0.7, 0.05, 0.35, 0.5),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "sectional_contrasting",
         "homophonic", "improvisatory_expansive", "notated_prescriptive", "soloist_with_accompaniment",
         "entertainment_display", "passive_audience", "decorative_pause", "clock_time_bounded"),
      notes="Arranged sections + solo improvisation. Notated prescriptive arrangements + improvised solos — a hybrid the transmission_mode can't fully capture. Calibrates ensemble popular-music region."),

    T("bebop_combo", "Bebop Jazz Combo", "USA, 1940s",
      "Charlie Parker, Dizzy Gillespie quintets",
      c=(0.16, 0.1, 1.0, 0.5, 0.7, 0.9, 0.95, 0.5, 0.15, 0.85, 0.1, 0.5, 0.5, 0.2, 0.85, 0.1, 0.85, 0.65),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "theme_and_variation",
         "polyphonic_independent", "improvisatory_expansive", "recorded_reference", "soloist_with_accompaniment",
         "entertainment_display", "evaluator_connoisseur", "decorative_pause", "clock_time_bounded"),
      notes="Max rhythmic_density — bebop eighth-note phrase. Head-solos-head form. transmission_mode=recorded_reference because lineage is via recordings + transcription."),

    T("classic_rock_song", "Classic Rock Song", "UK/USA, 1960s-70s",
      "Beatles, Led Zeppelin",
      c=(0.12, 0.1, 1.0, 0.75, 0.45, 0.95, 0.6, 0.25, 0.1, 0.95, 0.1, 0.9, 0.55, 0.35, 0.5, 0.15, 0.25, 0.3),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "sectional_contrasting",
         "homophonic", "decorative_optional", "recorded_reference", "unison_ensemble",
         "entertainment_display", "passive_audience", "decorative_pause", "clock_time_bounded"),
      notes="Verse-chorus structure → formal_repetition high. Anchor for Western popular song format."),

    T("techno_four_on_floor", "Four-on-the-Floor Techno", "Detroit/Berlin, 1985-",
      "Jeff Mills; Berghain-era minimal techno",
      c=(0.08, 0.0, 1.0, 0.35, 0.0, 1.0, 0.85, 0.4, 0.1, 1.0, 0.5, 0.98, 0.4, 0.25, 0.7, 0.35, 0.1, 0.1),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "modular_combinatorial",
         "layered_ostinato", "forbidden", "recorded_reference", "solo",
         "trance_induction", "participatory_communal", "avoided", "event_duration"),
      notes="DJ-as-composer — solo ensemble_topology. Kick drum on every beat. Additive layer structure (modular_combinatorial). social_function=trance_induction through sustained repetition + physical dance."),

    T("eno_ambient", "Brian Eno Ambient", "UK, 1975-",
      "Music for Airports; Discreet Music",
      c=(0.12, 0.1, 1.0, 0.4, 0.2, 0.25, 0.1, 0.3, 0.2, 0.3, 0.7, 0.8, 0.1, 0.4, 0.6, 0.5, 0.15, 0.1),
      g=("equal_temperament", "octave_repeating", "indeterminate_proportional", "static_contemplation",
         "layered_ostinato", "forbidden", "recorded_reference", "solo",
         "environmental_dialogue", "environmental_coexistent", "foundational_ground", "clock_time_bounded"),
      notes="Eno's 'as ignorable as it is interesting.' listener_role=environmental_coexistent is the Eno invention. Tape-loop systems produce layered_ostinato without strict meter."),

    T("drone_metal", "Drone/Doom Metal (Sunn O))))", "USA, 1998-",
      "Monoliths & Dimensions",
      c=(0.1, 0.15, 0.9, 0.6, 0.35, 0.3, 0.2, 0.15, 0.0, 0.45, 0.6, 0.6, 0.25, 0.25, 0.3, 0.95, 0.2, 0.15),
      g=("equal_temperament", "octave_repeating", "indeterminate_proportional", "static_contemplation",
         "drone_based", "decorative_optional", "recorded_reference", "unison_ensemble",
         "contemplative_personal", "passive_audience", "foundational_ground", "event_duration"),
      notes="Extreme-volume distorted-guitar drone. Ritual-performance aesthetic but framed as art. drone_presence near max; pitch_flexibility from feedback/overtones."),

    T("hyperpop", "Hyperpop", "online scenes, 2015-",
      "100 gecs; SOPHIE",
      c=(0.18, 0.2, 1.0, 0.7, 0.65, 0.9, 1.0, 0.3, 0.05, 0.7, 0.08, 0.85, 0.75, 0.3, 0.55, 0.1, 0.15, 0.5),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "sectional_contrasting",
         "homophonic", "decorative_optional", "recorded_reference", "solo",
         "entertainment_display", "passive_audience", "avoided", "clock_time_bounded"),
      notes="Max rhythmic_density; pitched vocals heavily pitch-corrected and pitch_flexibility is ornamental rather than expressive. Piece_duration very short (2-3 min)."),

    T("idm_glitch", "IDM / Glitch", "UK/Japan, 1995-",
      "Autechre; Aphex Twin Drukqs; Oval",
      c=(0.2, 0.35, 0.7, 0.25, 0.5, 0.55, 0.95, 0.85, 0.12, 0.45, 0.3, 0.4, 0.35, 0.4, 0.8, 0.2, 0.3, 0.3),
      g=("equal_temperament", "octave_repeating", "indeterminate_proportional", "through_composed_narrative",
         "spectral_cloud", "decorative_optional", "recorded_reference", "solo",
         "contemplative_personal", "passive_audience", "decorative_pause", "clock_time_bounded"),
      notes="Algorithmic/granular manipulation. Polyrhythmic_complexity high from non-integer-ratio rhythmic events. Close to Cage + spectral lineage but electronic."),

    # -------------------- Western folk --------------------
    T("appalachian_old_time", "Appalachian Old-Time String Band", "USA, 19th-20th c.",
      "Tommy Jarrell; Round Peak style",
      c=(0.12, 0.1, 1.0, 0.7, 0.5, 0.95, 0.7, 0.2, 0.15, 0.9, 0.08, 0.95, 0.2, 0.3, 0.5, 0.1, 0.35, 0.35),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "cyclical_return",
         "heterophonic", "decorative_optional", "oral_only", "heterophonic_group",
         "work_coordination", "participatory_communal", "avoided", "event_duration"),
      notes="Fiddle + banjo + guitar playing variations of same tune simultaneously — heterophonic texture. Dance function drives metric stability. Short tunes (AABB form)."),

    T("irish_session", "Irish Session (trad. session playing)", "Ireland, 19th-20th c.",
      "Paddy Keenan; The Chieftains",
      c=(0.14, 0.15, 1.0, 0.7, 0.7, 0.95, 0.75, 0.25, 0.15, 0.9, 0.1, 0.95, 0.25, 0.45, 0.4, 0.05, 0.3, 0.7),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "cyclical_return",
         "heterophonic", "obligatory_structural", "oral_only", "heterophonic_group",
         "entertainment_display", "participatory_communal", "avoided", "event_duration"),
      notes="Ornamentation (rolls, cuts, crans) obligatory for idiomatic playing. Pitch_flexibility higher than Appalachian due to modal scale inflections. Pipes drone influence on just intonation."),

    T("sea_shanty", "Sea Shanty (work song)", "Atlantic maritime, 19th c.",
      "Shallow Brown; Boney",
      c=(0.08, 0.05, 1.0, 0.75, 0.3, 0.9, 0.35, 0.1, 0.15, 0.85, 0.08, 0.95, 0.15, 0.3, 0.15, 0.0, 0.05, 0.15),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "cyclical_return",
         "call_response", "decorative_optional", "oral_only", "call_response",
         "work_coordination", "participatory_communal", "avoided", "event_duration"),
      notes="Pure work_coordination — tempo matches task (hauling rhythm). Shantyman leads verse, crew answers chorus. Ends when work ends."),

    T("english_folk_ballad", "English Folk Ballad (Child ballad tradition)", "England, medieval-19th c.",
      "Tam Lin; Reynardine",
      c=(0.1, 0.1, 1.0, 0.75, 0.4, 0.7, 0.4, 0.0, 0.2, 0.85, 0.15, 0.85, 0.4, 0.05, 0.0, 0.0, 0.2, 0.3),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "theme_and_variation",
         "monophonic", "decorative_optional", "oral_only", "solo",
         "narrative_storytelling", "passive_audience", "decorative_pause", "event_duration"),
      notes="Solo narrative ballad, strophic. Calibrates 'unaccompanied folk song' against American solo blues (which has guitar)."),

    # -------------------- Indian / Pakistani --------------------
    T("qawwali", "Sufi Qawwali (Pakistan/India)", "Pakistan/North India",
      "Nusrat Fateh Ali Khan",
      c=(0.2, 0.4, 1.0, 0.9, 0.8, 0.85, 0.75, 0.3, 0.35, 0.85, 0.75, 0.7, 0.95, 0.35, 0.4, 0.7, 0.65, 0.85),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "arc_buildup",
         "drone_based", "obligatory_structural", "oral_only", "soloist_with_accompaniment",
         "trance_induction", "participatory_communal", "avoided", "event_duration"),
      notes="Anchor for trance_induction. Handclaps + harmonium + lead + chorus. Pieces accelerate to ecstatic climax over 20-40 min. Devotional but listener participation is central."),

    T("tabla_solo", "Tabla Solo (North Indian percussion)", "North India",
      "Zakir Hussain; Alla Rakha solo tabla",
      c=(0.05, 0.05, 0.7, 0.5, 0.4, 0.8, 0.98, 0.4, 0.6, 0.75, 0.55, 0.5, 0.7, 0.15, 0.3, 0.7, 0.8, 0.6),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "theme_and_variation",
         "drone_based", "obligatory_structural", "oral_only", "soloist_with_accompaniment",
         "didactic_pedagogical", "evaluator_connoisseur", "structural_punctuation", "event_duration"),
      notes="Tabla over sarangi/harmonium lehara drone. cycle_length moderate-high (often 16-beat teental). didactic because solos explicitly demonstrate compositions from the memorized tabla repertoire."),

    T("bollywood_filmi", "Bollywood Filmi Song (golden era)", "India, 1950s-70s",
      "R.D. Burman; Lata Mangeshkar",
      c=(0.17, 0.25, 1.0, 0.8, 0.75, 0.85, 0.55, 0.35, 0.2, 0.85, 0.08, 0.85, 0.4, 0.5, 0.55, 0.3, 0.15, 0.55),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "sectional_contrasting",
         "homophonic", "decorative_optional", "notated_prescriptive", "soloist_with_accompaniment",
         "entertainment_display", "passive_audience", "decorative_pause", "clock_time_bounded"),
      notes="Prescriptive orchestral arrangement + raga/ornament-inflected vocal melody. Calibrates 'Indian-influenced ensemble film song' against Western pop."),

    # -------------------- Middle East / Mediterranean --------------------
    T("turkish_classical_makam", "Turkish Classical Makam", "Ottoman/Turkey",
      "Tanburi Cemil Bey; fasıl repertoire",
      c=(0.3, 0.6, 1.0, 0.85, 0.7, 0.55, 0.45, 0.2, 0.3, 0.55, 0.55, 0.55, 0.6, 0.3, 0.4, 0.2, 0.55, 0.85),
      g=("just_intonation", "adaptive_contextual", "additive_metric", "sectional_contrasting",
         "heterophonic", "obligatory_structural", "notated_skeletal", "heterophonic_group",
         "contemplative_personal", "evaluator_connoisseur", "decorative_pause", "event_duration"),
      notes="Sibling to Arabic maqam and Persian dastgah. Longer usul rhythmic cycles (additive_metric, e.g. aksak 9/8). 53-tone Turkish theory → highest systematic pitch_density among Near Eastern traditions."),

    T("flamenco_cante_jondo", "Flamenco Cante Jondo", "Andalusia, 19th c.-",
      "Camarón de la Isla; seguiriyas",
      c=(0.1, 0.3, 1.0, 0.8, 0.9, 0.55, 0.4, 0.15, 0.15, 0.55, 0.1, 0.6, 0.65, 0.05, 0.1, 0.2, 0.45, 0.85),
      g=("just_intonation", "octave_repeating", "additive_metric", "arc_buildup",
         "monophonic", "obligatory_structural", "oral_only", "soloist_with_accompaniment",
         "entertainment_display", "evaluator_connoisseur", "structural_punctuation", "event_duration"),
      notes="Vocal front-and-center with guitar. Compás (12-beat additive) = additive_metric. Cante jondo is the deep-song branch — extreme emotional weight, Phrygian-inflected."),

    T("greek_rebetiko", "Greek Rebetiko", "Greek urban, 1920s-50s",
      "Markos Vamvakaris; Rosa Eskenazi",
      c=(0.14, 0.3, 1.0, 0.8, 0.5, 0.8, 0.55, 0.2, 0.2, 0.85, 0.08, 0.85, 0.3, 0.25, 0.4, 0.15, 0.2, 0.55),
      g=("just_intonation", "octave_repeating", "additive_metric", "sectional_contrasting",
         "heterophonic", "decorative_optional", "oral_only", "heterophonic_group",
         "narrative_storytelling", "passive_audience", "decorative_pause", "event_duration"),
      notes="Urban tavern music — Ottoman-inflected scales (dromoi) in Balkan idiom. Zeibekiko rhythm = 9/4 additive. Songs of the manges subculture."),

    T("sephardic_liturgical", "Sephardic Liturgical Song", "Sephardic diaspora, medieval-",
      "Ladino romances; Judeo-Spanish piyyutim",
      c=(0.11, 0.15, 1.0, 0.7, 0.5, 0.5, 0.4, 0.05, 0.15, 0.55, 0.2, 0.7, 0.3, 0.08, 0.05, 0.1, 0.3, 0.55),
      g=("just_intonation", "octave_repeating", "additive_metric", "cyclical_return",
         "monophonic", "decorative_optional", "oral_only", "unison_ensemble",
         "ritual_religious", "ritual_participant", "decorative_pause", "ritual_duration"),
      notes="Cross-Mediterranean oral tradition, modal, strophic. Differs from Sephardic secular (more dance-meter)."),

    T("byzantine_chant", "Byzantine Orthodox Chant", "Eastern Mediterranean, Byzantine-",
      "Athonite tradition; Cappella Romana recordings",
      c=(0.18, 0.45, 1.0, 0.8, 0.6, 0.1, 0.35, 0.0, 0.15, 0.2, 0.25, 0.35, 0.25, 0.3, 0.15, 0.75, 0.05, 0.5),
      g=("just_intonation", "octave_repeating", "pulse_free", "through_composed_narrative",
         "drone_based", "obligatory_structural", "notated_skeletal", "unison_ensemble",
         "ritual_religious", "ritual_participant", "structural_punctuation", "ritual_duration"),
      notes="Ison (held drone) + chanted melody. Octoechos = eight modes. Microtonality_degree higher than Gregorian because of modal inflections. neumatic notated_skeletal."),

    # -------------------- East Asian --------------------
    T("chinese_guqin", "Chinese Guqin (scholar's zither)", "China, 3,000+ years",
      "Guan Pinghu; Gao Shan Liu Shui",
      c=(0.12, 0.2, 1.0, 0.55, 0.85, 0.1, 0.2, 0.0, 0.1, 0.15, 0.25, 0.3, 0.25, 0.0, 0.0, 0.15, 0.35, 0.85),
      g=("just_intonation", "octave_repeating", "pulse_free", "through_composed_narrative",
         "monophonic", "obligatory_structural", "notated_skeletal", "solo",
         "contemplative_personal", "no_listener_intended", "equal_to_sound", "event_duration"),
      notes="Silk-string zither played for one's own cultivation — no_listener_intended. Tablature notates fingerings but not rhythm. Microtonal slides (naoyin, yinyin) drive pitch_flexibility near max."),

    T("korean_pansori", "Korean Pansori (solo epic narrative)", "Korea, 17th c.-",
      "Ahn Sook-sun; Chunhyangga",
      c=(0.1, 0.35, 1.0, 0.7, 0.95, 0.6, 0.55, 0.15, 0.35, 0.5, 0.95, 0.5, 0.95, 0.08, 0.1, 0.0, 0.45, 0.75),
      g=("just_intonation", "octave_repeating", "additive_metric", "through_composed_narrative",
         "monophonic", "obligatory_structural", "oral_only", "soloist_with_accompaniment",
         "narrative_storytelling", "participatory_communal", "structural_punctuation", "event_duration"),
      notes="Singer + single drummer, performances 3-8 hours. Pansori jangdan are additive rhythmic cycles. Voice includes extreme guttural/speech/sung inflections → pitch_flexibility max."),

    T("korean_samulnori", "Korean Samulnori (four-drum ensemble)", "Korea, modernized 1978",
      "Kim Duk-soo SamulNori",
      c=(0.02, 0.0, 0.3, 0.3, 0.4, 0.98, 0.95, 0.85, 0.3, 0.85, 0.2, 0.85, 0.7, 0.4, 0.75, 0.0, 0.25, 0.3),
      g=("indeterminate", "single_cycle_no_repeat", "additive_metric", "arc_buildup",
         "layered_ostinato", "improvisatory_expansive", "oral_only", "interlocking_parts",
         "entertainment_display", "passive_audience", "structural_punctuation", "event_duration"),
      notes="Four percussion instruments (kkwaenggwari, jing, janggu, buk) in interlocking rhythmic cycles. Concert form derived from p'ungmul village tradition. Tempo accelerations produce arc."),

    T("korean_aak_court", "Korean Aak Court Music", "Korea, Goryeo/Joseon 12th c.-",
      "Munmyo Jeryeak (Confucian shrine music)",
      c=(0.14, 0.15, 1.0, 0.55, 0.2, 0.5, 0.1, 0.2, 0.3, 0.35, 0.25, 0.7, 0.1, 0.55, 0.45, 0.2, 0.02, 0.3),
      g=("just_intonation", "octave_repeating", "ritual_cued", "cyclical_return",
         "heterophonic", "obligatory_structural", "notated_prescriptive", "unison_ensemble",
         "ritual_religious", "ritual_participant", "foundational_ground", "ritual_duration"),
      notes="Anchor for notated_prescriptive non-Western ensemble. Preserved via Akhakgwebeom (15th c. treatise). Slow, ceremonial Confucian ritual music with large ensemble including dancers. Rare extant East Asian prescriptive notation tradition."),

    T("peking_opera", "Peking Opera (jingju)", "China, 1790-",
      "Mei Lanfang; Farewell My Concubine",
      c=(0.15, 0.35, 1.0, 0.75, 0.85, 0.85, 0.65, 0.25, 0.2, 0.75, 0.5, 0.65, 0.65, 0.5, 0.55, 0.15, 0.3, 0.8),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "sectional_contrasting",
         "heterophonic", "obligatory_structural", "oral_only", "soloist_with_accompaniment",
         "narrative_storytelling", "passive_audience", "structural_punctuation", "event_duration"),
      notes="Stylized vocal types (dan, sheng, etc.) with fixed ornament grammars. Jinghu fiddle + percussion ensemble. Character-type vocal style is the primary ornament system."),

    T("mongolian_urtiin_duu", "Mongolian Urtiin Duu (long song)", "Mongolian steppe",
      "Norovbanzad",
      c=(0.1, 0.4, 1.0, 0.65, 0.95, 0.1, 0.15, 0.0, 0.15, 0.15, 0.55, 0.3, 0.35, 0.08, 0.0, 0.1, 0.3, 0.95),
      g=("just_intonation", "octave_repeating", "pulse_free", "through_composed_narrative",
         "monophonic", "obligatory_structural", "oral_only", "solo",
         "environmental_dialogue", "participatory_communal", "structural_punctuation", "event_duration"),
      notes="Single-syllable phrases extended over long melismatic breaths. Ornament_density near max (nugulalt trills). Traditionally sung to horses/the steppe — environmental_dialogue."),

    T("japanese_noh", "Japanese Noh Theatre Music", "Japan, 14th c.-",
      "Kanze school; Hagoromo",
      c=(0.1, 0.35, 1.0, 0.65, 0.75, 0.3, 0.25, 0.3, 0.4, 0.25, 0.75, 0.55, 0.45, 0.3, 0.55, 0.3, 0.1, 0.8),
      g=("just_intonation", "octave_repeating", "cyclical_nonmetric", "through_composed_narrative",
         "heterophonic", "obligatory_structural", "notated_skeletal", "unison_ensemble",
         "ritual_religious", "ritual_participant", "foundational_ground", "ritual_duration"),
      notes="Chorus + shite (principal actor) + hayashi (drums + flute). Jo-ha-kyū structure (slow-break-rapid). Extremely slow overall tempo; ornament-dense vocal style."),

    T("javanese_gamelan", "Javanese Gamelan (Central Javanese court)", "Java, Surakarta/Yogyakarta",
      "Gamelan Kyai Kaduk Manis",
      c=(0.05, 0.35, 0.9, 0.45, 0.1, 0.75, 0.7, 0.6, 0.65, 0.35, 0.45, 0.9, 0.2, 0.6, 0.55, 0.0, 0.1, 0.3),
      g=("inharmonic_spectral", "octave_repeating", "cyclical_nonmetric", "cyclical_return",
         "layered_ostinato", "obligatory_structural", "oral_only", "interlocking_parts",
         "ritual_religious", "ritual_participant", "foundational_ground", "ritual_duration"),
      notes="Slower, more meditative than Balinese gong kebyar. Longer gong cycles (cycle_length higher). Gendhing form emphasizes gong structure over interlocking density. Pairs with balinese_gong_kebyar as contrast."),

    T("vietnamese_ca_tru", "Vietnamese Ca Trù", "North Vietnam, ~15th c.-",
      "Quách Thị Hồ",
      c=(0.12, 0.4, 1.0, 0.75, 0.9, 0.55, 0.4, 0.15, 0.25, 0.4, 0.3, 0.5, 0.45, 0.05, 0.05, 0.15, 0.35, 0.8),
      g=("just_intonation", "octave_repeating", "additive_metric", "sectional_contrasting",
         "monophonic", "obligatory_structural", "oral_only", "soloist_with_accompaniment",
         "entertainment_display", "evaluator_connoisseur", "decorative_pause", "event_duration"),
      notes="Female singer + đàn đáy lute + phách (bamboo clapper). Extremely ornamented vocal style. Near-extinct UNESCO-listed tradition."),

    # -------------------- African --------------------
    T("zulu_isicathamiya", "Zulu Isicathamiya (a cappella choral)", "South Africa, early 20th c.-",
      "Ladysmith Black Mambazo",
      c=(0.1, 0.1, 1.0, 0.65, 0.4, 0.8, 0.55, 0.3, 0.2, 0.85, 0.1, 0.85, 0.5, 0.55, 0.75, 0.0, 0.15, 0.3),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "cyclical_return",
         "homophonic", "decorative_optional", "oral_only", "heterophonic_group",
         "entertainment_display", "participatory_communal", "avoided", "event_duration"),
      notes="Male a cappella choral tradition emerged from migrant hostel culture. Soft-stepping dance — isicathamiya means 'stalk'. Homophonic four-part texture."),

    T("mbira_dzavadzimu", "Mbira dzavadzimu (Shona spirit music)", "Zimbabwe",
      "Stella Chiweshe; Thomas Mapfumo",
      c=(0.1, 0.15, 1.0, 0.3, 0.3, 0.85, 0.75, 0.6, 0.25, 0.75, 0.85, 0.95, 0.3, 0.3, 0.7, 0.5, 0.35, 0.3),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "cyclical_return",
         "layered_ostinato", "decorative_optional", "oral_only", "interlocking_parts",
         "ritual_religious", "ritual_participant", "avoided", "ritual_duration"),
      notes="All-night bira ceremonies to summon ancestors. Two mbiras play interlocking kushaura and kutsinhira parts. Formal_repetition near max but formal_type=cyclical_return with gradual variation (kutema)."),

    T("gnawa_lila", "Moroccan Gnawa Lila (all-night trance)", "Morocco, sub-Saharan diaspora",
      "Maâlem Mahmoud Guinia",
      c=(0.08, 0.3, 0.9, 0.5, 0.55, 0.9, 0.7, 0.3, 0.35, 0.85, 0.95, 0.9, 0.55, 0.3, 0.3, 0.75, 0.45, 0.45),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "cyclical_return",
         "drone_based", "obligatory_structural", "oral_only", "call_response",
         "trance_induction", "ritual_participant", "avoided", "ritual_duration"),
      notes="Gap-filler #1: canonical trance_induction tradition. Maâlem leads guimbri + qraqeb castanets + chorus. All-night lila ritual to summon spirits. Each mluk (spirit) has specific colors + tonal framework. piece_duration very high (single suite 30-90 min; whole lila 8+ hrs)."),

    T("ethiopian_orthodox_zema", "Ethiopian Orthodox Zema", "Ethiopia, 6th c.-",
      "Debtera chanting; Geez liturgy",
      c=(0.15, 0.3, 1.0, 0.75, 0.65, 0.3, 0.35, 0.1, 0.2, 0.3, 0.3, 0.6, 0.25, 0.35, 0.15, 0.25, 0.05, 0.6),
      g=("just_intonation", "octave_repeating", "cyclical_nonmetric", "cyclical_return",
         "heterophonic", "obligatory_structural", "notated_skeletal", "unison_ensemble",
         "ritual_religious", "ritual_participant", "structural_punctuation", "ritual_duration"),
      notes="Three melodic modes (Ge'ez, Ezel, Araray). Yared's melekket notation system is unique to Ethiopia. Debtera chanters + sistrum (tsenatsil) + drums."),

    T("manding_kora", "Manding Kora Tradition (jeli)", "West Africa (Mali/Senegambia)",
      "Toumani Diabaté",
      c=(0.12, 0.1, 1.0, 0.6, 0.3, 0.7, 0.75, 0.45, 0.25, 0.75, 0.25, 0.6, 0.45, 0.15, 0.3, 0.1, 0.45, 0.55),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "theme_and_variation",
         "polyphonic_independent", "decorative_optional", "oral_only", "solo",
         "narrative_storytelling", "participatory_communal", "decorative_pause", "event_duration"),
      notes="21-string harp-lute. Jeli (griot) plays kumbengo (ostinato) + birimintingo (improvised runs) simultaneously — hence voice_independence via one instrument. Narrative function — historical epics."),

    T("central_african_horn_ensemble", "Central African Horn/Flute Ensemble (hocket)", "CAR, Cameroon",
      "Banda-Linda horn orchestras",
      c=(0.08, 0.1, 0.8, 0.2, 0.1, 0.95, 0.95, 0.9, 0.2, 0.9, 0.2, 0.95, 0.3, 0.65, 0.9, 0.0, 0.1, 0.1),
      g=("just_intonation", "single_cycle_no_repeat", "isochronous_metric", "cyclical_return",
         "polyphonic_independent", "forbidden", "oral_only", "interlocking_parts",
         "ritual_religious", "participatory_communal", "avoided", "ritual_duration"),
      notes="Each player sounds a single pitch — melody emerges ONLY from group hocket. Extreme example of interlocking_parts + voice_independence without individual ornament."),

    # -------------------- Americas — Indigenous --------------------
    T("navajo_song_cycle", "Navajo Diné Ceremonial Song Cycle", "Southwest USA",
      "Blessingway (Hózhó) chants",
      c=(0.08, 0.25, 0.9, 0.55, 0.5, 0.75, 0.45, 0.15, 0.4, 0.8, 0.85, 0.9, 0.25, 0.25, 0.2, 0.1, 0.1, 0.35),
      g=("just_intonation", "octave_repeating", "ritual_cued", "cyclical_return",
         "heterophonic", "obligatory_structural", "oral_only", "unison_ensemble",
         "cosmological_representation", "ritual_participant", "structural_punctuation", "natural_cycle_aligned"),
      notes="Multi-day ceremonies (Nightway, Blessingway). Text-melody correspondence is cosmologically load-bearing — errors invalidate the ceremony. Rattle/drum drive metric pulse."),

    T("andean_wayno", "Andean Quechua Wayno", "Andes (Peru, Bolivia)",
      "Huayno; Carnaval melodies",
      c=(0.1, 0.1, 1.0, 0.8, 0.4, 0.95, 0.6, 0.25, 0.15, 0.9, 0.1, 0.9, 0.3, 0.35, 0.4, 0.05, 0.2, 0.3),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "cyclical_return",
         "homophonic", "decorative_optional", "oral_only", "heterophonic_group",
         "entertainment_display", "participatory_communal", "avoided", "natural_cycle_aligned"),
      notes="Pentatonic core + Spanish colonial influence. Quena flute, charango, drum. Seasonal festival function → natural_cycle_aligned temporal_framing."),

    T("peyote_chant", "Native American Peyote Chant (NAC)", "Plains/Southwest USA",
      "All-night Peyote ceremony songs",
      c=(0.06, 0.2, 0.85, 0.55, 0.5, 0.95, 0.55, 0.1, 0.1, 0.9, 0.85, 0.95, 0.3, 0.08, 0.05, 0.1, 0.15, 0.25),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "cyclical_return",
         "monophonic", "obligatory_structural", "oral_only", "unison_ensemble",
         "ritual_religious", "ritual_participant", "structural_punctuation", "natural_cycle_aligned"),
      notes="All-night ceremony, 4 ritual songs from each participant in turn. Water drum + gourd rattle fix tempo. Set of songs per participant → piece_duration structural."),

    # -------------------- Americas — Afro-diasporic --------------------
    T("haitian_vodou_drumming", "Haitian Vodou Rada Drumming", "Haiti",
      "Max Beauvoir lineage; Rada rites",
      c=(0.05, 0.0, 0.4, 0.25, 0.35, 0.9, 0.95, 0.9, 0.25, 0.8, 0.85, 0.9, 0.55, 0.45, 0.85, 0.1, 0.5, 0.35),
      g=("indeterminate", "single_cycle_no_repeat", "isochronous_metric", "arc_buildup",
         "layered_ostinato", "improvisatory_expansive", "oral_only", "interlocking_parts",
         "trance_induction", "ritual_participant", "avoided", "ritual_duration"),
      notes="Three-drum ensemble (manman, seconde, boula) + ogan bell. Master drummer (manman) improvises against fixed second/third drum patterns. Drives possession trance."),

    T("cuban_son_montuno", "Cuban Son Montuno", "Cuba, early 20th c.",
      "Arsenio Rodríguez; Septeto Habanero",
      c=(0.14, 0.05, 1.0, 0.75, 0.35, 0.9, 0.7, 0.6, 0.2, 0.9, 0.12, 0.9, 0.35, 0.4, 0.4, 0.2, 0.35, 0.4),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "sectional_contrasting",
         "call_response", "decorative_optional", "oral_only", "call_response",
         "entertainment_display", "participatory_communal", "avoided", "event_duration"),
      notes="Clave-based rhythmic framework. Verse + montuno (call-response vamp) structure. Anchor for clave-based Afro-Cuban forms; reggaeton and salsa descend from here."),

    T("brazilian_samba_escola", "Brazilian Samba Escola Parade", "Rio de Janeiro, 20th c.-",
      "Mangueira, Portela Carnival parades",
      c=(0.12, 0.0, 1.0, 0.7, 0.3, 1.0, 0.9, 0.8, 0.2, 0.95, 0.65, 0.95, 0.55, 0.85, 0.6, 0.0, 0.15, 0.3),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "cyclical_return",
         "layered_ostinato", "decorative_optional", "hybrid", "spatially_distributed",
         "life_cycle_event", "participatory_communal", "avoided", "event_duration"),
      notes="Second spatially_distributed example — parade stretches over 800m with 3000+ percussionists. Bateria sections in interlocking patterns. Samba-enredo melody sung simultaneously."),

    T("black_gospel", "Black Gospel (Pentecostal tradition)", "USA, 20th c.-",
      "Mahalia Jackson; Aretha Franklin",
      c=(0.15, 0.15, 1.0, 0.85, 0.85, 0.9, 0.65, 0.3, 0.2, 0.85, 0.15, 0.9, 0.85, 0.45, 0.55, 0.2, 0.6, 0.75),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "arc_buildup",
         "call_response", "obligatory_structural", "oral_only", "call_response",
         "trance_induction", "participatory_communal", "decorative_pause", "event_duration"),
      notes="Altar-call gospel aims for ecstatic climax → arc_buildup + trance_induction. Melisma-heavy lead + call-response with congregation. Pitch_flexibility max (shouts, runs)."),

    # -------------------- Americas — Latin --------------------
    T("argentine_tango", "Argentine Tango", "Buenos Aires, 1880s-",
      "Astor Piazzolla; Carlos Gardel-era",
      c=(0.15, 0.1, 1.0, 0.8, 0.6, 0.8, 0.6, 0.2, 0.2, 0.65, 0.15, 0.8, 0.7, 0.4, 0.55, 0.1, 0.25, 0.5),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "sectional_contrasting",
         "homophonic", "decorative_optional", "notated_prescriptive", "unison_ensemble",
         "entertainment_display", "passive_audience", "decorative_pause", "clock_time_bounded"),
      notes="Orquesta típica: bandoneones + strings + piano + bass. Rubato (hence tempo_stability moderate). Prescriptive arrangements, but bandoneon ornaments add flex."),

    T("mexican_mariachi", "Mexican Mariachi", "Mexico, 19th c.-",
      "Mariachi Vargas de Tecalitlán",
      c=(0.14, 0.05, 1.0, 0.75, 0.45, 0.95, 0.55, 0.15, 0.15, 0.95, 0.1, 0.9, 0.4, 0.5, 0.5, 0.05, 0.15, 0.4),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "cyclical_return",
         "homophonic", "decorative_optional", "oral_only", "heterophonic_group",
         "life_cycle_event", "participatory_communal", "avoided", "event_duration"),
      notes="Trumpets, violins, vihuela, guitarrón, vocals. Son jalisciense base. Strophic song form. Functional at weddings, funerals, serenatas — life_cycle_event."),

    T("reggaeton", "Reggaeton (dembow-based)", "Puerto Rico/Panama, 1990s-",
      "Daddy Yankee; contemporary urbano",
      c=(0.08, 0.05, 1.0, 0.5, 0.15, 1.0, 0.75, 0.35, 0.08, 1.0, 0.08, 0.98, 0.25, 0.2, 0.55, 0.05, 0.05, 0.2),
      g=("equal_temperament", "octave_repeating", "isochronous_metric", "modular_combinatorial",
         "layered_ostinato", "decorative_optional", "recorded_reference", "solo",
         "entertainment_display", "participatory_communal", "avoided", "clock_time_bounded"),
      notes="Dembow riddim = near-universal rhythmic template. Producer-as-author. Low formal_repetition for verse/chorus → high. Descends from son clave via dancehall."),

    # -------------------- Sacred / devotional --------------------
    T("gyuto_tantric_chant", "Gyütö Tantric Throat Chant", "Tibet (Gelugpa monastic)",
      "Gyütö monks vocal harmonics",
      c=(0.15, 0.35, 0.25, 0.6, 0.25, 0.1, 0.1, 0.05, 0.3, 0.3, 0.5, 0.85, 0.1, 0.3, 0.5, 0.85, 0.05, 0.2),
      g=("overtone_series", "non_octave_repeating", "pulse_free", "cyclical_return",
         "drone_based", "obligatory_structural", "oral_only", "unison_ensemble",
         "ritual_religious", "ritual_participant", "foundational_ground", "ritual_duration"),
      notes="Monks sing ultra-low fundamentals producing audible 5th/10th harmonics — overtone melody without soloistic line. Anchor for collective overtone-chord singing (contrast solo Tuvan)."),

    T("shaker_hymnody", "Shaker Hymnody (Millennial Church)", "New England, 1774-20th c.",
      "Simple Gifts; Brotherhood",
      c=(0.1, 0.05, 1.0, 0.75, 0.15, 0.85, 0.5, 0.1, 0.1, 0.85, 0.1, 0.9, 0.2, 0.1, 0.05, 0.0, 0.05, 0.05),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "cyclical_return",
         "monophonic", "forbidden", "notated_skeletal", "unison_ensemble",
         "ritual_religious", "ritual_participant", "avoided", "ritual_duration"),
      notes="Monophonic (Shakers rejected harmony as worldly). ornament_grammar=forbidden (doctrinal simplicity). Unison communal song with dance. letter-notation system unique to the sect."),

    T("hasidic_nigun", "Hasidic Nigun (wordless melody)", "Eastern Europe, 18th c.-",
      "Chabad nigunim; Bobov",
      c=(0.1, 0.1, 1.0, 0.75, 0.55, 0.75, 0.5, 0.1, 0.2, 0.75, 0.4, 0.95, 0.6, 0.2, 0.35, 0.2, 0.2, 0.4),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "arc_buildup",
         "heterophonic", "decorative_optional", "oral_only", "unison_ensemble",
         "trance_induction", "ritual_participant", "avoided", "ritual_duration"),
      notes="Wordless devotional melody sung communally, often with gradual acceleration to ecstatic climax. Lubavitch 'deveikus' nigunim — meditative tempo. Distinct from qawwali/gnawa by monophonic + no drum."),

    # -------------------- Experimental / frontier --------------------
    T("didgeridoo_solo", "Aboriginal Australian Didgeridoo Solo", "Northern Australia",
      "Djalu Gurruwiwi",
      c=(0.06, 0.3, 0.25, 0.5, 0.7, 0.85, 0.8, 0.5, 0.25, 0.75, 0.2, 0.9, 0.2, 0.0, 0.4, 0.95, 0.35, 0.65),
      g=("overtone_series", "non_octave_repeating", "isochronous_metric", "cyclical_return",
         "drone_based", "obligatory_structural", "oral_only", "solo",
         "ritual_religious", "ritual_participant", "avoided", "event_duration"),
      notes="Circular breathing produces continuous drone; vocalizations + tongue/cheek articulations modulate overtones. Part of ceremony but here framed as solo instrumental tradition."),

    T("hawaiian_oli", "Hawaiian Oli (chant)", "Hawaii, pre-contact-",
      "Genealogical mele; Kumulipo",
      c=(0.06, 0.2, 1.0, 0.7, 0.65, 0.25, 0.4, 0.0, 0.4, 0.45, 0.65, 0.4, 0.3, 0.0, 0.0, 0.15, 0.2, 0.3),
      g=("just_intonation", "octave_repeating", "pulse_free", "through_composed_narrative",
         "monophonic", "obligatory_structural", "oral_only", "solo",
         "cosmological_representation", "ritual_participant", "structural_punctuation", "ritual_duration"),
      notes="Unaccompanied chant preserving genealogies, cosmogony, place-names. Very narrow pitch range but intricate i‛i (trill) ornaments on a small number of tones."),

    T("lachenmann_instrumental_concrete", "Lachenmann Musique Concrète Instrumentale", "Germany, 1960s-",
      "Pression; Gran Torso; …zwei Gefühle…",
      c=(0.5, 0.75, 0.3, 0.1, 0.75, 0.3, 0.4, 0.5, 0.1, 0.35, 0.5, 0.1, 0.45, 0.4, 0.8, 0.15, 0.05, 0.5),
      g=("equal_temperament", "octave_repeating", "indeterminate_proportional", "through_composed_narrative",
         "spectral_cloud", "obligatory_structural", "notated_prescriptive", "unison_ensemble",
         "contemplative_personal", "passive_audience", "structural_punctuation", "clock_time_bounded"),
      notes="Extended instrumental techniques (bowing the body, key clicks, breath noises) composed into concrete-music forms. Pitch is present but not primary — texture/noise is the content."),

    T("conrad_long_string_drone", "Tony Conrad Violin Drone", "USA, 1960s-70s",
      "Four Violins; Early Minimalism",
      c=(0.15, 0.85, 0.3, 0.8, 0.2, 0.2, 0.3, 0.2, 0.0, 0.3, 0.9, 0.3, 0.1, 0.12, 0.3, 0.95, 0.15, 0.05),
      g=("just_intonation", "non_octave_repeating", "indeterminate_proportional", "static_contemplation",
         "drone_based", "forbidden", "recorded_reference", "solo",
         "contemplative_personal", "passive_audience", "foundational_ground", "event_duration"),
      notes="Just-intonation bowed-string drones emphasizing beating patterns. Formative pre-La Monte Young Theatre of Eternal Music. Shorter duration than Well-Tuned Piano."),

    T("inuit_drum_dance_song", "Inuit Drum-Dance Song", "Arctic Canada, Greenland",
      "Pisiit, aya-yait songs",
      c=(0.06, 0.15, 0.85, 0.45, 0.45, 0.85, 0.6, 0.15, 0.2, 0.8, 0.15, 0.9, 0.25, 0.05, 0.0, 0.05, 0.2, 0.2),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "cyclical_return",
         "monophonic", "decorative_optional", "oral_only", "solo",
         "narrative_storytelling", "participatory_communal", "avoided", "natural_cycle_aligned"),
      notes="Different from katajjaq — this is solo sung narrative with frame drum (qilaut). Pisiit are 'personal songs' composed for specific life events."),

    T("sardinian_launeddas", "Sardinian Launeddas (triple clarinet)", "Sardinia",
      "Luigi Lai; Efisio Melis",
      c=(0.1, 0.25, 1.0, 0.65, 0.5, 0.85, 0.65, 0.5, 0.25, 0.75, 0.45, 0.85, 0.4, 0.0, 0.7, 0.85, 0.45, 0.55),
      g=("just_intonation", "octave_repeating", "isochronous_metric", "theme_and_variation",
         "drone_based", "obligatory_structural", "oral_only", "solo",
         "entertainment_display", "participatory_communal", "decorative_pause", "event_duration"),
      notes="One player, three pipes — drone pipe + tumbu (low melody) + mancosedda (high counter-melody). Circular breathing. voice_independence moderate because one person plays three simultaneous parts."),
]


# ============================================================
# Validation — uses coherence.py as single source of truth
# ============================================================

with open(SCHEMA_PATH) as f:
    schema = json.load(f)

all_traditions = anchors + NEW

print(f"Validating {len(all_traditions)} traditions...\n")

total_errs = 0
for t in all_traditions:
    enum_errs = check_schema_values(t["categorical"], schema)
    result = check(t["continuous"], t["categorical"])
    errs = enum_errs + result.violations
    if errs:
        print(f"✗ {t['id']}:")
        for e in errs:
            print(f"    {e}")
        total_errs += len(errs)

if total_errs == 0:
    print(f"✓ All {len(all_traditions)} traditions pass categorical enum + coherence checks.")
else:
    print(f"\n{total_errs} total violations — fix before committing.")
    raise SystemExit(1)

# ============================================================
# Write corpus.json
# ============================================================

corpus = {
    "_meta": {
        "count": len(all_traditions),
        "anchor_count": sum(1 for t in all_traditions if t.get("is_anchor")),
        "built_from": "build_corpus.py + anchors.json",
        "date": "2026-04-21",
        "schema_version": schema["schema_version"],
    },
    "traditions": all_traditions,
}

with open(OUT_PATH, "w") as f:
    json.dump(corpus, f, ensure_ascii=False, indent=2)

print(f"\nWrote {len(all_traditions)} traditions to {OUT_PATH}")
print(f"  {corpus['_meta']['anchor_count']} anchors, {len(all_traditions) - corpus['_meta']['anchor_count']} additions")
