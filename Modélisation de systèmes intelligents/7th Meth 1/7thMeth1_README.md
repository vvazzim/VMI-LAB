# Sujet 7 — Méthode 1  
## Classification de Whole Slide Images (WSI)

Ce dossier correspond au **projet de développement** du module **Modélisation de systèmes intelligents (M2 VMI)**.

Le travail présenté implémente la **Méthode 1 du Sujet 7**, telle que définie dans l'énoncé officiel des projets : classification de lames histologiques en **supervision faible** (annotations WSI-level uniquement).

---

## 🎯 Objectif

Développer et évaluer une méthode de **classification de lames histologiques (WSI)** dans un cadre de **supervision faible**, où seules des annotations au niveau WSI sont disponibles.

L'objectif est méthodologique : proposer un pipeline cohérent, scientifiquement valide et correctement évalué.

---

## 🗂 Structure du dossier

```
7th Meth 1/
├── 7thMeth1_README.md           # Ce fichier
│
├── notebooks/                   # Pipeline expérimental (exécution sur Kaggle)
│   ├── 00-preproc-camelyon-patch-extraction (1).ipynb   # Tiling + filtrage
│   ├── 01-wsi-level-stratified-split (1).ipynb         # Split train/val/test
│   ├── 02-patch-embedding-extraction-vit-checkpoint (5).ipynb  # Embeddings DINOv2
│   ├── 03-str-randomwalk-sequence-generation-dinoembedv4 (2).ipynb  # SPPR
│   ├── 04-str-dinov2-training-v4-1 (4).ipynb           # Entraînement Transformer
│   ├── 05-dinov2-embeddings-extraction (1).ipynb       # Évaluation
│   └── Notebooks_README.md
│
├── report/
│   ├── Rapport_SPPR.pdf         # Rapport scientifique
│   └── Report_README.md
│
└── slides/
    ├── Classification_de_lames_histologiques_by_Wassim_V4.pdf  # Présentation orale
    └── Slides_README.md
```

---

## 🔬 Principe général du pipeline

1. **Découpage** des WSIs en patchs (256×256, filtrage fond/tissu via Laplacien + HSV)
2. **Extraction d'embeddings** patch-level avec DINOv2 (ViT pré-entraîné)
3. **Génération de chemins spatiaux** (SPPR — random walks sur la grille de patchs)
4. **Modélisation séquentielle** par Transformer sur les séquences d'embeddings
5. **Agrégation WSI-level** (MIL) pour la décision finale

Aucune supervision patch-level n'est utilisée.

---

## 📦 Données et plateforme

- **Dataset :** Camelyon16 / Camelyon17 (WSI H&E, normales vs tumeurs)
- **Plateforme d'exécution :** Kaggle (GPU)
- **Entrées :** `camelyon-normal6`, `camelyon-tumor4` (ou datasets pré-traités issus des étapes précédentes)

---

## ⚠️ Remarques

- Décisions exclusivement WSI-level
- Partitionnement strict WSI/patient (pas de fuite de données)
- Résultats interprétés avec prudence (dataset réduit)
- Objectif méthodologique et reproductibilité

---

## 📄 Livrables

| Fichier | Description |
|---------|-------------|
| `report/Rapport_SPPR.pdf` | Rapport scientifique complet |
| `slides/Classification_de_lames_histologiques_by_Wassim_V4.pdf` | Présentation orale |

---

## 👤 Auteur

**Mohammed Wassim Chikhi**  
Master 2 VMI — Université Paris Cité  
Année académique : 2025–2026
