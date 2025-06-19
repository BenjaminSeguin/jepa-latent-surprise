import os
import json

def create_json_file(company_name, date, texts_dict, output_dir):
    """
    Crée un fichier JSON structuré à partir des textes extraits.
    
    Args:
        company_name (str): Nom de l'entreprise (ex: "Apple").
        date (str): Date du call au format YYYY-MM-DD.
        texts_dict (dict): Dictionnaire contenant les clés 'intro', 'body', 'qna' et les textes associés.
        output_dir (str): Dossier où sauvegarder le JSON.
    
    Returns:
        str: Chemin complet du fichier JSON généré.
    """
    assert all(k in texts_dict for k in ['intro', 'body', 'qna']), "Missing sections in texts_dict"

    json_data = {
        "company": company_name,
        "date": date,
        "intro": texts_dict["intro"],
        "body": texts_dict["body"],
        "qna": texts_dict["qna"]
    }

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{company_name.lower()}_{date}.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    return output_path
