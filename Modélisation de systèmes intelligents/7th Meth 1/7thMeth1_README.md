# Sujet 7 — Méthode 1  
## Classification de Whole Slide Images (WSI)

Ce dossier correspond au **projet de développement** du module
**Modélisation de systèmes intelligents (M2 VMI)**.

Le travail présenté implémente la **Méthode 1 du Sujet 7**, telle que définie
dans l’énoncé officiel des projets.

---

## 🎯 Objectif

Développer et évaluer une méthode de **classification de lames histologiques (WSI)**
dans un cadre de **supervision faible**, où seules des annotations au niveau WSI
sont disponibles.

L’objectif est méthodologique : proposer un pipeline cohérent,
scientifiquement valide et correctement évalué.

---

## 🗂 Structure du dossier

7th Meth 1/
├── notebooks/     # Pipeline expérimental
├── report/        # Rapport scientifique
├── slides/        # Présentation orale
└── README.md

---

## 🔬 Principe général

- Découpage des WSIs en patchs
- Extraction d’embeddings patch-level (ViT / DINOv2)
- Génération de chemins spatiaux (SPPR / random walks)
- Modélisation séquentielle par Transformer
- Agrégation WSI-level (MIL)

Aucune supervision patch-level n’est utilisée.

---

## ⚠️ Remarques

- Décisions exclusivement WSI-level
- Résultats interprétés avec prudence (dataset réduit)
- Partitionnement strict WSI/patient

---

## 👤 Auteur

Mohammed Wassim Chikhi  
Master 2 VMI — Université Paris Cité
