# 🧠 Latent Surprise in Earnings Calls – preJEPA Prototype

This repository contains the prototype of a pipeline designed to detect **implicit surprise** in earnings call transcripts, by measuring semantic dissociation between the **prepared remarks** (`intro`, `body`) and the **Q&A session**.  
This work is a stepping stone toward a future implementation of a **Joint Embedding Predictive Architecture (JEPA)** for predictive modeling of financial communications.

---

## 🎯 Goal

The goal is to uncover **non-obvious, latent signals** in earnings calls — especially in the Q&A — that are not captured by traditional quantitative metrics (EPS surprise, guidance) but may explain **market reaction** or highlight **information asymmetry**.

---

## 🛠️ What’s in this prototype?

✔️ Intelligent segmentation of earnings call transcripts (`intro`, `body`, `qna`)  
✔️ Zero-shot classification using `facebook/bart-large-mnli`  
✔️ Embedding generation with `all-MiniLM-L6-v2`  
✔️ Semantic dissociation scoring (cosine distance) between sections  
✔️ Structured export and pipeline-ready `.json` / `.npz` files  
✔️ Filtering of metadata & short utterances (`meta`)  
✔️ Generation of a **latent surprise score** per document

---

## 🔬 What this is *not* (yet)

This is **not yet a JEPA**, but a **pre-JEPA** phase:
- No prediction of latent space yet (no `g(f(x)) ≈ f(y)`)
- No learned latent filtering or contrastive learning
- No supervised or autoregressive generation

---

## 📁 Folder structure

```text
data/
├── raw/                   # .docx earnings call transcripts
├── annotated_blocks/      # per-paragraph zero-shot classification
├── processed_structured/  # structured JSONs (intro/body/qna)
├── embeddings/            # .npz embeddings
├── results/               # JSONs with surprise scores
src/
├── parse_docx.py
├── zero_shot_parser.py
├── assemble_sections.py
├── generate_embeddings.py
├── compute_surprise.py
```

---

## 📊 Example output

```json
{
  "basename": "apple_q2_2025",
  "surprise_intro_qna": 0.832,
  "surprise_body_qna": 0.816,
  "surprise_intro_body": 0.787
}
```

## 🚀 Roadmap
✅ Pre-JEPA dissociation scoring (this repo)

🔜 Trainable JEPA to predict Q&A latent space from intro+body

🔜 Latent error filtering module (topic-sensitive or contrastive)

🔜 Correlation with market variables (return, volatility)

🔜 Extension to generative hallucination: “what questions should have been asked?”

## 📚 Citation & academic intent
This project is part of a prospective research thesis (CIFRE) on representation learning and surprise detection in financial communication, using self-supervised predictive architectures inspired by JEPA.
If you're interested in collaboration or supervision, feel free to open an issue or contact me directly.

## 🧑‍💻 Author
Benjamin Séguin
HEC Montréal, Quantitative Finance & AI
benjamin.seguin@hec.ca
