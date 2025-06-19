from sentence_transformers import SentenceTransformer
import json
import numpy as np
from pathlib import Path

# === Parameters ===
INPUT_DIR = Path("data/processed")
OUTPUT_DIR = Path("data/embeddings")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Choix du modèle
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# === Encoding Function ===
def encode_section(text: str):
    paragraphs = [p for p in text.split("\n") if p.strip()]
    embeddings = model.encode(paragraphs)
    return embeddings, paragraphs

# === Loop over files ===
for file_path in INPUT_DIR.glob("*.json"):
    print(f"Processing {file_path.name}")

    with open(file_path, "r", encoding="utf-8") as f:
        doc = json.load(f)

    # Encode each section
    intro_embeddings, intro_texts = encode_section(doc["intro"])
    body_embeddings, body_texts = encode_section(doc["body"])
    qna_embeddings, qna_texts = encode_section(doc["qna"])

    # Save all embeddings
    basename = doc["basename"]
    output_path = OUTPUT_DIR / f"{basename}.npz"
    np.savez_compressed(
        output_path,
        intro=intro_embeddings,
        body=body_embeddings,
        qna=qna_embeddings,
        intro_text=intro_texts,
        body_text=body_texts,
        qna_text=qna_texts,
    )

    print(f"Saved embeddings to: {output_path}")