# Modélisation de systèmes intelligents  
## Master 2 Vision et Machines Intelligentes (VMI) — Université Paris Cité

Ce dossier regroupe les travaux réalisés dans le cadre du module **Modélisation de systèmes intelligents** du Master 2 VMI.

Le module est structuré autour d'un projet de recherche appliquée visant à mettre en œuvre une démarche scientifique complète : étude de l'état de l'art, développement méthodologique, évaluation expérimentale et restitution écrite et orale.

---

## 🎯 Objectifs du module

- Analyser et synthétiser l'état de l'art sur un thème scientifique
- Implémenter une méthode inspirée de travaux de recherche récents
- Définir un protocole expérimental rigoureux (données, métriques, validation)
- Évaluer et discuter les résultats de manière critique
- Structurer et documenter un dépôt Git académique

---

## 🗂 Organisation complète

```
Modélisation de systèmes intelligents/
│
├── ModSysInt_README.md          # Ce fichier
│
├── 7th Meth 1/                  # Projet de développement (Sujet 7 – Méthode 1)
│   ├── 7thMeth1_README.md       # Description du projet WSI
│   ├── notebooks/               # Pipeline expérimental (6 notebooks)
│   │   ├── 00-preproc-camelyon-patch-extraction (1).ipynb
│   │   ├── 01-wsi-level-stratified-split (1).ipynb
│   │   ├── 02-patch-embedding-extraction-vit-checkpoint (5).ipynb
│   │   ├── 03-str-randomwalk-sequence-generation-dinoembedv4 (2).ipynb
│   │   ├── 04-str-dinov2-training-v4-1 (4).ipynb
│   │   ├── 05-dinov2-embeddings-extraction (1).ipynb
│   │   └── Notebooks_README.md
│   ├── report/
│   │   ├── Rapport_SPPR.pdf     # Rapport scientifique
│   │   └── Report_README.md
│   └── slides/
│       ├── Classification_de_lames_histologiques_by_Wassim_V4.pdf
│       └── Slides_README.md
│
├── state of the art/            # État de l'art
│   ├── Etat_de_l_art_VIEEE.pdf  # Synthèse (~15 pages, format IEEE)
│   └── README.md
│
└── UNI/                         # Article scientifique de référence
    ├── UNI____Nature_Medicine_2024_V5_1.pdf
    └── UNI_README.md
```

---

## 📌 Sujet traité

**Sujet 7 — Apprentissage de biomarqueurs en oncologie à partir de Whole Slide Images (WSI)**  
Méthode développée : **Méthode 1** (SPPR — Spatial Path-based Representation)

**Dataset :** Camelyon16 / Camelyon17 (lames H&E, tumeurs vs normales)

---

## 📚 Parcours de lecture recommandé

1. **État de l'art** (`state of the art/`) — Contexte scientifique et familles de méthodes
2. **Article UNI** (`UNI/`) — Référence pour les modèles fondation en pathologie
3. **Projet 7th Meth 1** (`7th Meth 1/`) — Implémentation et résultats

---

## 👤 Auteur

**Mohammed Wassim Chikhi**  
Master 2 VMI — Université Paris Cité  
Année académique : 2025–2026
