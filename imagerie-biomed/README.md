# Imagerie Biomédicale  
## Master 2 Vision et Machines Intelligentes (VMI) — Université Paris Cité

Ce dossier regroupe les Travaux Pratiques d'**Imagerie Biomédicale**, couvrant l'imagerie photonique, la détection et le tracking de particules, et la segmentation de cellules.

**Encadrement :** Camille Kurtz

---

## 🗂 Structure

```
imagerie-biomed/
├── README.md              # Ce fichier
│
├── Tp1-Modalities/        # Imagerie photonique, photoblanchiment
│   ├── figures/
│   ├── report/
│   │   └── TP_1_BioImg_Wassim.pdf
│   └── README_TP1_BioImg.md
│
├── TP2-Spots/             # Détection et tracking de spots (ICY)
│   ├── captures/
│   ├── data/
│   ├── ICY_TP02_pipeline/
│   ├── result/
│   ├── report/
│   │   └── TP_2_BioImg_Wassim.pdf
│   └── README.md
│
└── TP3/                   # Segmentation et tracking HeLa (Cellpose + TrackPy)
    ├── notebook/
    ├── figures/
    ├── results/
    ├── report/
    │   └── TP3_CellSegmentation_Tracking_Wassim.pdf
    └── README.md
```

---

## 📚 TPs réalisés

### TP1 — Imagerie Photonique : Modalités et Photoblanchiment
Étude des modalités de microscopie (champ clair, contraste de phase, fluorescence, confocale) et mesure du photoblanchiment.  
📁 `Tp1-Modalities/` | Rapport : `report/TP_1_BioImg_Wassim.pdf`

### TP2 — Détection et Tracking de Spots sous ICY
Pipeline ICY (Wavelet Spot Detector, Kalman) + scripts Jython pour automatisation.  
📁 `TP2-Spots/` | Rapport : `report/TP_2_BioImg_Wassim.pdf`

### TP3 — Segmentation et Tracking de cellules HeLa
Segmentation avec **Cellpose**, tracking avec **TrackPy** ; comparaison approche ICY vs Python.  
📁 `TP3/` | Rapport : `report/TP3_CellSegmentation_Tracking_Wassim.pdf`

---

## ⚙️ Environnement

**Librairies :** `numpy`, `scikit-image`, `matplotlib`, `tifffile`, `scipy`, `cellpose`, `trackpy`  
**Logiciels externes :** ICY, Fiji (optionnel)

---

## 📘 Références

- Olivo-Marin, *Wavelet-based detection of spots and features in biological images*, IEEE, 2002.
- Ronneberger et al., *U-Net: Convolutional Networks for Biomedical Image Segmentation*, MICCAI, 2015.

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
