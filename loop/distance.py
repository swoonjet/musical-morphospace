"""Morphospace distance metric.

Hybrid: weighted Euclidean on the 18 continuous dimensions + Hamming on the
12 categorical dimensions. Weights match schema.distance_metric defaults.
"""

from typing import Dict, Iterable, List, Tuple

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

CONT_WEIGHT = 0.6
CAT_WEIGHT = 0.4


def continuous_distance(a: Dict[str, float], b: Dict[str, float]) -> float:
    """Euclidean distance on shared continuous dimensions, normalized to [0, 1]."""
    sq = 0.0
    n = 0
    for d in CONT_DIMS:
        if d in a and d in b:
            sq += (a[d] - b[d]) ** 2
            n += 1
    if n == 0:
        return 0.0
    # max Euclidean distance in unit hypercube of dim n is sqrt(n); normalize
    return (sq ** 0.5) / (n ** 0.5)


def categorical_distance(a: Dict[str, str], b: Dict[str, str]) -> float:
    """Hamming distance on categorical dimensions, normalized to [0, 1]."""
    diff = 0
    n = 0
    for d in CAT_DIMS:
        if d in a and d in b:
            if a[d] != b[d]:
                diff += 1
            n += 1
    return diff / n if n else 0.0


def point_distance(
    point_cont: Dict[str, float],
    point_cat: Dict[str, str],
    ref_cont: Dict[str, float],
    ref_cat: Dict[str, str],
) -> float:
    """Combined weighted distance between two morphospace points."""
    cd = continuous_distance(point_cont, ref_cont)
    kd = categorical_distance(point_cat, ref_cat)
    return CONT_WEIGHT * cd + CAT_WEIGHT * kd


def nearest_neighbors(
    point_cont: Dict[str, float],
    point_cat: Dict[str, str],
    corpus: List[dict],
    k: int = 3,
) -> List[Tuple[dict, float]]:
    """Return the k nearest corpus traditions to the given point, as (tradition, distance) pairs."""
    scored = [
        (t, point_distance(point_cont, point_cat, t["continuous"], t["categorical"]))
        for t in corpus
    ]
    scored.sort(key=lambda x: x[1])
    return scored[:k]


def curiosity_score(
    point_cont: Dict[str, float],
    point_cat: Dict[str, str],
    corpus: List[dict],
) -> float:
    """Curiosity score = distance to the nearest corpus tradition.

    Higher = more novel. Used to bias sampling toward empty regions.
    """
    if not corpus:
        return 1.0
    nearest = nearest_neighbors(point_cont, point_cat, corpus, k=1)
    return nearest[0][1]


def shared_and_divergent(
    point_cont: Dict[str, float],
    point_cat: Dict[str, str],
    ref_cont: Dict[str, float],
    ref_cat: Dict[str, str],
    cont_threshold: float = 0.15,
) -> Tuple[List[str], List[str]]:
    """Return (shared_parameters, divergent_parameters) for narrative comparison.

    Continuous dims are "shared" if |a - b| < cont_threshold, else divergent.
    Categorical dims are shared iff equal.
    """
    shared = []
    divergent = []
    for d in CONT_DIMS:
        if d in point_cont and d in ref_cont:
            if abs(point_cont[d] - ref_cont[d]) < cont_threshold:
                shared.append(d)
            else:
                divergent.append(d)
    for d in CAT_DIMS:
        if d in point_cat and d in ref_cat:
            if point_cat[d] == ref_cat[d]:
                shared.append(d)
            else:
                divergent.append(d)
    return shared, divergent
