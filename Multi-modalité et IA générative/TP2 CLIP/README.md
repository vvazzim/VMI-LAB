# TP2 — CLIP : Apprentissage Multimodal Texte–Image

**Master 2 VMI — Université Paris Cité (2025/2026)**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vvazzim/Tp-VMI-Wassim/blob/main/Multi-modalité%20et%20IA%20générative/TP2%20CLIP/notebook/TP_CLIP_Wassim.ipynb)

---

## 🎯 Objectif

Explorer la capacité du modèle **CLIP** à aligner images et textes :

- Analyse d'images naturelles avec similarité texte-image
- Évaluation sur images médicales **ROCO** (Radiology Objects in Context)
- Fine-tuning ViT-B/16 sur ROCO
- Comparaison de 5 architectures CLIP (RN50, RN101, RN50x4, ViT-B/32, ViT-B/16)
- Classification zero-shot sur **CIFAR10**

---

## 📁 Structure du projet

```
TP2 CLIP/
├── notebook/
│   └── TP_CLIP_Wassim.ipynb    # Notebook principal
├── figures/                     # Visualisations
│   ├── natural_similarity.png
│   ├── medical_similarity_finetuned.png
│   ├── roco_similarity_pre_vs_ft.png
│   ├── model_comparison_scores.png
│   └── ...
├── repport/
│   └── TP2_CLIP_r.pdf          # Rapport final
└── README.md
```

---

## 📦 Données utilisées

| Source | Description |
|--------|-------------|
| **Natural images** | 8 images de `skimage.data` avec légendes |
| **ROCO** | Radiographies / CT / IRM + légendes — évaluation & fine-tuning |
| **CIFAR10** | Validation zero-shot |

---

## 🧪 Résultats principaux

| Expérience | Résultat |
|------------|----------|
| Natural Images | Acc@1 = 100%, Acc@5 = 100% |
| ROCO pré-entraîné | Similarité correcte mais limitée |
| ROCO fine-tuné | Amélioration nette du contraste diagonal |
| CIFAR10 zero-shot | Top-1 = 89.16 %, Top-5 = 99.08 % |

---

## ⚙️ Modèles CLIP évalués

RN50, RN101, RN50x4, ViT-B/32, ViT-B/16 (fine-tuné sur ROCO)

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
