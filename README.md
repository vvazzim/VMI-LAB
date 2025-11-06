# TPs IA — Organisation Colab-First
**Auteur :** <Ton Nom> · **Année :** 2025 · **Parcours :** M2 VMI

Ce repo contient **uniquement l'organisation** (notebooks vides, README, templates).  
**Pas de code local** : tout se fait sur **Google Colab** avec données sur **Drive** ou via URL.

## 📦 Arborescence
```
tp-ia-structure-only/
├─ reco-forme-avancee/
│  └─ tp1-fuzzy-cmeans/
│     ├─ notebooks/
│     ├─ data/        (placeholders + liens Drive/URL)
│     └─ rapport/
├─ deep-learning/
│  ├─ tp1-mlp-mnist/
│  └─ tp2-cnn-transfer-learning/
├─ imagerie-biomed/
│  └─ tp1-seg-medicale/
├─ 3d/
│  └─ tp1-bases/
└─ docs/templates/
```

## 🔑 Principes
- 1 TP = 1 dossier = 1 notebook principal `notebooks/TP_<nom>.ipynb` (squelette ici).
- **Données** : stockées sur Drive (ou via URL), ne pas committer les gros fichiers.
- **Résultats** : screenshots/figures importés dans `rapport/` (markdown).
- **Badge Colab** : chaque README de TP a un badge “Open in Colab” pointant vers *ton* repo une fois créé.

## 🚦 Priorités
1) **Reco** — TP1: Fuzzy C-Means *(d’abord)*  
2) **DL** — TP1: MLP (MNIST)  
3) **DL** — TP2: CNN & Transfer Learning

## 🧭 Workflow Colab recommandé
1. Ouvrir le notebook depuis GitHub (badge Colab).  
2. Monter Drive (`from google.colab import drive; drive.mount('/content/drive')`).  
3. Charger les données depuis Drive ou URL.  
4. Travailler et **sauvegarder** le notebook sur **Drive**, puis **File ▸ Save a copy to GitHub** (versioning).  
5. Exporter 2–3 figures clés vers `rapport/` et compléter `rapport.md`.

## 🗂️ Templates
Dans `docs/templates/` :  
- `README_TP.md` : README par TP (copier/coller).  
- `RAPPORT_template.md` : modèle court de rapport.  
- `COLAB_header.md` : entête à coller dans le 1er bloc markdown.

---
Licence MIT — © <Ton Nom>, 2025
# Tp-VMI-Wassim
