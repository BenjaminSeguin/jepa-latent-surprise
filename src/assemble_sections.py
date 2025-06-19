import json
from pathlib import Path

# === Parameters ===
ANNOTATED_DIR = Path("data/annotated")  
OUTPUT_DIR = Path("data/processed")  
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Valid Labels
VALID_SECTIONS = ["intro", "body", "qna"]

# === Principal Function ===
def assemble_sections_from_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sections = {key: [] for key in VALID_SECTIONS}

    for item in data:
        label = item["label"]
        if label in sections:
            sections[label].append(item["text"])

    # Merge sections into a single structured document
    assembled = {
        "basename": json_path.stem.replace("_annotated", ""),
        "intro": "\n\n".join(sections["intro"]),
        "body": "\n\n".join(sections["body"]),
        "qna": "\n\n".join(sections["qna"]),
    }

    return assembled

# === File Treatment ===
for json_file in ANNOTATED_DIR.glob("*.json"):
    print(f"Processing {json_file.name}")
    result = assemble_sections_from_json(json_file)

    output_file = OUTPUT_DIR / f"{result['basename']}_structured.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Saved structured JSON: {output_file}")