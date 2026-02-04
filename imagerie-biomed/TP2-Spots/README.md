# 🧠 TP2 — Détection et Tracking de Spots sous ICY

**Auteur :** Wassim CHIKHI — M2 VMI 2025  
**UE :** Imagerie Biomédicale

---

## 🎯 Objectif
Mettre en œuvre un pipeline sous **ICY** pour : détecter des spots fluorescents, suivre leurs trajectoires (2D+t) et analyser quantitativement leur dynamique (longueur, vitesse, durée), avec archivage reproductible.

---

## ⚙️ Pipeline expérimental

| Étape | Plugin / Action | Objectif | Résultat |
|:--:|:--|:--|:--|
| 1️⃣ | Import `cell2D_timelapse.tif` | Charger la séquence temporelle | Séquence visible avec barre T |
| 2️⃣ | Spot Detector | Identifier les points lumineux | ROI ponctuels par frame |
| 3️⃣ | Réglages | Scales = 1–2, Sensitivity = 100, Threshold = 5–8 | Export ROI + SwimmingPool |
| 4️⃣ | Spot Tracking | Relier les ROIs dans le temps | 138 trajectoires |
| 5️⃣ | Track Manager + ROI Statistics | Mesures (durée, longueur, vitesse) | `Interior.xlsx` |
| 6️⃣ | Export final | Sauvegarder résultats et XML | `trackManager.xml`, `cell2D_timelapse_with_tracks.xml` |

---

## 🧩 Paramètres ICY utilisés
- **Wavelet Spot Detector** → Bright over dark ✅ ; Scales = 1, 2 ; Threshold = 5–8  
- **Spot Tracking** → Model = Diffusive ; Linking distance = 5 px ; Gap closing = 1 frame  
- **Track Manager** → Processors : ROI Statistics + Instant Speed

---

## ⚙️ Automatisation (dossier `ICY_TP02_pipeline/`)
- `TP02_tracking_script.py` : sauvegarde **un seul** XML ICY ré-ouvrable (pixels+ROIs+tracks) depuis la séquence active.
- `TP02_semi_auto_pipeline.py` : mode **semi-automatique** avec pause/validation puis sauvegarde.
- `TP02_tracking_howto.md` : pas-à-pas (Script Editor, Jython).
- `TP02_tracking_blocks.txt` : topologie des blocs (option reconstruire visuellement).
- `TP02_tracking_params.json` : paramètres de référence (chemins, seuils, linking, gap).

---

## 📊 Résultats quantitatifs

| Mesure | Moyenne | Écart-type | Unité |
|:--|:--:|:--:|:--|
| Nombre de trajectoires | 138 | — | — |
| Longueur moyenne | 10.5 | 3.2 | px |
| Durée moyenne | 8.4 | 1.7 | frames |
| Vitesse moyenne | 1.2 | 0.4 | px/frame |

> Données issues de `result/Interior.xlsx`.

---

## 🖼️ Figures
- `captures/Spot Detector.png` — Détection des spots (Wavelet)
- `captures/Spot Tracking.png` — Trajectoires colorées
- `captures/Track Manager.png` — Analyse des pistes
- `captures/num2.png` — Évolution temporelle

---

## 📁 Arborescence
```
TP2-Spots/
├── captures/
├── data/
├── result/
├── ICY_TP02_pipeline/
├── report/
└── README.md
```

---

## 📄 Rapport
- PDF : `report/TP_2_BioImg_Wassim.pdf`

---

## 🔗 Dépôt
https://github.com/vvazzim/Tp-VMI-Wassim/tree/main/imagerie-biomed/TP2-Spots