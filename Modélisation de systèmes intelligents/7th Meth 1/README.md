# Sujet 7 — Méthode 1  
## Classification de Whole Slide Images (WSI)

Ce dossier correspond au **projet de développement** du module
**Modélisation de systèmes intelligents (M2 VMI)**.

Le travail présenté ici implémente la **Méthode 1 du Sujet 7**, telle que définie
dans l’énoncé officiel des projets du module.

---

## 🎯 Objectif

Développer et évaluer une méthode de **classification de lames histologiques (WSI)**
dans un cadre de **supervision faible**, où seules des annotations au niveau de la lame
sont disponibles.

L’objectif est méthodologique : proposer un pipeline cohérent, scientifiquement valide,
et correctement évalué, plutôt que d’optimiser une performance absolue.

---

## 🗂 Structure du dossier

```
7th Meth 1/
├── notebooks/     # Notebooks du pipeline expérimental
├── report/        # Rapport de développement
├── slides/        # Slides de présentation
└── ReadMe.md
```

---

## 🔬 Principe général de la méthode

- Découpage des WSIs en patchs
- Extraction d’embeddings patch-level (ViT / DINOv2)
- Construction de chemins spatiaux de patchs (random walks / SPPR)
- Modélisation séquentielle par Transformer
- Agrégation WSI-level (MIL)

Aucune supervision patch-level n’est utilisée.

---

## ⚠️ Remarques importantes

- Les décisions sont prises **exclusivement au niveau WSI**
- Les résultats doivent être interprétés avec prudence si le jeu de test est de petite taille
- Le protocole expérimental respecte strictement les splits WSI/patient

---

## 👤 Auteur

Mohammed Wassim Chikhi  
Master 2 VMI — Université Paris Cité
