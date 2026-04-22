"""Morphospace coordinate sampler.

Rejection sampling: draw candidate points, reject those that fail coherence
or sit too close to known corpus. Bias toward high curiosity (high distance).

Strategy:
  1. Sample N candidates uniformly in the continuous hypercube + categorical enums.
  2. Coherence-check each; drop failures.
  3. Rank survivors by curiosity score.
  4. Return the top candidate.

This is a baseline — not Voronoi-optimal, but honest and simple. The loop
surfaces warnings, the user can iterate on the strategy later.
"""

import json
import random
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
from coherence import check  # noqa: E402
from loop.distance import CONT_DIMS, CAT_DIMS, curiosity_score  # noqa: E402


def load_schema() -> dict:
    with open(ROOT / "schema" / "schema.json") as f:
        return json.load(f)


def load_corpus() -> List[dict]:
    with open(ROOT / "corpus" / "corpus.json") as f:
        return json.load(f)["traditions"]


def sample_random_point(schema: dict, rng: random.Random) -> Tuple[Dict[str, float], Dict[str, str]]:
    """Draw a uniform random point in the morphospace."""
    cont = {d: round(rng.random(), 3) for d in CONT_DIMS}
    cat = {}
    for d in CAT_DIMS:
        values = schema["categorical"][d]["values"]
        cat[d] = rng.choice(values)
    return cont, cat


def is_compositional(cont: Dict[str, float], cat: Dict[str, str]) -> bool:
    """Filter candidates that can support real composition (melody/harmony/rhythm).

    Rejects grammars that are structurally hostile to composed form: no home
    pitch, forbidden ornaments, avoided silence, no intended listener, aperiodic
    scales, or non-metric rhythm. See feedback_musical_morphospace_composition.md
    for the reasoning behind each threshold.
    """
    if cont["interval_hierarchy"] < 0.55:
        return False
    if cont["pitch_flexibility"] > 0.85:
        return False
    if cont["metric_periodicity"] < 0.45:
        return False
    if cont["voice_count"] < 0.35:
        return False
    if cont["formal_repetition"] < 0.3 and cont["development_arc"] < 0.4:
        return False
    if cat["rhythmic_structure"] not in ("metric", "additive_metric"):
        return False
    if cat["scale_topology"] == "aperiodic":
        return False
    if cat["ornament_grammar"] == "forbidden":
        return False
    if cat["silence_treatment"] == "avoided":
        return False
    if cat["listener_role"] == "no_listener_intended":
        return False
    if cat["formal_type"] in ("generative_algorithmic", "spectral_static"):
        return False
    return True


def sample_expedition(
    schema: dict,
    corpus: List[dict],
    n_candidates: int = 500,
    min_curiosity: float = 0.35,
    seed: int | None = None,
    compositional: bool = False,
) -> Tuple[Dict[str, float], Dict[str, str], float, List[str]]:
    """Sample one viable expedition point.

    Returns (continuous, categorical, curiosity_score, warnings).
    Raises RuntimeError if no viable point is found after n_candidates attempts.
    If compositional=True, only candidates passing is_compositional() are kept.
    """
    rng = random.Random(seed)
    best: Tuple[Dict[str, float], Dict[str, str], float, List[str]] | None = None

    attempts = 0
    rejects_coherence = 0
    rejects_not_compositional = 0
    rejects_low_curiosity = 0

    while attempts < n_candidates:
        attempts += 1
        cont, cat = sample_random_point(schema, rng)
        result = check(cont, cat)
        if not result.ok:
            rejects_coherence += 1
            continue
        if compositional and not is_compositional(cont, cat):
            rejects_not_compositional += 1
            continue
        score = curiosity_score(cont, cat, corpus)
        if score < min_curiosity:
            rejects_low_curiosity += 1
            continue
        if best is None or score > best[2]:
            best = (cont, cat, score, result.warnings)

    if best is None:
        raise RuntimeError(
            f"No viable point after {n_candidates} attempts "
            f"(coherence rejects: {rejects_coherence}, "
            f"non-compositional rejects: {rejects_not_compositional}, "
            f"low-curiosity rejects: {rejects_low_curiosity}). "
            f"Try lowering min_curiosity or increasing n_candidates."
        )

    print(f"Sampled {attempts} candidates: {rejects_coherence} incoherent, "
          f"{rejects_not_compositional} non-compositional, "
          f"{rejects_low_curiosity} too-close-to-corpus, "
          f"accepted 1 with curiosity={best[2]:.3f}", file=sys.stderr)
    return best


if __name__ == "__main__":
    schema = load_schema()
    corpus = load_corpus()
    cont, cat, score, warnings = sample_expedition(schema, corpus, seed=42)
    print(f"Curiosity: {score:.3f}")
    print(f"Continuous: {json.dumps(cont, indent=2)}")
    print(f"Categorical: {json.dumps(cat, indent=2)}")
    if warnings:
        print(f"Warnings: {warnings}")
