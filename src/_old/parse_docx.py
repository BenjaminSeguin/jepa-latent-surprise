import os
import docx
from typing import Tuple


def extract_text(docx_path: str) -> str:
    """Extracts clean text from a .docx file."""
    doc = docx.Document(docx_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)


def extract_texts_from_folder(folder_path: str) -> Tuple[str, str, str]:
    """
    Expects 3 .docx files in the folder: intro_*.docx, body_*.docx, qna_*.docx
    Returns (intro_text, body_text, qna_text)
    """
    intro_file = next((f for f in os.listdir(folder_path) if f.startswith("intro") and f.endswith(".docx")), None)
    body_file = next((f for f in os.listdir(folder_path) if f.startswith("body") and f.endswith(".docx")), None)
    qna_file = next((f for f in os.listdir(folder_path) if f.startswith("qna") and f.endswith(".docx")), None)

    if not all([intro_file, body_file, qna_file]):
        raise FileNotFoundError("Missing one or more required .docx files in the folder (intro, body, qna).")

    intro_text = extract_text(os.path.join(folder_path, intro_file))
    body_text = extract_text(os.path.join(folder_path, body_file))
    qna_text = extract_text(os.path.join(folder_path, qna_file))

    return intro_text, body_text, qna_text