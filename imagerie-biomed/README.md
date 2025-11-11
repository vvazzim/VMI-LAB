# 🧬 Imagerie Biomédicale — VMI 2025
**Auteur :** Wassim CHIKHI  
**Formation :** Master 2 Vision et Machines Intelligentes — Université Paris Cité  
**Année :** 2025 / 2026  

---

## 🎯 Objectif
Ce projet regroupe les **Travaux Pratiques d’Imagerie Biomédicale**, réalisés dans le cadre du parcours **VMI** :

1. 🧪 **TP1 — Imagerie Photonique : Modalités et Principe de la Fluorescence**  
2. 🧠 **TP2 — Détection et Tracking de Spots sous ICY**  
3. 🧬 **TP3 — Segmentation et Morphométrie (à venir)**  

Chaque TP comprend :
- un **notebook ou workflow ICY**,  
- des **figures et scripts associés**,  
- et un **rapport final** (PDF LaTeX format tau-class).

---

## 📂 Structure générale
```
imagerie-biomed/
├── tp1-modalities/
│   ├── figures/           # Schémas optiques, intensités
│   ├── images/            # Données d’analyse
│   ├── report/            # Rapport LaTeX + PDF
│   └── README.md
│
├── tp2-spots/
│   ├── captures/          # Figures ICY (détection, tracking, stats)
│   ├── data/              # Données TIFF et images sources
│   ├── result/            # Exports ICY (xlsx, xml)
│   ├── report/            # Rapport PDF + source LaTeX
│   └── README.md
│
└── tp3-segmentation/      # (à venir)
```

---

## 🧩 TPs réalisés

### 🧪 TP1 — Imagerie Photonique : Modalités et Fluorescence
**Objectif :** Illustrer les principales **modalités de microscopie photonique** (champ clair, contraste de phase, fluorescence, confocale).  
- Construction de **schémas optiques TikZ**.  
- Étude du **photoblanchiment** sur une séquence temporelle.  
- Calcul de l’intensité moyenne :  
  \[
  I_{moy}(t) = \frac{1}{N}\sum_{i=1}^{N} I_i(t)
  \]
📄 Rapport : [`tp1-modalities/report/TP_1_BioImg.pdf`](./tp1-modalities/report/TP_1_BioImg.pdf)

---

### 🧠 TP2 — Détection et Tracking de Spots sous ICY
**Objectif :** Mettre en œuvre un pipeline complet de **détection et suivi de particules** sous ICY.  
- Détection multi-échelle via **Wavelet Spot Detector**.  
- Suivi temporel par **Spot Tracking + Kalman**.  
- Analyse des vitesses et longueurs via **Track Manager**.  
**Résultats principaux :**
| Mesure | Moyenne | Écart-type | Unité |
|:--|:--:|:--:|:--|
| Nombre de trajectoires | 138 | — | — |
| Longueur moyenne | 10.5 | 3.2 | px |
| Durée moyenne | 8.4 | 1.7 | frames |
| Vitesse moyenne | 1.2 | 0.4 | px/frame |

📄 Rapport : [`tp2-spots/report/TP_2_BioImg_Wassim.pdf`](./tp2-spots/report/TP_2_BioImg_Wassim.pdf)

---

## ⚙️ Environnement de travail
**Installation via Conda :**
```bash
conda env create -f env/environment.yml
conda activate bioimg
```

**ou via pip :**
```bash
pip install -r env/requirements.txt
```

Librairies clés :
- `scikit-image`, `tifffile`, `numpy`, `matplotlib`, `opencv-python`
- ICY / Fiji pour le tracking
- LaTeX avec `tau-class` pour la mise en page des rapports

---

## 🧠 Bonnes pratiques
- 🔒 **Ne jamais modifier** `data/raw/` → travailler uniquement sur `processed/`.  
- 🧪 Chaque TP contient son propre environnement et son rapport.  
- 📈 Les figures et scripts sont systématiquement reliés dans le README du TP.  
- 🧾 Les rapports sont compilés sous LaTeX pour assurer une mise en page homogène.

---

## 📘 Références
- Olivo-Marin, *Wavelet-based detection of spots and features in biological images*, IEEE, 2002.  
- Genovesio et al., *Tracking of Cells in Videos: A Particle Filtering Approach*, IEEE TPAMI, 2005.  
- Ronneberger et al., *U-Net: Convolutional Networks for Biomedical Image Segmentation*, MICCAI, 2015.  
- Cours d’Imagerie Biomédicale — M2 VMI (Camille Kurtz).

---

## 🔗 Liens utiles
- [ICY Software](https://icy.bioimageanalysis.org/)  
- [scikit-image](https://scikit-image.org/)  
- [TrackMate (Fiji)](https://imagej.net/plugins/trackmate/)
