# Lab — Large Language Models (LLM)

**Master 2 VMI — Multi-modalité et IA générative (IFLCE055)**

Ce dossier contient le TP sur l'adaptation de modèles de langage pré-entraînés (LLMs) pour une tâche de **classification de sentiments**.

---

## 🚀 Lancer sur Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZTCXM_edq0ysQlmLN5ZBcO8p9mmLQL5w?usp=sharing)

---

## 🎯 Objectifs du TP

Explorer et comparer **trois stratégies** d'adaptation d'un LLM à une tâche aval :

| Stratégie | Description |
|-----------|-------------|
| **Inference without training** | Utilisation du modèle pré-entraîné tel quel (zéro entraînement) |
| **Linear Probing** | Gel du backbone, entraînement uniquement de la tête de classification |
| **Fine-tuning** | Complet (tous les paramètres) ou partiel (certaines couches gelées) |

Une section dédiée à l'**analyse des tokens, IDs et embeddings** est également incluse.

---

## 🧠 Modèle et données

- **Dataset :** `cornell-movie-review-data/rotten_tomatoes` (Hugging Face)
  - Train : 8 530 | Validation : 1 066 | Test : 1 066
- **Modèle :** `cardiffnlp/twitter-roberta-base-sentiment-latest` (RoBERTa)
- **Tâche :** Classification binaire (NEGATIVE / POSITIVE)

---

## 📁 Structure du projet

```
LLM_LAB/
├── notebook/
│   └── LLM_Lab.ipynb           # Notebook principal
├── report/
│   └── TP_LLM.pdf              # Rapport final
└── README.md
```

---

## 📊 Résultats (jeu de test)

| Approche | Accuracy | F1-score |
|----------|----------|----------|
| Inference sans entraînement | 0.751 | 0.742 |
| Linear probing | 0.836 | 0.835 |
| Fine-tuning complet | **0.877** | **0.874** |
| Fine-tuning partiel | 0.875 | 0.872 |

Le fine-tuning partiel offre un excellent compromis entre performance et coût computationnel.

---

## ⚙️ Dépendances

- `transformers`, `datasets`
- `torch`, `scikit-learn`, `matplotlib`

Datasets et modèles publics — aucun token Hugging Face requis.

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
