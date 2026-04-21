"""Project morphospace points to 2D via classical MDS.

Computes the NxN pairwise distance matrix using the project's hybrid
(continuous + categorical) metric, then runs classical multidimensional
scaling to produce 2D coordinates. Pure numpy — no sklearn, no umap-learn.

Writes `viewer/projection.json` containing:
  - corpus: [{name, id, is_anchor, x, y, continuous, categorical, notes, ...}]
  - expeditions: [{name, id, x, y, curiosity_score, ...}]  (empty until runs exist)
  - dim_ranges: {min_x, max_x, min_y, max_y}
  - method: "classical_mds"

Usage: python3 viewer/project.py
"""

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
from loop.distance import point_distance  # noqa: E402


def load_corpus() -> list:
    with open(ROOT / "corpus" / "corpus.json") as f:
        return json.load(f)["traditions"]


def load_expeditions() -> list:
    exps = []
    for d in sorted((ROOT / "expeditions").glob("[0-9]*")):
        coords_path = d / "coords.json"
        if not coords_path.exists():
            continue
        coords = json.loads(coords_path.read_text())
        notes_path = d / "field_notes.md"
        name = f"Expedition {coords['expedition_number']:03d}"
        if notes_path.exists():
            import re
            m = re.search(r"###?\s*1\.?\s*System name\s*\n\s*(.+?)(?:\n|$)", notes_path.read_text())
            if m:
                name = m.group(1).strip()
        exps.append({
            "id": d.name,
            "name": name,
            "continuous": coords["continuous"],
            "categorical": coords["categorical"],
            "curiosity_score": coords["curiosity_score"],
        })
    return exps


def compute_distance_matrix(points: list) -> np.ndarray:
    n = len(points)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            d = point_distance(
                points[i]["continuous"], points[i]["categorical"],
                points[j]["continuous"], points[j]["categorical"],
            )
            D[i, j] = d
            D[j, i] = d
    return D


def classical_mds(D: np.ndarray, dim: int = 2) -> np.ndarray:
    """Classical MDS (Torgerson scaling).

    Given an NxN distance matrix, return Nxdim embedding that preserves
    pairwise Euclidean distances as closely as possible.
    """
    n = D.shape[0]
    # Square the distances
    D2 = D ** 2
    # Double centering: B = -0.5 * J * D^2 * J  where J = I - (1/n) * 11^T
    J = np.eye(n) - np.ones((n, n)) / n
    B = -0.5 * J @ D2 @ J
    # Symmetrize for numerical stability
    B = (B + B.T) / 2
    # Eigendecomposition
    eigvals, eigvecs = np.linalg.eigh(B)
    # Sort descending
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]
    # Take top `dim` positive eigenvalues
    pos = eigvals[:dim].clip(min=0)
    return eigvecs[:, :dim] * np.sqrt(pos)


def project_all():
    corpus = load_corpus()
    expeditions = load_expeditions()
    all_points = corpus + expeditions

    print(f"Computing pairwise distances for {len(all_points)} points...", file=sys.stderr)
    D = compute_distance_matrix(all_points)
    print(f"Running classical MDS...", file=sys.stderr)
    coords = classical_mds(D, dim=2)

    # Normalize to roughly [-1, 1]
    coords = coords - coords.mean(axis=0)
    scale = np.max(np.abs(coords))
    if scale > 0:
        coords = coords / scale

    n_corpus = len(corpus)

    corpus_out = []
    for i, t in enumerate(corpus):
        corpus_out.append({
            "id": t["id"],
            "name": t["name"],
            "region": t.get("region", ""),
            "is_anchor": t.get("is_anchor", False),
            "x": float(coords[i, 0]),
            "y": float(coords[i, 1]),
            "continuous": t["continuous"],
            "categorical": t["categorical"],
            "notes": t.get("notes", ""),
        })

    expedition_out = []
    for i, e in enumerate(expeditions):
        idx = n_corpus + i
        expedition_out.append({
            "id": e["id"],
            "name": e["name"],
            "x": float(coords[idx, 0]),
            "y": float(coords[idx, 1]),
            "curiosity_score": e["curiosity_score"],
        })

    output = {
        "method": "classical_mds",
        "distance_metric": "0.6 × continuous_euclidean + 0.4 × categorical_hamming",
        "corpus_count": len(corpus),
        "expedition_count": len(expeditions),
        "corpus": corpus_out,
        "expeditions": expedition_out,
    }

    out_path = ROOT / "viewer" / "projection.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(output))
    print(f"Wrote {out_path}", file=sys.stderr)
    print(f"  {len(corpus)} corpus points + {len(expeditions)} expeditions", file=sys.stderr)


if __name__ == "__main__":
    project_all()
