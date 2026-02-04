# Deep Learning  
## Master 2 Vision et Machines Intelligentes (VMI) — Université Paris Cité

Ce dossier regroupe les travaux du module **Deep Learning**, de la classification supervisée au self-supervised learning.

---

## 🎯 Objectif du module

Explorer les architectures et méthodes du deep learning :

- **TP1** : MLP sur MNIST — introduction au Deep Learning supervisé
- **TP2** : CNN & Transfer Learning (ResNet18) — fine-tuning
- **TP3** : Self-Supervised Learning — tâches prétextes et linear probe

---

## 🗂 Structure du module

```
deep-learning/
├── README.md                   # Ce fichier
│
├── tp1-mlp-mnist/
│   ├── notebooks/TP1_MLP.ipynb
│   ├── data/
│   └── rapport/rapport.md
│
├── tp2-cnn-transfer-learning/
│   ├── notebooks/TP2_CNN_Transfer.ipynb
│   ├── data/
│   └── rapport/rapport.md
│
└── tp3-self-supervised-learning/
    ├── notebooks/Self_Supervised_Learning_Demos_final.ipynb
    ├── rapport/rapport_SSL.pdf
    └── README.md
```

---

## 📚 TPs réalisés

### TP1 — MLP sur MNIST
Classification supervisée avec un réseau de neurones multicouches.  
📁 `tp1-mlp-mnist/`

### TP2 — CNN & Transfer Learning
Fine-tuning de ResNet18 sur des datasets standards.  
📁 `tp2-cnn-transfer-learning/`

### TP3 — Self-Supervised Learning
Comparaison de tâches prétextes (Rotation, Relative Patch, SimCLR, Inpainting) sur CIFAR-10 / STL-10.  
📁 `tp3-self-supervised-learning/` | Rapport : `rapport/rapport_SSL.pdf`

---

## ⚙️ Environnement

`torch`, `torchvision`, `numpy`, `matplotlib` — exécution recommandée sur **Google Colab** (GPU) pour TP2 et TP3.

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
