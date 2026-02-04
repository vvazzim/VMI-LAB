# TP3 — Efficient DL : Knowledge Distillation

**Master 2 VMI — IFLCE075 Méthodologie et Imageries Thématiques**

Ce TP porte sur la **Knowledge Distillation (KD)** : transférer les connaissances d'un Teacher (ResNet50) vers un Student (ResNet18) sur **CIFAR-10**.

---

## 🎯 Objectif

Compresser un grand modèle tout en conservant (ou dépassant) ses performances via l'apprentissage par distillation :

- **Teacher** : ResNet50 pré-entraîné ImageNet, fine-tuné sur CIFAR-10
- **Student** : ResNet18 (baseline ou avec KD)
- **KD logits** : distillation des sorties (scores)
- **KD features** : distillation des cartes de caractéristiques intermédiaires

---

## 📁 Structure du projet

```
TP3 Efficient DL/
├── notebook/
│   └── EfficientDL_KD_Lab.ipynb   # Notebook principal
├── figures/
│   ├── comparaison_finale.png     # Comparaison validation
│   └── comparison_test_accuracy.png
├── report/
│   ├── KD_LAB.pdf                 # Rapport final
│   └── KD_LAB.tex
└── README.md
```

---

## 📊 Résultats (test accuracy)

| Modèle | Test accuracy |
|--------|---------------|
| Teacher (ResNet50) | 0.9297 |
| Student baseline (ResNet18, pretrained) | 0.9213 |
| Student KD logits (ResNet18, pretrained) | **0.9312** |

La figure globale inclut aussi KD features et la stratégie student *from scratch*.

---

## ⚙️ Prérequis

- **Google Colab** recommandé (GPU)
- Python ≥ 3.10, PyTorch, torchvision, matplotlib, tqdm

```bash
pip install -U torch torchvision tqdm matplotlib
```

---

## ▶️ Exécution (Colab)

1. Monter Google Drive et définir `CKPT_DIR` :

```python
from google.colab import drive
drive.mount('/content/drive')
CKPT_DIR = "/content/drive/MyDrive/KD_checkpoints"
```

2. Exécuter le notebook — mode **train OR load** : si un checkpoint existe, il est chargé ; sinon, entraînement puis sauvegarde.

### Checkpoints attendus

`teacher_resnet50_best.pt`, `student_pretrained_baseline_best.pt`, `student_pretrained_kd_logits_best.pt`, `student_pretrained_kd_features_best.pt`, `student_scratch_baseline_best.pt`, `student_scratch_kd_scores_best.pt`

---

## 📐 Configuration

- Split : 45 000 train / 5 000 val / 10 000 test
- Seed : `42` (reproductibilité)
- Hyperparamètres détaillés dans le rapport

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
