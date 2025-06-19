import json
import os
from sentence_transformers import SentenceTransformer
import numpy as np

# Read JSON file
with open("c:/Users/benj0/OneDrive - HEC Montréal/Desktop/jepa-latent-surprise/data/processed/apple_earnings_2025.json", encoding="utf-8") as f:
    data = json.load(f)

# Fast and reliable model for embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Extract and encode each section
intro_emb = model.encode(data["intro"])
body_emb = model.encode(data["body"])
qna_emb = model.encode(data["qna"])

# Embedding file path
embedding_path = "c:/Users/benj0/OneDrive - HEC Montréal/Desktop/jepa-latent-surprise/data/embeddings/embeddings_appleq2_2025.npz"

# Créer le dossier s’il n’existe pas
os.makedirs(os.path.dirname(embedding_path), exist_ok=True)

# Sauvegarder les embeddings
np.savez(embedding_path, intro=intro_emb, body=body_emb, qna=qna_emb)

print(f"✅ Embeddings saved to {embedding_path}")