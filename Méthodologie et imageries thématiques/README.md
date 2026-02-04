# Méthodologie et imageries thématiques  
## Master 2 Vision et Machines Intelligentes (VMI) — Université Paris Cité

Ce dossier regroupe les travaux du module **Méthodologie et Imageries Thématiques** (IFLCE075), couvrant le traitement de la couleur en vision computationnelle et pathologie, ainsi que l'apprentissage profond efficient (Knowledge Distillation).

**Responsable du module :** Nicolas Loménie

---

## 🎯 Objectif du module

Explorer des méthodes avancées en vision par ordinateur et imagerie médicale :

- **Perception et traitement de la couleur** : espaces couleur, déconvolution pour la pathologie computationnelle
- **Deep Learning efficient** : Knowledge Distillation pour compresser et transférer les connaissances d'un grand modèle vers un modèle léger

---

## 🗂 Structure du module

```
Méthodologie et imageries thématiques/
│
├── README.md                   # Ce fichier
│
├── TP2 Color Supp/             # TP — Couleur et déconvolution
│   ├── notebook/
│   │   └── tp-color-supp.ipynb
│   ├── figures/                # Résultats visuels
│   ├── report/
│   │   └── TP_Color_Wassim_compressed.pdf
│   └── README.md
│
└── TP3 Efficient DL/           # TP — Knowledge Distillation
    ├── notebook/
    │   └── EfficientDL_KD_Lab.ipynb
    ├── figures/
    ├── report/
    │   ├── KD_LAB.pdf
    │   └── KD_LAB.tex
    └── README.md
```

---

## 📚 TPs réalisés

### 🎨 TP2 — Couleur : espaces et déconvolution

**Objectif :** Maîtriser les espaces couleur (RGB, CIELab), la luminance, la densité optique et la **déconvolution de Ruifrok & Johnston** pour les colorations histologiques (H&E, H-DAB).

**Contenu :** Color Display Paradox, comparaison Y vs L*, déconvolution H&E/H-DAB, application sur images réelles (YTMA10).

📁 Dossier : [`TP2 Color Supp/`](TP2%20Color%20Supp/) | Rapport : `TP2 Color Supp/report/TP_Color_Wassim_compressed.pdf`

---

### ⚡ TP3 — Efficient DL : Knowledge Distillation

**Objectif :** Compresser un Teacher (ResNet50) vers un Student (ResNet18) sur CIFAR-10 via Knowledge Distillation (logits et feature maps).

**Résultats :**

| Modèle | Test accuracy |
|--------|---------------|
| Teacher (ResNet50) | 0.9297 |
| Student baseline (ResNet18, pretrained) | 0.9213 |
| Student KD logits (ResNet18, pretrained) | **0.9312** |

📁 Dossier : [`TP3 Efficient DL/`](TP3%20Efficient%20DL/) | Rapport : `TP3 Efficient DL/report/KD_LAB.pdf`

---

## ⚙️ Environnement

**TP2 Color :** `numpy`, `scipy`, `scikit-image`, `matplotlib`, `opencv-python`, `pillow`

**TP3 Efficient DL :** `torch`, `torchvision`, `matplotlib`, `tqdm` — exécution recommandée sur **Google Colab** (GPU)

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
