# 🧬 Imagerie Biomédicale — Vision & Machines Intelligentes (VMI)
**Auteur :** Wassim CHIKHI  
**Année :** 2025  
**Master 2 — Université Paris Cité — Parcours Vision et Machines Intelligentes**

---

## 🎯 Objectif
Cette section du dépôt regroupe les **Travaux Pratiques d’Imagerie Biomédicale**, couvrant l’imagerie photonique, la détection et le tracking de particules, et la segmentation morphologique à venir.

Les TPs ont été réalisés dans le cadre du **Master 2 VMI**, à l’Université Paris Cité, sous l’encadrement de **Camille Kurtz**.

---

## 🧩 Liste des Travaux Pratiques

### 🧪 TP1 — Imagerie Photonique : Modalités et Photoblanchiment
**Objectif :** Étudier les principales **modalités de microscopie photonique** (champ clair, fluorescence, confocale) et mesurer le phénomène de photoblanchiment.  

- Visualisation et mesure d’intensité lumineuse dans le temps  
- Fit exponentiel pour estimer la constante de décroissance τ  
- Schémas optiques et traitement d’images sous Python

📄 **Rapport PDF :** [`tp1-modalities/report/TP_1_BioImg.pdf`](./tp1-modalities/report/TP_1_BioImg.pdf)  
📁 **Dossier complet :** [`tp1-modalities/`](./tp1-modalities/)

---

### 🧠 TP2 — Détection et Tracking de Spots sous ICY
**Objectif :** Détecter et suivre le **mouvement de particules fluorescentes** à l’aide du logiciel **ICY**, puis automatiser partiellement le processus via des scripts Python (Jython).  

**Pipeline ICY :**
1️⃣ Import `cell2D_timelapse.tif`  
2️⃣ Détection des spots (Wavelet Spot Detector)  
3️⃣ Tracking temporel (Kalman / Diffusive Model)  
4️⃣ Analyse (ROI Statistics + Track Manager)  
5️⃣ Export des fichiers `Interior.xlsx` et `trackManager.xml`

**Résultats principaux :**
| Mesure | Moyenne | Écart-type | Unité |
|:--|:--:|:--:|:--|
| Nombre de trajectoires | 138 | — | — |
| Longueur moyenne | 10.5 | 3.2 | px |
| Durée moyenne | 8.4 | 1.7 | frames |
| Vitesse moyenne | 1.2 | 0.4 | px/frame |

📄 **Rapport PDF :** [`tp2-spots/report/TP_2_BioImg_Wassim.pdf`](./tp2-spots/report/TP_2_BioImg_Wassim.pdf)  
📁 **Code source complet :** [TP2-Spots sur GitHub](https://github.com/vvazzim/Tp-VMI-Wassim/tree/main/imagerie-biomed/tp2-spots)

---

### 🧬 TP3 — Segmentation et Morphométrie (à venir)
**Objectif :** Implémenter des approches de **segmentation sémantique** (U-Net, Watershed) et des outils de morphométrie sur images médicales.  
📁 Dossier : `tp3-segmentation/`

---

## 📂 Arborescence de la section BioImaging
```
imagerie-biomed/
├── tp1-modalities/
│   ├── figures/
│   ├── data/
│   ├── report/
│   └── README.md
│
├── tp2-spots/
│   ├── captures/
│   ├── data/
│   ├── ICY_TP02_pipeline/
│   ├── result/
│   ├── report/
│   └── README.md
│
└── tp3-segmentation/
```

---

## ⚙️ Environnement recommandé
### Installation via Conda
```bash
conda env create -f env/environment.yml
conda activate bioimg
```

### ou via pip
```bash
pip install -r env/requirements.txt
```

**Librairies clés :**  
`numpy`, `scikit-image`, `matplotlib`, `opencv-python`, `tifffile`, `scipy`  
+ logiciels externes : **ICY**, **Fiji**, **LaTeX (tau-class)**

---

## 📘 Références
- Olivo-Marin, *Wavelet-based detection of spots and features in biological images*, IEEE, 2002.  
- Genovesio et al., *Tracking of Cells in Videos: A Particle Filtering Approach*, IEEE TPAMI, 2005.  
- Ronneberger et al., *U-Net: Convolutional Networks for Biomedical Image Segmentation*, MICCAI, 2015.  
- Cours d’Imagerie Biomédicale — *Université Paris Cité* (Camille Kurtz).

---

## ⚖️ Licence
Projet académique — **Licence MIT**  
© 2025 — *Wassim CHIKHI*
