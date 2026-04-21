"""Finalize an offline expedition.

After running expedition.py with --backend offline and pasting the prompt into
an LLM of your choice, save the response as `field_notes.md` in the expedition
folder. Then run:

    python3 -m loop.finalize <expedition_number>

This extracts the audio spec, renders the WAV, and writes index.html.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from loop.expedition import extract_audio_spec, make_index_html  # noqa: E402
from synthesis.engine import render_spec, write_wav  # noqa: E402


def finalize(expedition_number: int, seed: int = 42) -> None:
    exp_dir = ROOT / "expeditions" / f"{expedition_number:03d}"
    if not exp_dir.exists():
        raise SystemExit(f"No expedition folder at {exp_dir}")

    notes_path = exp_dir / "field_notes.md"
    if not notes_path.exists():
        raise SystemExit(
            f"No field_notes.md in {exp_dir}. Paste your LLM response there first."
        )

    field_notes = notes_path.read_text()
    spec = extract_audio_spec(field_notes)
    (exp_dir / "audio_spec.json").write_text(json.dumps(spec, indent=2))

    print(f"Rendering audio...")
    samples = render_spec(spec, seed=seed)
    write_wav(samples, str(exp_dir / "audio.wav"))

    # Extract system name
    m = re.search(r"###?\s*1\.?\s*System name\s*\n\s*(.+?)(?:\n|$)", field_notes)
    system_name = m.group(1).strip() if m else f"Expedition {expedition_number:03d}"

    coords = json.loads((exp_dir / "coords.json").read_text())
    rhythm_type = spec.get("rhythm_system", {}).get("type", "?")
    n_voices = len(spec.get("voices", []))
    duration = spec.get("duration_seconds", 0)

    (exp_dir / "index.html").write_text(
        make_index_html(expedition_number, system_name, coords["curiosity_score"],
                        duration, n_voices, rhythm_type)
    )

    print(f"\n✓ Expedition {expedition_number:03d} finalized: {exp_dir}")
    print(f"  system: {system_name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 -m loop.finalize <expedition_number>")
        sys.exit(1)
    finalize(int(sys.argv[1]))
