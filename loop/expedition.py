"""One expedition — sample coordinate, call LLM, render audio, archive.

Usage:
    python3 -m loop.expedition [--backend offline|claude|ollama] [--seed N] [--min-curiosity 0.35]

Produces a new directory at expeditions/NNN/ containing:
  - coords.json       the sampled morphospace point + curiosity score + neighbors
  - prompt.md         the filled expedition prompt (for auditability)
  - field_notes.md    the LLM's field notes (or empty if offline backend)
  - audio_spec.json   extracted from the JSON block in field_notes.md
  - audio.wav         rendered demonstration
  - index.html        per-expedition detail page
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from loop.backends import make_backend  # noqa: E402
from loop.distance import CONT_DIMS, CAT_DIMS, nearest_neighbors, shared_and_divergent  # noqa: E402
from loop.sampler import load_corpus, load_schema, sample_expedition  # noqa: E402
from synthesis.engine import render_spec, write_wav  # noqa: E402


PROMPTS_DIR = ROOT / "prompts"
EXPEDITIONS_DIR = ROOT / "expeditions"


# ----------------------------------------------------------------------------
# Template filling
# ----------------------------------------------------------------------------

def next_expedition_number() -> int:
    existing = []
    for p in EXPEDITIONS_DIR.glob("[0-9]*"):
        m = re.match(r"^(\d+)", p.name)
        if m:
            existing.append(int(m.group(1)))
    return max(existing, default=0) + 1


def render_template(template: str, substitutions: dict) -> str:
    for k, v in substitutions.items():
        template = template.replace("{{" + k + "}}", str(v))
    return template


def fill_expedition_prompt(
    expedition_number: int,
    cont: dict,
    cat: dict,
    curiosity: float,
    warnings: list,
    neighbors: list,
    corpus: list,
) -> str:
    template = (PROMPTS_DIR / "expedition_template.md").read_text()

    # Build dim tables
    cont_table = "\n".join(f"  - {d}: {cont[d]:.3f}" for d in CONT_DIMS)
    cat_table = "\n".join(f"  - {d}: {cat[d]}" for d in CAT_DIMS)

    # Count hard constraints
    from coherence import HARD_RULES, SOFT_RULES  # local import
    n_hard = len(HARD_RULES)

    subs = {
        "expedition_number": f"{expedition_number:03d}",
        "iso_date": dt.datetime.now().isoformat(timespec="seconds"),
        "continuous_vector_json": json.dumps(cont),
        "categorical_vector_json": json.dumps(cat),
        "curiosity_score": f"{curiosity:.3f}",
        "hard_constraints_checked": str(n_hard),
        "soft_warnings_triggered": str(len(warnings)),
        "continuous_dim_table": cont_table,
        "categorical_dim_table": cat_table,
        "soft_warnings_list": "\n".join(f"  - {w}" for w in warnings) if warnings else "  (none)",
    }

    # Fill neighbor blocks
    for i, (t, dist) in enumerate(neighbors[:3], start=1):
        shared, divergent = shared_and_divergent(cont, cat, t["continuous"], t["categorical"])
        subs[f"neighbor_{i}_name"] = t["name"]
        subs[f"neighbor_{i}_distance"] = f"{dist:.3f}"
        subs[f"neighbor_{i}_region"] = t.get("region", "")
        subs[f"neighbor_{i}_notes"] = t.get("notes", "")
        subs[f"neighbor_{i}_shared"] = ", ".join(shared) if shared else "(none)"
        subs[f"neighbor_{i}_divergent"] = ", ".join(divergent) if divergent else "(none)"

    return render_template(template, subs)


# ----------------------------------------------------------------------------
# Audio spec extraction
# ----------------------------------------------------------------------------

def extract_audio_spec(field_notes_md: str) -> dict:
    m = re.search(r"```json\s*\n(.*?)\n```", field_notes_md, re.DOTALL)
    if not m:
        raise ValueError("No ```json block found in field notes")
    return json.loads(m.group(1))


# ----------------------------------------------------------------------------
# Index page template
# ----------------------------------------------------------------------------

EXPEDITION_INDEX_TEMPLATE = Path(__file__).parent.parent / "expeditions" / "example" / "index.html"


def make_index_html(expedition_num: int, system_name: str, curiosity: float, duration: float, n_voices: int, rhythm_type: str) -> str:
    # Reuse the example's template, patch key fields
    tpl = EXPEDITION_INDEX_TEMPLATE.read_text()
    tpl = tpl.replace("N° 001", f"N° {expedition_num:03d}")
    tpl = tpl.replace("Curiosity</span> <b>0.58</b>", f"Curiosity</span> <b>{curiosity:.2f}</b>")
    tpl = tpl.replace("Duration</span> <b>75s</b>", f"Duration</span> <b>{int(duration)}s</b>")
    tpl = tpl.replace("Rhythm</span> <b>breath_based</b>", f"Rhythm</span> <b>{rhythm_type}</b>")
    tpl = tpl.replace("Voices</span> <b>4</b>", f"Voices</span> <b>{n_voices}</b>")
    tpl = tpl.replace("Interlocking Overtone Respiration", system_name)
    # Adjust title tag
    tpl = re.sub(r"<title>.*?</title>",
                 f"<title>Expedition {expedition_num:03d} — {system_name} · Musical Morphospace</title>",
                 tpl)
    return tpl


# ----------------------------------------------------------------------------
# Orchestrator
# ----------------------------------------------------------------------------

def run_expedition(backend_name: str, seed: int | None, min_curiosity: float, n_candidates: int, compositional: bool = False) -> Path:
    schema = load_schema()
    corpus = load_corpus()

    print(f"Sampling coordinate (min_curiosity={min_curiosity}, n_candidates={n_candidates}, compositional={compositional})...")
    cont, cat, curiosity, warnings = sample_expedition(
        schema=schema,
        corpus=corpus,
        n_candidates=n_candidates,
        min_curiosity=min_curiosity,
        seed=seed,
        compositional=compositional,
    )
    neighbors = nearest_neighbors(cont, cat, corpus, k=3)
    print(f"  curiosity: {curiosity:.3f}")
    print("  nearest: " + ", ".join(f"{t[0]['name']} ({t[1]:.2f})" for t in neighbors))
    if warnings:
        print(f"  soft warnings: {warnings}")

    # Prepare expedition directory
    num = next_expedition_number()
    exp_dir = EXPEDITIONS_DIR / f"{num:03d}"
    exp_dir.mkdir(parents=True, exist_ok=True)
    print(f"  expedition dir: {exp_dir}")

    # Save coords
    (exp_dir / "coords.json").write_text(json.dumps({
        "expedition_number": num,
        "iso_date": dt.datetime.now().isoformat(timespec="seconds"),
        "curiosity_score": curiosity,
        "continuous": cont,
        "categorical": cat,
        "warnings": warnings,
        "neighbors": [
            {"name": t[0]["name"], "id": t[0]["id"], "distance": t[1]}
            for t in neighbors
        ],
    }, indent=2))

    # Fill the prompt
    user_prompt = fill_expedition_prompt(num, cont, cat, curiosity, warnings, neighbors, corpus)
    (exp_dir / "prompt.md").write_text(user_prompt)
    system_prompt = (PROMPTS_DIR / "system.md").read_text()

    # Call LLM
    backend = make_backend(backend_name, exp_dir)
    field_notes = backend.generate(system_prompt, user_prompt)

    if not field_notes:
        print(f"\nOffline mode — prompt written to {exp_dir / 'prompt.md'}.")
        print("Run an LLM, save response to field_notes.md in that folder,")
        print(f"then: python3 -m loop.finalize {num}")
        return exp_dir

    (exp_dir / "field_notes.md").write_text(field_notes)

    # Extract audio spec
    try:
        spec = extract_audio_spec(field_notes)
    except Exception as e:
        print(f"ERROR extracting audio spec: {e}")
        print(f"Field notes saved to {exp_dir / 'field_notes.md'} for inspection.")
        return exp_dir

    (exp_dir / "audio_spec.json").write_text(json.dumps(spec, indent=2))

    # Render audio
    print(f"Rendering audio...")
    samples = render_spec(spec, seed=seed or 42)
    write_wav(samples, str(exp_dir / "audio.wav"))

    # Extract system name for index.html
    m = re.search(r"###?\s*1\.?\s*System name\s*\n\s*(.+?)(?:\n|$)", field_notes)
    system_name = m.group(1).strip() if m else f"Expedition {num:03d}"

    # Write index.html
    rhythm_type = spec.get("rhythm_system", {}).get("type", "?")
    n_voices = len(spec.get("voices", []))
    duration = spec.get("duration_seconds", 0)
    (exp_dir / "index.html").write_text(
        make_index_html(num, system_name, curiosity, duration, n_voices, rhythm_type)
    )

    print(f"\n✓ Expedition {num:03d} complete: {exp_dir}")
    print(f"  system: {system_name}")
    return exp_dir


def main():
    ap = argparse.ArgumentParser(description="Run one morphospace expedition")
    ap.add_argument("--backend", default=os.environ.get("BACKEND", "offline"),
                    choices=["offline", "claude", "ollama"])
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--min-curiosity", type=float, default=0.35)
    ap.add_argument("--n-candidates", type=int, default=500)
    ap.add_argument("--compositional", action="store_true",
                    help="Restrict sampling to grammars that can support melody/harmony/rhythm")
    args = ap.parse_args()

    run_expedition(
        backend_name=args.backend,
        seed=args.seed,
        min_curiosity=args.min_curiosity,
        n_candidates=args.n_candidates,
        compositional=args.compositional,
    )


if __name__ == "__main__":
    main()
