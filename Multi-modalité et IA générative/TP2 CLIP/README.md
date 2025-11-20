# 🧠 TP2 — CLIP : Apprentissage Multimodal Texte–Image  
Master 2 Vision & Machine Intelligente — Université Paris Cité (2025/2026)

[![Ouvrir dans Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vvazzim/Tp-VMI-Wassim/blob/main/Multi-modalité%20et%20IA%20générative/TP2%20CLIP/notebook/TP_CLIP_Wassim.ipynb)

## 🎯 Objectif
Ce TP explore la capacité du modèle **CLIP** à aligner images et textes :
- Analyse d’images naturelles  
- Évaluation sur images médicales ROCO  
- Fine-tuning (ViT-B/16)  
- Comparaison de 5 architectures CLIP  
- Classification zero-shot sur CIFAR10  

## 📁 Structure du projet

```
TP2-CLIP/
│
├── notebook/
│   └── TP_CLIP_Wassim.ipynb
│
├── figures/
│   ├── natural_similarity.png
│   ├── medical_top5_imagenet.png
│   ├── model_comparison_scores.png
│   ├── roco_similarity_pre_vs_ft.png
│   ├── cifar10_preds.png
│   └── ...
│
├── repport/
│   └── TP2_CLIP_Wassim.pdf
│
└── README.md
```

## 📦 Données utilisées
### 🔹 Natural images  
8 images de `skimage.data` avec légendes.

### 🔹 ROCO (Radiology Objects in Context)  
Radiographies / CT / IRM + légendes. Utilisé pour évaluation & fine-tuning.

### 🔹 CIFAR10 (zero-shot)  
Dataset naturel différent de CIFAR100, utilisé pour validation zero-shot.

## ⚙️ Modèles CLIP évalués
RN50, RN101, RN50x4, ViT-B/32, ViT-B/16 (fine-tuné).

## 🧪 Résultats principaux
- **Natural Images** : Acc@1 = 100%, Acc@5 = 100%
- **ROCO pré-entraîné** : similarité correcte mais limitée  
- **Fine-tuning ROCO** : amélioration nette du contraste diagonal  
- **CIFAR10** : Top-1 = 89.16 %, Top-5 = 99.08 %

## 🔗 Code source  
https://github.com/vvazzim/Tp-VMI-Wassim/tree/main/Multi-modalité%20et%20IA%20générative/TP2%20CLIP

## 👤 Auteur  
Wassim Chikhi — M2 VMI  
Université Paris Cité (2025/2026)
