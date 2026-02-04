# 🧠 Vision & Machines Intelligentes (VMI) — Master 2 Lab Repository

**Auteur :** Wassim CHIKHI  
**Année :** 2025  
**Master 2 — Parcours Vision et Machines Intelligentes (VMI)**  
**Université Paris Cité**

---

## 🎯 Objectif du dépôt

Ce dépôt constitue **l'ensemble des travaux du Master 2 VMI** : Travaux Pratiques, projets méthodologiques et rapports scientifiques réalisés tout au long de l'année universitaire.

**Objectif :** offrir une **organisation claire, reproductible et documentée** de tous les projets — notebooks Colab, pipelines Python, scripts ICY, rapports LaTeX — pour servir de référence et de portfolio académique.

---

## 🗂️ Structure générale

```
Tp-VMI-Wassim/
│
├── reco-forme-avancee/          # Reconnaissance de Formes Avancée
│   └── tp1-fuzzy-cmeans/
│       ├── notebooks/
│       ├── data/
│       └── rapport/
│
├── deep-learning/               # Deep Learning
│   ├── tp1-mlp-mnist/
│   ├── tp2-cnn-transfer-learning/
│   └── tp3-self-supervised-learning/
│
├── imagerie-biomed/             # Imagerie Biomédicale
│   ├── Tp1-Modalities/
│   ├── TP2-Spots/
│   └── TP3/                     # Segmentation & Tracking HeLa
│
├── 3d/                          # Imagerie 3D / Photogrammétrie
│   ├── tp1/
│   │   └── TP2 Drone GCP/       # Photos drone + GCPs
│   └── Projet Final/
│
├── Méthodologie et imageries thématiques/
│   ├── TP2 Color Supp/          # Couleur, déconvolution H&E / H-DAB
│   └── TP3 Efficient DL/        # Knowledge Distillation
│
├── Modélisation de systèmes intelligents/
│   ├── 7th Meth 1/              # Classification WSI (DINOv2, SPPR)
│   ├── state of the art/
│   └── UNI/
│
├── Multi-modalité et IA générative/
│   ├── LLM_LAB/                 # LLM, classification sentiments
│   ├── TP2 CLIP/                # CLIP multimodal, ROCO, CIFAR10
│   └── TP 3 GaN-VAE/            # VAE / GAN (sprites Pokémon)
│
├── SeqVid/                      # Séquences Vidéo
│   ├── TP1/                     # Calibration caméra
│   ├── TP2/                     # Flot optique
│   └── TP3/                     # Multi-object tracking (CSRT, YOLO)
│
└── docs/
    └── templates/
```

---

## 🧩 Modules et TPs réalisés

### 🧩 Reconnaissance de Formes Avancée
- **TP1 — Fuzzy C-Means (Segmentation floue)**  
  Implémentation *from scratch* du Fuzzy C-Means appliqué à la segmentation d'images (GRAY C=2, RGB C=3).  
  Notebook : `reco-forme-avancee/tp1-fuzzy-cmeans/notebooks/TP_Fuzzy_C_Means3_0.ipynb`  
  Rapport : `reco-forme-avancee/tp1-fuzzy-cmeans/rapport/rapport_fcm.pdf`

---

### 🤖 Deep Learning
- **TP1 — MLP sur MNIST** : introduction au Deep Learning supervisé (classification).  
- **TP2 — CNN & Transfer Learning (ResNet18)** : fine-tuning sur datasets standards.  
- **TP3 — Self-Supervised Learning (SSL)** : comparaison de tâches prétextes (Rotation, Relative Patch, SimCLR, Inpainting) sur CIFAR-10 / STL-10.  
  Rapport : `deep-learning/tp3-self-supervised-learning/rapport/rapport_SSL.pdf`

---

### 🧬 Imagerie Biomédicale
- **TP1 — Imagerie Photonique : Modalités et Photoblanchiment**  
  Étude des modalités de microscopie optique (champ clair, fluorescence, confocale) et mesure du photoblanchiment.  
  Rapport : `imagerie-biomed/Tp1-Modalities/report/TP_1_BioImg_Wassim.pdf`

- **TP2 — Détection et Tracking de Spots sous ICY**  
  Pipeline ICY (Wavelet Spot Detector + Kalman) + scripts Python/Jython pour automatisation.  
  Rapport : `imagerie-biomed/TP2-Spots/report/TP_2_BioImg_Wassim.pdf`

- **TP3 — Segmentation et Tracking de cellules HeLa**  
  Segmentation avec **Cellpose** + tracking avec **TrackPy** ; comparaison approche ICY vs Python.  
  Rapport : `imagerie-biomed/TP3/report/TP3_CellSegmentation_Tracking_Wassim.pdf`

---

