# Séquences Vidéo (SeqVid)  
## Master 2 Vision et Machines Intelligentes (VMI) — Université Paris Cité

Ce dossier regroupe les travaux du module **Séquences Vidéo**, couvrant la calibration de caméra, le flot optique et le suivi multi-objets.

---

## 🎯 Objectif du module

Explorer le traitement des séquences vidéo et le suivi d'objets :

- **TP1** : Calibration de caméra (mire, paramètres intrinsèques/extrinsèques)
- **TP2** : Flot optique (Lucas-Kanade, Farneback)
- **TP3** : Multi-object tracking (CSRT, YOLOv8 + IoU, Kalman)

---

## 🗂 Structure du module

```
SeqVid/
├── README.md                   # Ce fichier
│
├── TP1/                        # Calibration caméra
│   ├── tp-calibcam.ipynb
│   └── TP_Calibration_Camera.pdf
│
├── TP2/                        # Flot optique
│   ├── tp-2-seqvid-optical-flow.ipynb
│   └── TP2_SeqVid flot optique.pdf
│
└── TP3/                        # Multi-object tracking
    ├── src/                    # Scripts Python
    ├── report/
    │   └── TP3_SeqVid_Wassim.pdf
    ├── requirements.txt
    ├── environment.yml
    └── README.md
```

---

## 📚 TPs réalisés

### 📷 TP1 — Calibration de caméra

**Objectif :** Calibrer une caméra à partir d'images de mire (échiquier), extraire les paramètres intrinsèques et extrinsèques.

📁 Dossier : [`TP1/`](TP1/) | Sujet : `TP1/TP_Calibration_Camera.pdf`

---

### 🌊 TP2 — Flot optique

**Objectif :** Implémenter et comparer des méthodes de flot optique (Lucas-Kanade pyramidal, Farneback) pour l'estimation du mouvement entre images.

📁 Dossier : [`TP2/`](TP2/) | Sujet : `TP2/TP2_SeqVid flot optique.pdf`

---

### 🎯 TP3 — Multi-object tracking

**Objectif :** Comparer le tracking classique (CSRT) et le tracking par détection (YOLOv8 + association IoU), avec bonus Kalman et étude de paramètres.

📁 Dossier : [`TP3/`](TP3/) | Rapport : `TP3/report/TP3_SeqVid_Wassim.pdf`

---

## ⚙️ Environnement

**TP1 & TP2 :** notebooks Jupyter — `opencv-python`, `numpy`, `matplotlib` (exécution possible sur Kaggle ou local)

**TP3 :** environnement dédié — voir `TP3/requirements.txt` et `TP3/environment.yml`

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
