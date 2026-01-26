# TP3 — Multi-Object Tracking (Séquences Vidéo)

**UE Séquence Vidéo — Master 2 Vision et Machine Intelligente (VMI)**  
Université Paris Cité — Année 2025/2026

## 👤 Auteur
**Wassim Chikhi**

---

## 🎯 Objectifs du TP

Ce TP a pour objectif d’explorer et comparer différentes approches de **suivi multi-objets**
dans des séquences vidéo réelles :

- **Q1 — Tracking classique (OpenCV)**  
  Suivi multi-objets par trackers CSRT avec initialisation manuelle.

- **Q2 — Tracking par détection (YOLOv8 + IoU)**  
  Détection image par image avec YOLOv8 et association temporelle par recouvrement IoU.

- **Bonus 1 — Filtrage de Kalman**  
  Lissage et prédiction de trajectoires 2D.

- **Bonus 2 — Étude de paramètres**  
  Influence des seuils (confidence, IoU), FPS et stabilité des trajectoires.

---

## 📁 Organisation du projet

```
SeqVid/TP3/
├── README.md
├── .gitignore
├── environment.yml
├── requirements.txt
├── src/
│   ├── q1_csrt.py
│   ├── q2_yolo_iou.py
│   ├── bonus_kalman.py
│   ├── bonus_param_sweep.py
│   ├── export_frames.py
│   ├── select_bboxes.py
│   └── utils_io.py
├── tracking/
│   └── README_DATA.md
├── tracking_results/
│   ├── *.mp4
│   ├── *.csv
│   └── *.png
└── report/
    └── TP3_SeqVid_Wassim.pdf
```

---

## ⚙️ Installation

```bash
conda create -n seqvid python=3.10
conda activate seqvid
pip install -r requirements.txt
```

---

## ▶️ Exécution

```bash
python src/q1_csrt.py --video tracking/Tracking2min.avi
python src/q2_yolo_iou.py --video tracking/Tracking2min.avi
```

---

## 📊 Résultats

Les résultats sont enregistrés dans `tracking_results/` :
- vidéos annotées,
- trajectoires,
- fichiers CSV,
- figures PNG.

---

## 📄 Rapport

Rapport final :
```
SeqVid/TP3/report/TP3_SeqVid_Wassim.pdf
```
