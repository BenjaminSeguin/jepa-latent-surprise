import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer

def generate_and_save_embeddings(json_path, output_dir, model_name="all-mpnet-base-v2"):
    """
    Encode le contenu textuel du fichier JSON et sauvegarde les embeddings.
    
    Args:
        json_path (str): Chemin vers le fichier JSON (contenant intro, body, qna).
        output_dir (str): Dossier où sauvegarder le fichier .npz.
        model_name (str): Modèle SentenceTransformer à utiliser.

    Returns:
        str: Chemin du fichier .npz sauvegardé.
    """
    # Charger le JSON
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = {
        "intro": data["intro"],
        "body": data["body"],
        "qna": data["qna"]
    }

    # Encoder les textes
    model = SentenceTransformer(model_name)
    embeddings = {section: model.encode(content) for section, content in texts.items()}

    # Créer le chemin de sauvegarde
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(json_path))[0]
    save_path = os.path.join(output_dir, f"{base_name}_embeddings.npz")

    # Sauvegarder les embeddings
    np.savez(save_path, **embeddings)

    return save_path