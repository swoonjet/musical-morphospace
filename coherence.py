"""
Coherence checker for morphospace points.

Enforces the hard constraints declared in schema/schema.json against any candidate
point (real corpus tradition OR sampled expedition coordinate). Soft warnings are
returned separately so the loop can display them without blocking.

Usage:
    from coherence import check
    result = check(continuous_dict, categorical_dict)
    if not result.ok:
        print(result.violations)

This module is the single source of truth for coherence rules. build_corpus.py
and the expedition loop both import from here.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class CoherenceResult:
    ok: bool
    violations: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


# Hard constraints — fail the point if any triggers.
# Each rule is (condition_fn, message_template). condition_fn returns True if violated.
HARD_RULES = [
    (
        lambda c, g: g.get("scale_topology") == "non_octave_repeating" and c.get("octave_equivalence", 0) > 0.3,
        lambda c, g: f"scale_topology=non_octave_repeating but octave_equivalence={c['octave_equivalence']} (must be ≤ 0.3)",
    ),
    (
        lambda c, g: g.get("rhythmic_structure") == "pulse_free" and c.get("metric_periodicity", 0) > 0.3,
        lambda c, g: f"rhythmic_structure=pulse_free but metric_periodicity={c['metric_periodicity']} (must be ≤ 0.3)",
    ),
    (
        lambda c, g: g.get("rhythmic_structure") == "pulse_free" and c.get("tempo_stability", 0) > 0.5,
        lambda c, g: f"rhythmic_structure=pulse_free but tempo_stability={c['tempo_stability']} (must be ≤ 0.5)",
    ),
    (
        lambda c, g: g.get("texture_type") == "monophonic" and c.get("voice_count", 0) > 0.1,
        lambda c, g: f"texture_type=monophonic but voice_count={c['voice_count']} (must be ≤ 0.1)",
    ),
    (
        lambda c, g: g.get("texture_type") == "monophonic" and c.get("voice_independence", 0) > 0.1,
        lambda c, g: f"texture_type=monophonic but voice_independence={c['voice_independence']} (must be ≤ 0.1)",
    ),
    (
        lambda c, g: g.get("texture_type") == "drone_based" and c.get("drone_presence", 0) <= 0.6,
        lambda c, g: f"texture_type=drone_based but drone_presence={c['drone_presence']} (must be > 0.6)",
    ),
    (
        lambda c, g: g.get("ornament_grammar") == "forbidden" and c.get("ornament_density", 0) > 0.1,
        lambda c, g: f"ornament_grammar=forbidden but ornament_density={c['ornament_density']} (must be ≤ 0.1)",
    ),
    (
        lambda c, g: g.get("formal_type") == "static_contemplation" and c.get("development_arc", 0) > 0.3,
        lambda c, g: f"formal_type=static_contemplation but development_arc={c['development_arc']} (must be ≤ 0.3)",
    ),
    (
        lambda c, g: c.get("improvisation_degree", 0) > 0.8 and g.get("transmission_mode") == "notated_prescriptive",
        lambda c, g: f"improvisation_degree={c['improvisation_degree']} but transmission_mode=notated_prescriptive (conflicts)",
    ),
    (
        lambda c, g: g.get("listener_role") == "no_listener_intended" and g.get("social_function") == "entertainment_display",
        lambda c, g: "listener_role=no_listener_intended conflicts with social_function=entertainment_display",
    ),
]


# Soft warnings — advisory only. Rare combinations that occur in real traditions
# but should be flagged so the expedition loop can note them.
SOFT_RULES = [
    (
        lambda c, g: c.get("piece_duration", 0) > 0.8 and c.get("metric_periodicity", 0) > 0.9,
        lambda c, g: "long piece with strict meter — rare but attested (minimalism, trance traditions)",
    ),
    (
        lambda c, g: c.get("voice_count", 0) > 0.7 and c.get("improvisation_degree", 0) > 0.7,
        lambda c, g: "large-ensemble improvisation — rare (New Orleans, some free jazz, Aka polyphony)",
    ),
    (
        lambda c, g: c.get("microtonality_degree", 0) > 0.7 and c.get("voice_count", 0) > 0.5,
        lambda c, g: "ensemble microtonal coordination — rare (Arabic takht, Turkish classical)",
    ),
]


def check(continuous: Dict[str, float], categorical: Dict[str, str]) -> CoherenceResult:
    """Check a candidate point against all constraints.

    Args:
        continuous: Dict mapping continuous dimension name to value in [0.0, 1.0].
        categorical: Dict mapping categorical dimension name to string value.

    Returns:
        CoherenceResult with ok, violations, warnings.
    """
    violations = []
    for trigger, message in HARD_RULES:
        if trigger(continuous, categorical):
            violations.append(message(continuous, categorical))

    warnings = []
    for trigger, message in SOFT_RULES:
        if trigger(continuous, categorical):
            warnings.append(message(continuous, categorical))

    return CoherenceResult(
        ok=len(violations) == 0,
        violations=violations,
        warnings=warnings,
    )


def check_schema_values(categorical: Dict[str, str], schema: dict) -> List[str]:
    """Verify categorical values are present in the schema's enum lists.

    Returns list of error strings (empty if all valid).
    """
    enum_values = {d: set(v["values"]) for d, v in schema["categorical"].items() if d != "_note"}
    errs = []
    for dim, val in categorical.items():
        if dim not in enum_values:
            errs.append(f"unknown categorical dimension: {dim}")
            continue
        if val not in enum_values[dim]:
            errs.append(f"{dim}={val!r} is not a valid value (expected one of: {sorted(enum_values[dim])})")
    return errs


if __name__ == "__main__":
    # Sanity check: run against the full corpus.
    import json
    from pathlib import Path

    root = Path(__file__).parent
    with open(root / "schema" / "schema.json") as f:
        schema = json.load(f)
    with open(root / "corpus" / "corpus.json") as f:
        corpus = json.load(f)

    n = len(corpus["traditions"])
    fail = 0
    warn = 0
    for t in corpus["traditions"]:
        enum_errs = check_schema_values(t["categorical"], schema)
        if enum_errs:
            print(f"✗ {t['id']}: enum errors: {enum_errs}")
            fail += 1
            continue
        result = check(t["continuous"], t["categorical"])
        if not result.ok:
            print(f"✗ {t['id']}: {result.violations}")
            fail += 1
        if result.warnings:
            warn += 1

    if fail == 0:
        print(f"✓ All {n} corpus traditions pass hard coherence. {warn} have soft warnings.")
    else:
        print(f"\n{fail} / {n} traditions failed.")
        raise SystemExit(1)
