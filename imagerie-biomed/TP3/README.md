# 🧬 TP3 — Segmentation & Tracking de cellules HeLa  
**UE Imagerie Biomédicale — Master 2 Vision & Machines Intelligentes (VMI)**

---

## 👤 Auteur  
**Wassim Chikhi**  
Université Paris Cité — Année universitaire 2025–2026

---

## 🎯 Objectifs pédagogiques

Ce TP vise à mettre en œuvre et comparer **deux approches complémentaires** d’analyse d’images cellulaires :

- **Approche interactive (ICY)** : segmentation, détection de spots fluorescents et analyse quantitative par cellule.  
- **Approche automatique (Python / Deep Learning)** : segmentation par réseau de neurones (Cellpose) et reconstruction de trajectoires cellulaires (TrackPy).

L’objectif global est d’évaluer les avantages et limites d’une analyse **manuelle supervisée** face à une analyse **automatique et scalable**.

---

## 📁 Organisation du dossier

```text
TP3-Imagerie-Biomed/
├─ data/
│  ├─ HeLa_cells.tif
│  └─ DIC-C2DH-HeLa/
│
├─ icy/
│  ├─ captures/
│  ├─ protocols/
│  └─ exports/
│
├─ python/
│  ├─ tp3-cellseg-tracking.ipynb
│  └─ figures/
│
├─ report/
│  ├─ TP3_CellSegmentation_Tracking.pdf
│  └─ figures/
│
└─ README.md
```

---

## 🧪 Question 1 — Analyse sous ICY

- Filtrage médian  
- Seuillage automatique (Otsu / Best Threshold)  
- Morphologie (Fill Holes, Dilation, Erosion)  
- Détection de spots par ondelettes  
- Comptage des spots par cellule via ROIs  

Les paramètres sont documentés par captures d’écran pour assurer la reproductibilité.

---

## 🤖 Question 2 — Analyse automatique (Python)

### Segmentation — Cellpose
- Modèle : Cellpose v4  
- `diameter = 30`  
- `flow_threshold = 0.4`  
- `cellprob_threshold = 0.0`

### Tracking — TrackPy
- Extraction des centroïdes  
- `search_range = 25`  
- `memory = 3`

---

## 📊 Figures produites

- Image DIC brute  
- Segmentation Cellpose  
- Centroïdes  
- Trajectoires cellulaires

---

## 🔁 Reproductibilité

Notebook exécutable (GPU) :  
https://www.kaggle.com/code/wassmed/tp3-cellsegmentation-tracking-q2

---

## ✅ Conclusion

Ce TP met en évidence la complémentarité entre **ICY** (contrôle visuel précis)
et **Cellpose + TrackPy** (pipeline automatique robuste), constituant un workflow
efficace pour l’étude dynamique des cellules HeLa.
