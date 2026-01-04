# Lab – Large Language Models (LLM)
**Master 2 Informatique – Parcours VMI**  
**Multi-modalité et IA générative (IFLCE055)**

Ce dépôt contient le notebook et le rapport associés au TP sur l’adaptation de modèles de langage pré‑entraînés (LLMs) pour une tâche de **classification de sentiments**.

---

## 🚀 Lancer le notebook sur Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZTCXM_edq0ysQlmLN5ZBcO8p9mmLQL5w?usp=sharing)

---

## 📌 Objectifs du TP

Explorer et comparer **trois stratégies** d’adaptation d’un LLM à une tâche aval :

1. **Inference without training**  
   Utilisation du modèle pré‑entraîné tel quel (zéro entraînement).
2. **Linear Probing**  
   Gel du backbone et entraînement uniquement de la tête de classification.
3. **Fine‑tuning**  
   - Fine‑tuning complet (tous les paramètres entraînables)  
   - Fine‑tuning partiel (certaines couches gelées)

Une section dédiée à l’**analyse des tokens, IDs et embeddings** est également incluse.

---

## 🧠 Modèle et données

- **Dataset** : `cornell-movie-review-data/rotten_tomatoes`  
  - Train : 8 530  
  - Validation : 1 066  
  - Test : 1 066  
- **Modèle** : `cardiffnlp/twitter-roberta-base-sentiment-latest` (RoBERTa)

La tâche cible est **binaire** (NEGATIVE / POSITIVE).  
La tête de classification du modèle est donc réinitialisée en 2 classes lorsque nécessaire.

---

## 📊 Métriques d’évaluation

Pour garantir une comparaison cohérente entre toutes les approches :

- **Accuracy** → performance quantitative globale  
- **F1‑score (binaire)** → qualité de la classification

Une **matrice de confusion** (fine‑tuning complet) et une **figure de comparaison globale**
(bar plot Accuracy / F1) sont incluses.

---

## 📁 Contenu du projet

```
.
├── LLM_Lab.ipynb              # Notebook principal (expériences complètes)
├── TP_LLM.pdf                 # Rapport final (LaTeX → PDF)
├── figures/
│   ├── performance_comparison.png
│   └── confusion_matrix_finetune.png
└── README.md
```

---

## ▶️ Exécution

Le notebook est conçu pour être exécuté **directement sur Google Colab**.

### Dépendances principales
- `transformers`
- `datasets`
- `torch`
- `scikit-learn`
- `matplotlib`

Les datasets et modèles utilisés sont **publics**.  
Aucun token Hugging Face n’est requis dans un environnement standard.

---

## 📝 Résumé des résultats (jeu de test)

| Approche | Accuracy | F1-score |
|--------|---------|----------|
| Inference sans entraînement | 0.751 | 0.742 |
| Linear probing | 0.836 | 0.835 |
| Fine‑tuning complet | 0.877 | 0.874 |
| Fine‑tuning partiel | 0.875 | 0.872 |

Les résultats montrent une amélioration progressive avec le degré d’adaptation du modèle,
le fine‑tuning partiel offrant un excellent compromis entre performance et coût computationnel.

---

## 👤 Auteur

**Wassim Chikhi**  
Master 2 Vision et Machines Intelligentes (VMI)  
Université Paris Cité — 2025/2026

---

## 📄 Licence

Ce projet est fourni dans un cadre académique (TP universitaire).
