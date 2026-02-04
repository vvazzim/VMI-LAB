# Multi-modalité et IA générative  
## Master 2 Vision et Machines Intelligentes (VMI) — Université Paris Cité

Ce dossier regroupe les travaux du module **Multi-modalité et IA générative** (IFLCE055), couvrant l'adaptation de LLMs, l'apprentissage multimodal texte-image (CLIP) et la génération d'images (VAE, GAN).

---

## 🎯 Objectif du module

Explorer les architectures et méthodes à la frontière de la **vision par ordinateur**, du **traitement du langage** et de la **génération d'images** :

- Adaptation de modèles de langage pré-entraînés (LLM) à des tâches aval
- Apprentissage multimodal pour l'alignement texte-image (CLIP)
- Modèles génératifs : VAE et GAN (DCGAN)

---

## 🗂 Structure du module

```
Multi-modalité et IA générative/
│
├── ReadMe.md                   # Ce fichier
│
├── LLM_LAB/                    # TP — Large Language Models
│   ├── notebook/
│   │   └── LLM_Lab.ipynb       # Classification de sentiments (RoBERTa)
│   ├── report/
│   │   └── TP_LLM.pdf
│   └── README.md
│
├── TP2 CLIP/                   # TP — CLIP : multimodal texte-image
│   ├── notebook/
│   │   └── TP_CLIP_Wassim.ipynb
│   ├── figures/                # Similarités, comparaisons modèles
│   ├── repport/
│   │   └── TP2_CLIP_r.pdf
│   └── README.md
│
└── TP 3 GaN-VAE/               # TP — Génération (VAE + GAN)
    ├── ganlab-completed-by-wassim.ipynb
    ├── TP_GaN_VAE_WASSIM (1).pdf
    └── README.md
```

---

## 📚 TPs réalisés

### 🤖 LLM Lab — Classification de sentiments

**Objectif :** Adapter un LLM (RoBERTa) à une tâche de classification binaire (NEGATIVE/POSITIVE) sur des critiques de films.

**Stratégies comparées :** Inference sans entraînement, Linear Probing, Fine-tuning (complet et partiel).

| Approche | Accuracy | F1-score |
|----------|----------|----------|
| Inference sans entraînement | 0.751 | 0.742 |
| Linear probing | 0.836 | 0.835 |
| Fine-tuning complet | **0.877** | **0.874** |
| Fine-tuning partiel | 0.875 | 0.872 |

📁 Dossier : [`LLM_LAB/`](LLM_LAB/) | Rapport : `LLM_LAB/report/TP_LLM.pdf`

---

### 🖼 TP2 — CLIP : multimodal texte-image

**Objectif :** Explorer CLIP pour l'alignement images-textes, l'évaluation sur données médicales (ROCO) et la classification zero-shot.

**Contenu :** Images naturelles, fine-tuning ViT-B/16 sur ROCO, comparaison de 5 architectures, zero-shot CIFAR10.

| Expérience | Résultat |
|------------|----------|
| Natural Images | Acc@1 = 100%, Acc@5 = 100% |
| CIFAR10 zero-shot | Top-1 = 89.16 %, Top-5 = 99.08 % |

📁 Dossier : [`TP2 CLIP/`](TP2%20CLIP/) | Rapport : `TP2 CLIP/repport/TP2_CLIP_r.pdf`

---

### 🎨 TP3 — GAN & VAE : génération de sprites Pokémon

**Objectif :** Implémenter un VAE convolutionnel et un GAN (DCGAN) pour générer des sprites Pokémon.

**Contenu :** VAE (reconstruction + échantillonnage), DCGAN, étude des hyperparamètres, comparaison qualitative.

📁 Dossier : [`TP 3 GaN-VAE/`](TP%203%20GaN-VAE/) | Rapport : `TP 3 GaN-VAE/TP_GaN_VAE_WASSIM (1).pdf`

---

## ⚙️ Environnement

**Librairies principales :**

- `torch`, `torchvision`
- `transformers`, `datasets` (LLM, CLIP)
- `open_clip_torch` ou `clip` (TP2)
- `matplotlib`, `scikit-learn`

Les notebooks sont exécutables sur **Google Colab** (LLM, CLIP) ou en local avec GPU (GAN-VAE recommandé).

---

## 👤 Auteur

**Wassim Chikhi**  
Master 2 VMI — Université Paris Cité  
Année universitaire 2025–2026