### 🕹️ Imagerie 3D
- **tp1 — TP2 Drone GCP** : données photogrammétriques (photos drone P4 RTK, GCPs).  
- **Projet Final** : livrables et rendus du projet de photogrammétrie 3D.

---

### 📐 Méthodologie et Imageries Thématiques
- **TP2 — Couleur** : espaces RGB/CIELab, luminance, déconvolution Ruifrok & Johnston (H&E, H-DAB).  
  Rapport : `Méthodologie et imageries thématiques/TP2 Color Supp/report/TP_Color_Wassim_compressed.pdf`

- **TP3 — Efficient DL (Knowledge Distillation)** : ResNet50 → ResNet18 sur CIFAR-10 (logits + feature maps).  
  Rapport : `Méthodologie et imageries thématiques/TP3 Efficient DL/report/KD_LAB.pdf`

---

### 🔬 Modélisation de Systèmes Intelligents
- **Projet — Classification de lames histologiques (WSI)**  
  Pipeline DINOv2 + SPPR (chemins aléatoires) pour classification WSI en supervision faible.  
  Rapport : `Modélisation de systèmes intelligents/7th Meth 1/report/Rapport_SPPR.pdf`  
  Slides : `Modélisation de systèmes intelligents/7th Meth 1/slides/Classification_de_lames_histologiques_by_Wassim_V4.pdf`  
- **État de l'art** et article UNI dans les sous-dossiers dédiés.

---

### 🎨 Multi-modalité et IA Générative
- **LLM Lab** : adaptation de RoBERTa pour classification de sentiments (inference, linear probing, fine-tuning).  
  Rapport : `Multi-modalité et IA générative/LLM_LAB/report/TP_LLM.pdf`

- **TP2 — CLIP** : apprentissage multimodal texte-image, fine-tuning sur ROCO, zero-shot CIFAR10.  
  Rapport : `Multi-modalité et IA générative/TP2 CLIP/repport/TP2_CLIP_r.pdf`

- **TP3 — GAN & VAE** : génération de sprites Pokémon (DCGAN, VAE convolutionnel).  
  Rapport : `Multi-modalité et IA générative/TP 3 GaN-VAE/TP_GaN_VAE_WASSIM (1).pdf`

---

### 🎬 Séquences Vidéo (SeqVid)
- **TP1** : Calibration caméra.  
- **TP2** : Flot optique.  
- **TP3 — Multi-Object Tracking** : CSRT (OpenCV), YOLOv8 + IoU, bonus Kalman.  
  Rapport : `SeqVid/TP3/report/TP3_SeqVid_Wassim.pdf`

---

## ⚙️ Workflow de travail

### Sur **Google Colab**
1. Ouvrir le notebook via le badge « Open in Colab ».  
2. Monter le Drive :  
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Charger les données depuis Drive / URL.  
4. Exécuter les cellules, documenter, sauvegarder.  
5. Exporter le notebook → « Save a copy to GitHub ».

### Sur **ICY / Local**
- Lancer ICY, importer les images `.tif`.  
- Utiliser les plugins : *Spot Detector*, *Track Manager*, *ROI Statistics*.  
- Exporter les résultats (.xml, .xlsx) vers le dossier `result/`.

---

## 🧾 Rapports et documentation
- Chaque TP contient un **rapport LaTeX** compilé en PDF dans `rapport/` ou `report/`.  
- Figures, tables et légendes sont reliées aux données ICY, NumPy ou Matplotlib selon le TP.  
- Chaque module dispose de son propre `README.md` pour les détails spécifiques.  
- Modèles (templates) pour TPs et rapports : `docs/templates/` (voir `docs/README.md`).

---

## ⚙️ Environnement

Chaque module peut définir ses propres dépendances. Exemples :

**SeqVid TP3** (tracking) :
```bash
conda create -n seqvid python=3.10
conda activate seqvid
pip install -r SeqVid/TP3/requirements.txt
```

**Librairies courantes** :  
`numpy`, `matplotlib`, `scikit-image`, `torch`, `torchvision`, `opencv-python`, `tifffile`, `scipy`, `ultralytics`, `transformers`, `cellpose`, `trackpy`.

---

## 📘 Références principales
- Olivo-Marin, *Wavelet-based detection of spots and features in biological images*, IEEE, 2002.  
- Ronneberger et al., *U-Net: Convolutional Networks for Biomedical Image Segmentation*, MICCAI, 2015.  
- Gidaris et al., *Unsupervised Representation Learning by Predicting Image Rotations*, 2018.  
- Chen et al., *SimCLR: A Simple Framework for Contrastive Learning*, 2020.  
- Ruifrok & Johnston, *Quantification of histochemical staining by color deconvolution*, J Histochem Cytochem, 2001.  
- Cours Master 2 VMI — Université Paris Cité.

---

## ⚖️ Licence
Projet académique — **Licence MIT**  
© 2025 — *Wassim CHIKHI*
