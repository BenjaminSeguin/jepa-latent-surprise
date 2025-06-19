from docx import Document
from transformers import pipeline
from pathlib import Path
import json

# === Paramètres ===
DOCX_DIR = Path("data/raw")  # Dossier avec tes .docx
OUTPUT_DIR = Path("data/annotated")
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

# Modèle HuggingFace
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Labels plus explicites
label_map = {
    "opening disclaimer": "intro",
    "prepared remarks": "body",
    "questions and answers": "qna"
}
labels = list(label_map.keys())

# Taille des blocs
BLOCK_SIZE = 4

def extract_paragraphs(docx_path):
    doc = Document(docx_path)
    return [p.text.strip() for p in doc.paragraphs if p.text.strip()]

def split_into_blocks(paragraphs, size=4):
    blocks = []
    for i in range(0, len(paragraphs), size):
        block_paragraphs = paragraphs[i:i+size]
        text = " ".join(block_paragraphs)
        blocks.append((i, block_paragraphs, text))
    return blocks

def is_meta(text):
    """
    Règle simple pour détecter un paragraphe 'meta'
    """
    if len(text.split()) <= 3:
        return True
    if text.strip().startswith("[") and text.strip().endswith("]"):
        return True
    return False

def classify_blocks(blocks):
    annotated = []
    for start_idx, paras, block_text in blocks:
        pred = classifier(block_text, labels)
        label_explicit = pred["labels"][0]
        label = label_map[label_explicit]
        for p in paras:
            # Tag override
            if is_meta(p):
                assigned_label = "meta"
            else:
                assigned_label = label
            annotated.append({
                "text": p,
                "label": assigned_label,
                "scores": dict(zip(pred["labels"], pred["scores"]))
            })
    return annotated

# === Main processing ===
for docx_file in DOCX_DIR.glob("*.docx"):
    print(f"🗂️ Processing {docx_file.name}")
    paragraphs = extract_paragraphs(docx_file)
    blocks = split_into_blocks(paragraphs, size=BLOCK_SIZE)
    annotated = classify_blocks(blocks)

    out_path = OUTPUT_DIR / f"{docx_file.stem}_annotated.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(annotated, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved to {out_path}")