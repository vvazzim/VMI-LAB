# TP3 — Multi-Object Tracking (Séquences Vidéo)

**Master 2 VMI — Module Séquences Vidéo**  
Université Paris Cité — 2025/2026

---

## 🎯 Objectifs

Explorer et comparer différentes approches de **suivi multi-objets** dans des séquences vidéo :

| Partie | Description |
|--------|-------------|
| **Q1 — Tracking classique** | Trackers CSRT (OpenCV) avec initialisation manuelle des bboxes sur la première frame |
| **Q2 — Tracking par détection** | YOLOv8 + association temporelle par IoU (classe person) |
| **Bonus 1 — Kalman** | Filtrage de Kalman 2D pour lissage et prédiction des trajectoires |
| **Bonus 2 — Paramètres** | Étude de l'influence des seuils (confidence, IoU) sur la stabilité |

---

## 📁 Organisation

```
SeqVid/TP3/
├── README.md
├── environment.yml
├── requirements.txt
├── src/
│   ├── q1_csrt.py           # Q1 — CSRT
│   ├── q2_yolo_iou.py       # Q2 — YOLO + IoU
│   ├── bonus_kalman.py      # Bonus — Kalman
│   ├── bonus_param_sweep.py # Bonus — étude paramètres
│   ├── export_frames.py     # Export de frames
│   ├── select_bboxes.py     # Sélection manuelle bboxes (Q1)
│   └── utils_io.py
├── tracking/                # Vidéos d'entrée (à fournir, non versionnées)
├── tracking_results/        # Sorties (vidéos, CSV, figures)
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

**Dépendances principales :** `opencv-python`, `ultralytics` (YOLOv8), `torch`, `pandas`, `matplotlib`, `tqdm`

---

## ▶️ Exécution

Placer les vidéos dans `tracking/` ou préciser le chemin avec `--video` :

```bash
# Q1 — CSRT (sélection manuelle des bboxes au lancement)
python src/q1_csrt.py --video tracking/VOTRE_VIDEO.avi

# Q2 — YOLO + IoU
python src/q2_yolo_iou.py --video tracking/VOTRE_VIDEO.avi
```

Les sorties sont enregistrées dans `tracking_results/`.

---

## 📊 Résultats

- Vidéos annotées (`.mp4`)
- Trajectoires (CSV)
- Figures (PNG)

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
