import numpy as np
import json
from pathlib import Path
from sklearn.metrics.pairwise import cosine_distances

EMBEDDING_DIR = Path("data/embeddings")
RESULTS_DIR = Path("data/results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def mean_cosine_distance(A, B):
    """Average pairwise cosine distance between two sets of embeddings"""
    if len(A) == 0 or len(B) == 0:
        return None
    dist_matrix = cosine_distances(A, B)
    return float(np.mean(dist_matrix))

for file_path in EMBEDDING_DIR.glob("*.npz"):
    print(f"Computing surprise for {file_path.name}")

    data = np.load(file_path, allow_pickle=True)

    intro = data["intro"]
    body = data["body"]
    qna = data["qna"]

    # Compute distances
    s_intro_qna = mean_cosine_distance(intro, qna)
    s_body_qna = mean_cosine_distance(body, qna)
    s_intro_body = mean_cosine_distance(intro, body)

    output = {
        "basename": file_path.stem,
        "surprise_intro_qna": s_intro_qna,
        "surprise_body_qna": s_body_qna,
        "surprise_intro_body": s_intro_body,
    }

    # Save as JSON
    out_path = RESULTS_DIR / f"{file_path.stem}_surprise.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Surprise saved to {out_path}")