# TP2 — Couleur : Vision & Computational Pathology

**Master 2 VMI — IFLCE075 Méthodologie et Imageries Thématiques**  
**Responsable :** Nicolas Loménie

---

## 🎯 Objectif

Explorer la perception et le traitement numérique de la couleur dans le contexte de la vision par ordinateur et de la pathologie computationnelle. La coloration histologique (H&E, H-DAB) repose sur des colorants dont la séparation est essentielle pour l'analyse morphologique et biochimique.

---

## 📁 Structure du projet

```
TP2 Color Supp/
├── notebook/
│   └── tp-color-supp.ipynb     # Notebook principal
├── figures/                     # Résultats visuels
│   ├── normandy_paradox.png
│   ├── clown_rgb_lab.png
│   ├── sampleHE_deconv_HE.png
│   ├── ytma10_deconv_HDAB.png
│   └── ...
├── report/
│   └── TP_Color_Wassim_compressed.pdf
└── README.md
```

---

## 📘 Contenu du notebook

### 1. Image de Normandie
- Split des canaux R, G, B
- Permutation des canaux → *Color Display Paradox*
- Dépendance du gamut et du dispositif d'affichage

### 2. Image du Clown
- Split RGB, histogrammes
- Luminance **Y** vs luminance perceptuelle **L***
- Conversion en **CIELab (L*, a*, b*)**

### 3. Image du Mandrill
- RGB + Lab, analyse des histogrammes
- Étude des contrastes perceptuels

### 4. Déconvolution couleur (Ruifrok & Johnston, 2001)
- Conversion RGB → Densité optique (OD)
- Séparation des colorants H&E et H-DAB
- Cas H&E correct/incorrect, ZoomBrownish, YTMA10

---

## 🧠 Concepts clés

| Concept | Explication |
|---------|-------------|
| **RGB insuffisant** | Dépend du matériel, pas perceptuellement uniforme — *Color Display Paradox* |
| **CIELab** | Sépare luminance (L*) et chrominance (a*, b*) — uniformité perceptuelle |
| **Densité optique** | Loi de Beer–Lambert : OD = -log(I/I₀) — contributions linéaires des colorants |
| **Sensibilité déconvolution** | Matrice incorrecte → artefacts, inversions, bruit |

---

## 📦 Données utilisées

`normandy.jpg`, `clown.png`, `mandrill.tif`, `sampleHE.tif`, `ZoomBrownish.tif`, `ytma10_010704_benign1_ccd.tif`

---

## ⚙️ Installation

```bash
pip install numpy scipy scikit-image matplotlib opencv-python pillow
```

---

## ▶️ Exécution

```bash
cd "Méthodologie et imageries thématiques/TP2 Color Supp"
jupyter notebook notebook/tp-color-supp.ipynb
```

Ou ouvrir le notebook dans Jupyter / VSCode / Google Colab.

---

## 📚 Références

- Ruifrok & Johnston, *Quantification of histochemical staining by color deconvolution*, J Histochem Cytochem, 2001
- CIE, *Colorimetry*, Third Edition, 2004

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
