# 🧬 Imagerie Biomédicale — VMI 2025
**Auteur :** Wassim CHIKHI  
**Formation :** Master 2 Vision et Machines Intelligentes — Université Paris Cité  
**Année :** 2025 / 2026  

---

## 🎯 Objectif
Ce projet regroupe les **Travaux Pratiques d’Imagerie Biomédicale**, couvrant :
1. Les **modalités de microscopie** et le photoblanchiment (TP01)
2. La **détection et le tracking** de particules biologiques (TP02)
3. La **segmentation et la morphométrie** (TP03, à venir)

Le dépôt vise à assurer la **reproductibilité** : scripts, notebooks, rapports et figures sont versionnés et documentés.

---

## 📂 Structure
```
BioImaging_VMI2025/
├── data/          # Images brutes, traitées, résultats
├── notebooks/     # Notebooks Colab / Jupyter
├── scripts/       # Modules Python réutilisables
├── figures/       # Schémas et visualisations
├── reports/       # Rapports PDF / DOCX
├── refs/          # Cours et articles de référence
├── icy_macros/    # Scripts ICY (suivi, segmentation)
├── env/           # Fichiers d’environnement
└── utils/         # Fonctions utilitaires
```

---

## ⚙️ Environnement
**Conda :**
```bash
conda env create -f env/environment.yml
conda activate bioimg
```
**pip :**
```bash
pip install -r env/requirements.txt
```

---

## 🧠 Bonnes pratiques
- 🔒 **Ne jamais modifier** `data/raw/` → travaille uniquement dans `processed/`.
- 🧹 Nettoyer les images avec `scripts/preprocessing.py` avant analyses.
- 🧪 Chaque TP = 1 notebook (`notebooks/TP0X_...ipynb`) + scripts associés (`scripts/`) + rapport dans `reports/`.
- 🧾 Traçabilité : chaque figure correspond à un script + un résultat (ex. `TP02 -> tracking.py -> figure_tracks.png`).

---

## 📘 Références
- Olivo-Marin, *Wavelet-based detection of spots and features in biological images*, IEEE, 2002  
- Genovesio et al., *Tracking of Cells in Videos: A Particle Filtering Approach*, IEEE TPAMI, 2005  
- Cours d’Imagerie Biomédicale — M2 VMI (Camille Kurtz)

---

## 🔗 Liens utiles
- ICY : https://icy.bioimageanalysis.org/  
- scikit-image : https://scikit-image.org/  
- TrackMate (Fiji) : https://imagej.net/plugins/trackmate/
