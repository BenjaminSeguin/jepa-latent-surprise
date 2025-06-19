import docx
import json

def extract_text(docx_path):
    """Extracts clean text from a .docx file."""
    doc = docx.Document(docx_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)

# File paths
intro_path = "c:/Users/benj0/OneDrive - HEC Montréal/Desktop/jepa-latent-surprise/data/raw_docx/intro_apple_q2_2025.docx"
body_path = "c:/Users/benj0/OneDrive - HEC Montréal/Desktop/jepa-latent-surprise/data/raw_docx/body_apple_q2_2025.docx"
qna_path = "c:/Users/benj0/OneDrive - HEC Montréal/Desktop/jepa-latent-surprise/data/raw_docx/qna_apple_q2_2025.docx"

# Extract text from each section
intro_text = extract_text(intro_path)
body_text = extract_text(body_path)
qna_text = extract_text(qna_path)

# Build JSON structure
earnings_data = {
    "company": "Apple",
    "date": "2025-05-01",
    "intro": intro_text,
    "body": body_text,
    "qna": qna_text,
}

# Output to JSON file
output_path = "c:/Users/benj0/OneDrive - HEC Montréal/Desktop/jepa-latent-surprise/data/raw_json/apple_earnings_2025.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(earnings_data, f, indent=2, ensure_ascii=False)

print(f"✅ JSON file created: {output_path}")