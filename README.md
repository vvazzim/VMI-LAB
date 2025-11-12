# 🧠 Travaux Pratiques — Vision & Machines Intelligentes (VMI)
**Auteur :** Wassim CHIKHI  
**Année :** 2025  
**Master 2 — Parcours Vision et Machines Intelligentes (VMI)**  
**Université Paris Cité**

---

## 🎯 Objectif du dépôt
Ce dépôt regroupe **l’ensemble des Travaux Pratiques du Master 2 VMI**, répartis en quatre grands modules :  
- 🧩 **Reconnaissance de Formes Avancée (RecoForme)**  
- 🤖 **Deep Learning (DL)**  
- 🧬 **Imagerie Biomédicale (BioImg)**  
- 🕹️ **Imagerie 3D (3D Vision)**  

L’objectif est de proposer une **organisation claire, reproductible et documentée** de tous les TPs réalisés en Colab, ICY ou Python.

---

## 🗂️ Structure générale
```
Tp-VMI-Wassim/
├─ reco-forme-avancee/
│  └─ tp1-fuzzy-cmeans/
│     ├─ notebooks/
│     ├─ data/
│     └─ rapport/
│
├─ deep-learning/
│  ├─ tp1-mlp-mnist/
│  ├─ tp2-cnn-transfer-learning/
│  └─ tp3-self-supervised-learning/
│
├─ imagerie-biomed/
│  ├─ tp1-modalities/
│  ├─ tp2-spots/
│  └─ tp3-segmentation/ (à venir)
│
├─ 3d/
│  └─ tp1-bases/
│
└─ docs/templates/
```

---

## 🧩 Modules et TPs réalisés

### 🧠 Reconnaissance de Formes Avancée
- **TP1 — Fuzzy C-Means (Segmentation floue)**  
  Implémentation Python du Fuzzy C-Means appliqué à la segmentation d’images.  
  Notebook disponible sous :  
  `reco-forme-avancee/tp1-fuzzy-cmeans/notebooks/FCM_TP_Etudiant.ipynb`

---

### 🤖 Deep Learning
- **TP1 — MLP sur MNIST** : introduction au Deep Learning supervisé (classification simple).  
- **TP2 — CNN & Transfer Learning (ResNet18)** : apprentissage par fine-tuning.  
- **TP3 — Self-Supervised Learning (SSL)** : comparaison de tâches prétextes (Rotation, Relative Patch, SimCLR, Inpainting).  
  Rapport : `deep-learning/tp3-self-supervised-learning/rapport/CHIKHI_Wassim_TP_SSL_VMI2025.pdf`

---

### 🧬 Imagerie Biomédicale
- **TP1 — Imagerie Photonique : Modalités et Fluorescence**  
  Étude des principes de microscopie optique et du photoblanchiment.  
  Rapport : `imagerie-biomed/tp1-modalities/report/TP_1_BioImg.pdf`

- **TP2 — Détection et Tracking de Spots sous ICY**  
  Mise en œuvre d’un pipeline complet ICY (Wavelet Spot Detector + Kalman Tracking).  
  Rapport : `imagerie-biomed/tp2-spots/report/TP_2_BioImg_Wassim.pdf`

- **TP3 — Segmentation et Morphométrie (à venir)**  
  Application d’algorithmes de segmentation (U-Net, Watershed).

---

### 🕹️ Imagerie 3D
- **TP1 — Bases du traitement 3D**  
  Chargement, visualisation et analyse de nuages de points (Open3D, ICP).  
  *Prévu pour la fin du semestre.*

---

## ⚙️ Workflow de travail
### Sur **Google Colab**
1. Ouvrir le notebook via le badge “Open in Colab”.  
2. Monter le Drive :  
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Charger les données depuis Drive / URL.  
4. Exécuter les cellules, documenter, sauvegarder.  
5. Exporter le notebook → “Save a copy to GitHub”.

### Sur **ICY / Local**
- Lancer ICY, importer les images `.tif`.  
- Utiliser les plugins : *Spot Detector*, *Track Manager*, *ROI Statistics*.  
- Exporter les résultats (.xml, .xlsx) vers le dossier `result/`.

---

## 🧾 Rapports et documentation
- Chaque TP contient un **rapport LaTeX** compilé en PDF dans `rapport/` ou `report/`.  
- Tous les rapports utilisent la **classe tau** (`tau-class/tau.cls`) pour uniformiser la mise en page.  
- Figures, tables et légendes sont reliées aux données ICY, NumPy ou Matplotlib selon le TP.

---

## ⚙️ Environnement
**Option Conda :**
```bash
conda env create -f env/environment.yml
conda activate vmi
```

**Option pip :**
```bash
pip install -r env/requirements.txt
```

Librairies clés :  
`numpy`, `matplotlib`, `scikit-image`, `torch`, `torchvision`, `opencv-python`, `tifffile`, `scipy`.

---

## 📘 Références principales
- Olivo-Marin, *Wavelet-based detection of spots and features in biological images*, IEEE, 2002.  
- Ronneberger et al., *U-Net: Convolutional Networks for Biomedical Image Segmentation*, MICCAI, 2015.  
- Gidaris et al., *Unsupervised Representation Learning by Predicting Image Rotations*, 2018.  
- Chen et al., *SimCLR: A Simple Framework for Contrastive Learning*, 2020.  
- Cours Master 2 VMI — Camille Kurtz.

---

## ⚖️ Licence
Projet académique — **Licence MIT**  
© 2025 — *Wassim CHIKHI*
