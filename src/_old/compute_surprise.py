import os
import numpy as np
from scipy.spatial.distance import cosine, euclidean

def compute_and_save_surprise(embedding_path, output_dir):
    """
    Calcule les distances entre embeddings (intro, body, qna) pour quantifier la surprise latente.
    Sauvegarde les résultats dans un fichier JSON.

    Args:
        embedding_path (str): Chemin vers le fichier .npz contenant les embeddings.
        output_dir (str): Dossier où sauvegarder le fichier de surprise.

    Returns:
        str: Chemin du fichier JSON sauvegardé.
    """
    data = np.load(embedding_path)

    intro = data["intro"]
    body = data["body"]
    qna = data["qna"]

    # Calcul des surprises (comparaison Q&A vs intro et Q&A vs body)
    results = {
        "cosine_intro_qna": float(cosine(intro, qna)),
        "euclidean_intro_qna": float(euclidean(intro, qna)),
        "cosine_body_qna": float(cosine(body, qna)),
        "euclidean_body_qna": float(euclidean(body, qna))
    }

    # Création du chemin de sauvegarde
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(embedding_path))[0].replace("_embeddings", "")
    save_path = os.path.join(output_dir, f"{base_name}_surprise.json")

    # Sauvegarde dans un fichier JSON
    import json
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return save_path