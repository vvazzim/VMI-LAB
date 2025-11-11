# 🧠 TP2 — Détection et Tracking de Spots sous ICY
**Auteur :** Wassim CHIKHI — M2 VMI 2025  
**UE :** Imagerie Biomédicale  

---

## 🎯 Objectif
Mettre en œuvre un pipeline complet sous **ICY** pour :
- détecter des particules lumineuses dans des images microscopiques,  
- suivre leurs trajectoires au fil du temps,  
- et analyser quantitativement leur comportement (longueur, vitesse, durée, intensité).

---

## ⚙️ Pipeline expérimental

| Étape | Plugin / Action | Objectif | Résultat |
|:--:|:--|:--|:--|
| 1️⃣ | Import `cell2D_timelapse.tif` | Charger la séquence temporelle | Séquence visible avec barre T |
| 2️⃣ | Spot Detector | Identifier les points lumineux | Cercles verts visibles sur chaque frame |
| 3️⃣ | Réglages | Scales = 1–2, Sensitivity = 100, Threshold = 5–8 | Détection multi-échelle, export ROI + SwimmingPool |
| 4️⃣ | Spot Tracking | Relier les ROIs dans le temps | 138 trajectoires créées |
| 5️⃣ | Track Manager + ROI Statistics | Calcul de longueurs, durées, vitesses | Fichier `Interior.xlsx` généré |
| 6️⃣ | Export final | Sauvegarder résultats et XML | `trackManager.xml`, `cell2D_timelapse_with_tracks.xml` |

---

## 🧩 Paramètres ICY utilisés
- **Wavelet Spot Detector** → Bright over dark ✅ ; Scales = 1, 2 ; Threshold = 5–8  
- **Spot Tracking** → Model = Diffusive ; Linking distance = 5 px ; Gap closing = 1 frame  
- **Track Manager** → Processors : ROI Statistics + Instant Speed  

---

## ⚙️ Automatisation (ICY_TP02_pipeline)
L’automatisation du protocole a été réalisée **uniquement en Python (Jython)** via le **Script Editor** d’ICY :

| Script | Fonction | Détails |
|:--|:--|:--|
| `TP02_tracking_script.py` | Sauvegarde **un seul** fichier XML ré-ouvrable (`cell2D_timelapse_with_tracks.xml`). | Utilise la séquence active avec trajectoires. |
| `TP02_semi_auto_pipeline.py` | Mode **semi-automatique** (pause → OK → export). | Le script attend la validation avant sauvegarde. |
| `TP02_tracking_howto.md` | Guide pas-à-pas (Script Editor). | Utilisation et dépannage. |
| `TP02_tracking_blocks.txt` | Description du pipeline visuel (optionnelle). | Pour reconstruire les blocs manuellement. |

🗂️ Ces fichiers se trouvent dans le dossier [`ICY_TP02_pipeline/`](./ICY_TP02_pipeline/).

---

## 📊 Résultats quantitatifs

| Mesure | Moyenne | Écart-type | Unité |
|:--|:--:|:--:|:--|
| Nombre de trajectoires | 138 | — | — |
| Longueur moyenne | 10.5 | 3.2 | px |
| Durée moyenne | 8.4 | 1.7 | frames |
| Vitesse moyenne | 1.2 | 0.4 | px/frame |

> Données issues du fichier `Interior.xlsx` exporté depuis ICY.

---

## 🧠 Interprétation scientifique
- Le mouvement observé est **principalement diffusif** (type brownien).  
- Les vitesses faibles indiquent une **activité intracellulaire confinée**.  
- L’association **Wavelet Spot Detector + Kalman Tracking** offre une **robustesse élevée au bruit**.  
- Les écarts-types reflètent une variabilité biologique normale entre particules.

---

## 🖼️ Figures et captures

| Figure | Fichier | Description |
|:--:|:--|:--|
| 1️⃣ | `Spot Detector.png` | Détection des spots lumineux |
| 2️⃣ | `Spot Tracking.png` | Trajectoires colorées dans le temps |
| 3️⃣ | `Track Manager.png` | Interface ICY de gestion et mesures |
| 4️⃣ | `num2.png` | Graphique des vitesses ou intensités |

> Les figures se trouvent dans le dossier [`captures/`](./captures/).

---

## 📁 Arborescence du TP2
```
TP2-Spots/
├── captures/          # Figures pour le rapport
├── data/              # Données brutes (.tif, .jpg)
├── result/            # Exports ICY : .xlsx, .xml
├── ICY_TP02_pipeline/ # Scripts Python pour automatisation
├── report/            # Rapport PDF + source LaTeX
│   ├── TP_2_BioImg_Wassim.pdf
│   └── latex/TP2_Spots_Tracking.tex
└── README.md
```

---

## 📄 Rapport
📘 Rapport PDF : [`report/TP_2_BioImg_Wassim.pdf`](./report/TP_2_BioImg_Wassim.pdf)  
📜 Source LaTeX : [`report/latex/TP2_Spots_Tracking.tex`](./report/latex/TP2_Spots_Tracking.tex)

---

## 📚 Références
- Olivo-Marin, *Wavelet-based detection of spots and features in biological images*, IEEE, 2002.  
- Genovesio et al., *Tracking of Cells in Videos: A Particle Filtering Approach*, IEEE TPAMI, 2005.  
- ICY Documentation — Spot Detector, Track Manager, Scripting (Jython).

---

## 🔗 Dépôt GitHub
Code et scripts :  
👉 [https://github.com/vvazzim/Tp-VMI-Wassim/tree/main/imagerie-biomed/TP2-Spots](https://github.com/vvazzim/Tp-VMI-Wassim/tree/main/imagerie-biomed/TP2-Spots)
