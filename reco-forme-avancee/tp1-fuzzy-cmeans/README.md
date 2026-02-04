# Reco — TP1 — Fuzzy C-Means  
**Auteur :** Wassim Chikhi · **Date :** 06/11/2025  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vvazzim/Tp-VMI-Wassim/blob/main/reco-forme-avancee/tp1-fuzzy-cmeans/notebooks/TP_Fuzzy_C_Means3_0.ipynb)

---

## 🎯 Objectifs
- Implémenter **from scratch** l’algorithme **Fuzzy C-Means (FCM)**.
- Appliquer FCM sur **la même image** en deux modes : **GRAY (C=2)** puis **RGB (C=3)**.
- Visualiser heatmap/appartenance et **segmentation durcie** ; exporter les figures.

---

## 📂 Données
- **Source :** téléchargement automatique depuis GitHub (pas d’upload manuel).
- **Lien :** [`data/`](https://github.com/vvazzim/Tp-VMI-Wassim/tree/main/reco-forme-avancee/tp1-fuzzy-cmeans/data)
- **Fichier utilisé :** `milky-way.jpg` (RGB, 1024×1024).
- **Remarque :** l’image **niveaux de gris n’est pas un fichier** — elle est **générée à l’exécution** depuis `milky-way.jpg`.

---

## ▶️ Lancer (Colab)
1. Cliquez sur le badge **Open In Colab** ci-dessus.  
2. **Run all** – les données sont téléchargées automatiquement depuis GitHub.  
3. Les résultats sont exportés dans `out/`.

---

## 🧪 Plan d’expérience
1. Charger une **seule image source** : `milky-way.jpg`.  
2. Exécuter FCM en :
   - **GRAY** → `C=2` (fond vs région lumineuse),
   - **RGB** → `C=3` (fond / bras / bulbe).
3. Comparer les segmentations et commenter l’influence de `m` (tests : 1.5, 2.0, 3.0).

---

## 📈 Résultats générés
- `out/fcm_gray_result.png.png` — segmentation durcie (mode **GRAY**, C=2)  
- `out/fcm_rgb_result.png.png` — segmentation durcie (mode **RGB**, C=3)


---

## 📝 Rapport
- PDF (si présent) : `rapport/rapport-fcm.pdf`  
- Les figures insérées dans le rapport sont celles de `out/` (voir noms ci-dessus).


Le rapport présente les 4 images finales :
| Ligne | Contenu |
|--------|----------|
| 1 | Image originale (RGB) + version niveaux de gris |
| 2 | Résultat FCM GRAY (C=2) + Résultat FCM RGB (C=3) |

---

## 📎 Références
- J.C. Dunn (1973) — *A Fuzzy Relative of the ISODATA Process and Its Use in Detecting Compact Well-Separated Clusters.*  
- J.C. Bezdek (1981) — *Pattern Recognition with Fuzzy Objective Function Algorithms.*

---

## 🧩 Auteur
Wassim **Chikhi**  
Master 2 Vision et Machine Intelligente — Université Paris Cité  
Année universitaire **2025 / 2026**
