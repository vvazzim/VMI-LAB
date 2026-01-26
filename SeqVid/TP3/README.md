# TP3 — Multi-Object Tracking (OpenCV & YOLO)

**UE Séquences Vidéo — Master 2 Vision et Machine Intelligente (VMI)**  
Université Paris Cité — Année 2025/2026

---

## 🎯 Objectifs du TP

Ce TP a pour objectif d’explorer et de comparer plusieurs approches de **suivi multi-objets (Multi-Object Tracking)** dans des séquences vidéo réelles :

- **Q1 — Trackers classiques (OpenCV)**  
  Suivi multi-objets basé sur des trackers CSRT initialisés manuellement.

- **Q2 — Tracking par détection (YOLOv8 + IoU)**  
  Détection d’objets par YOLOv8 puis association inter-frames par recouvrement IoU.

- **Bonus 1 — Filtrage de Kalman**  
  Lissage et prédiction des trajectoires 2D pour améliorer la stabilité du suivi.

- **Bonus 2 — Étude de paramètres**  
  Analyse de l’impact des seuils (confidence, IoU), du FPS et de la stabilité des trajectoires.

L’objectif global est de comparer les limites des trackers classiques face aux méthodes modernes basées sur la détection.

---

## 📁 Organisation du projet

```text
TP3-SequenceVid/
├─ tracking/                 # Vidéos d’entrée
├─ tracking_results/         # Résultats (vidéos, CSV, figures)
├─ src/
│  ├─ q1_csrt.py             # Tracking CSRT (OpenCV)
│  ├─ q2_yolo_iou.py         # YOLOv8 + association IoU
│  ├─ bonus_kalman.py        # Filtre de Kalman 2D
│  └─ bonus_param_sweep.py  # Étude de paramètres
├─ report/
│  ├─ main.tex
│  └─ figures/
├─ requirements.txt
└─ README.md
```

---

## ⚙️ Installation

Créer un environnement Python (3.10 recommandé) :

```bash
conda create -n seqvid python=3.10
conda activate seqvid
pip install -r requirements.txt
```

---

## ▶️ Exécution

### Q1 — Tracking CSRT (OpenCV)
```bash
python src/q1_csrt.py --video tracking/Tracking2min.avi
```

### Q2 — YOLOv8 + IoU
```bash
python src/q2_yolo_iou.py --video tracking/Tracking2min.avi
```

### Bonus — Filtre de Kalman
```bash
set KMP_DUPLICATE_LIB_OK=TRUE
python src/bonus_kalman.py --video tracking/Walk1.mpeg --class_name person
```

### Bonus — Étude de paramètres
```bash
python src/bonus_param_sweep.py --video tracking/Walk1.mpeg --max_frames 60
```

---

## 📊 Résultats

Les résultats sont générés automatiquement dans le dossier `tracking_results/` :

- Vidéos annotées (`.mp4`)
- Trajectoires filtrées (`.png`)
- Tableaux de mesures (`.csv`)

Ces sorties permettent une évaluation qualitative et quantitative des performances de suivi.

---

## ✍️ Auteur

**Wassim Chikhi**  
Master 2 Vision et Machine Intelligente — Université Paris Cité  
Année universitaire 2025/2026

---

## ✅ Remarques

- Le code est conçu pour être **reproductible** et **facilement paramétrable**
- Aucun fichier vidéo lourd n’est requis pour l’évaluation GitHub
- Compatible avec une exécution locale CPU/GPU
