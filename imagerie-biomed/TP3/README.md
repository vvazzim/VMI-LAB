# TP3 — Segmentation & Tracking de cellules HeLa
**UE Bio-Imagerie Médicale — Master 2 Vision et Machine Intelligente (VMI)**

[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-blue?logo=kaggle)](https://www.kaggle.com/code/wassmed/tp3-cellsegmentation-tracking-q2-v-2-2)

## 👤 Auteur
**Wassim Chikhi**  
Université Paris Cité — Année 2025/2026

---

## 🎯 Objectifs du TP

Ce TP met en œuvre deux approches complémentaires d’analyse d’images cellulaires HeLa :

- **Question 1 — ICY (approche interactive)**  
  Segmentation de cellules fluorescentes, détection de *spots* intracellulaires et quantification du nombre de spots par cellule via des ROIs.

- **Question 2 — Python (approche automatique)**  
  Segmentation automatique de cellules HeLa dans une séquence 2D+temps (Cell Tracking Challenge) avec **Cellpose**, puis reconstruction des trajectoires avec **TrackPy**.

L’objectif global est de comparer une approche interactive contrôlée (ICY) à une approche entièrement automatique (deep learning + tracking).

---

## 📁 Organisation du dossier

```
imagerie-biomed/TP3/
├─ data/
│  ├─ HeLa_cells.tif
│  └─ DIC-C2DH-HeLa/
│
├─ icy/
│  ├─ captures/
│  ├─ protocols/
│  └─ exports/
│
├─ notebook/
│  └─ tp3-cellsegmentation-tracking-q2-v-2-2.ipynb
│
├─ figures/
│  ├─ dic_frame0.png
│  ├─ cellpose_segmentation_frame0.png
│  ├─ centroids_frame0.png
│  └─ HeLa_trajectories.png
│
├─ results/
│  └─ HeLa_trajectories.csv
│
├─ report/
│  └─ TP3_CellSegmentation_Tracking_Wassim.pdf
│
└─ README.md
```

---

## 🧪 Question 1 — Analyse sous ICY

**Données**  
- Image multicanal : `HeLa_cells.tif`

**Pipeline ICY**
- Filtrage médian (réduction du bruit)
- Seuillage automatique (Otsu / Best Threshold)
- Morphologie (Fill Holes, Dilation, Erosion)
- Détection de spots par ondelettes (*Spot Detector*)
- Comptage des spots par cellule via ROIs

**Résultats**
- Comptage des spots sur plusieurs cellules
- Calcul moyenne / écart-type
- Discussion sur la variabilité inter-cellulaire et la sensibilité aux seuils

---

## 🤖 Question 2 — Analyse automatique (Python)

### Segmentation (Cellpose)
- Modèle : Cellpose v4  
- Paramètres :
  - `diameter = 30`
  - `flow_threshold = 0.4`
  - `cellprob_threshold = 0.0`

### Tracking (TrackPy)
- Extraction des centroïdes à partir des masques
- Nearest Neighbour linking :
  - `search_range = 25`
  - `memory = 3`
- Visualisation des trajectoires superposées à l’image DIC

---

## 📊 Figures clés
- `dic_frame0.png` — image DIC brute
- `cellpose_segmentation_frame0.png` — segmentation Cellpose
- `centroids_frame0.png` — centroïdes
- `HeLa_trajectories.png` — trajectoires finales

---

## 🔁 Reproductibilité (Kaggle)

Le notebook est exécutable **sur GPU via Kaggle** :

👉 https://www.kaggle.com/code/wassmed/tp3-cellsegmentation-tracking-q2-v-2-2

Il permet de :
- relancer la segmentation Cellpose,
- extraire les centroïdes,
- effectuer le tracking TrackPy,
- régénérer toutes les figures du rapport.

---

## ✅ Conclusion

Ce TP met en évidence la complémentarité entre :
- **ICY**, adapté à l’analyse interactive et au contrôle visuel précis,
- **Cellpose + TrackPy**, solution automatique et scalable pour l’analyse dynamique temporelle.

L’association des deux constitue un workflow robuste pour l’étude morphologique et dynamique des cellules HeLa.
