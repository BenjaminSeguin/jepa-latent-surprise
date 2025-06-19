# JEPA-Latent-Surprise: Predicting Market Reaction to Earnings Calls via Latent Representations

Prototype de recherche mêlant autoencodeurs prédictifs (JEPA) et filtrage latent pour extraire des signaux de "surprise implicite" à partir des earnings calls d’entreprises cotées.

## Objectif
- Encoder les blocs narratifs d’un earnings call dans un espace latent
- Prédire l’évolution de ce signal latent entre l’intro et le Q&A
- Quantifier l’écart entre attente (`ẑ`) et réalisation (`z`) pour capter la surprise du discours
- Évaluer la corrélation avec le retour boursier post-call

## Statut
🛠️ Prototype en construction (Juin–Septembre 2025)

## À venir
- Première expérimentation sur 10 earnings calls
- Visualisations de l’espace latent
- Baseline de prédiction
- Filtrage séquentiel simplifié (Kalman)

## Auteur
Benjamin Seguin – MSc Financial Engineering, passionné d’IA et de recherche quantitative.