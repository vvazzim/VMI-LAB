# Classification de lames histologiques (WSI)
## Par chemins spatiaux de patchs (SPPR) et Transformers

**Auteur** : Wassim Chikhi  
**Master** : M2 Vision et Machines Intelligentes (VMI)  
**Université** : Université Paris Cité  
**Année académique** : 2025–2026

---

## 📌 Objectif du projet

Ce projet vise la **classification de Whole Slide Images (WSI)** en histopathologie
(normal vs tumoral) dans un cadre de **supervision faible**, où seules des étiquettes
au niveau global de la lame (WSI-level) sont disponibles.

L’approche proposée repose sur :
- une représentation **patch-level** via des modèles fondation (ViT, DINOv2),
- une modélisation **spatiale explicite** du tissu à l’aide de **chemins de patchs (SPPR)**,
- une **agrégation MIL** pour produire une décision finale au niveau WSI.

L’objectif principal est **méthodologique** : proposer un pipeline cohérent et
scientifiquement valide en supervision faible, plutôt que d’optimiser une performance
absolue sur un petit jeu de test.

---

## 🗂 Structure du dépôt

```
Modélisation_de_systèmes_intelligents/
│
├── Diapo/
│   └── Classification_de_lames_histologiques.pdf
│
├── notebooks/
│   ├── 00-preproc-camelyon-patch-extraction.ipynb
│   ├── 01-wsi-level-stratified-split.ipynb
│   ├── 02-patch-embedding-extraction-vit.ipynb
│   ├── 03-str-randomwalk-sequence-generation.ipynb
│   ├── 04-str-dinov2-training-v4-1.ipynb
│   └── 05-dinov2-embeddings-extraction.ipynb
│
├── report/
│   └── report_sppr_wsi.pdf
│
└── README.md
```

---

## 🧪 Dataset

Les expériences sont menées sur un **sous-ensemble de CAMELYON16** :
- **54 WSI** au total
- Annotation **WSI-level uniquement** (normal / tumoral)

| Split | Total | Normal | Tumoral |
|------:|------:|-------:|--------:|
| Train | 39 | 17 | 22 |
| Val   | 8  | 3  | 5  |
| Test  | 9  | 4  | 5  |

👉 Le split est strictement réalisé au niveau WSI afin d’éviter toute fuite de données.

---

## 🧩 Pipeline global

### 1. Prétraitement des WSI
- Découpage en patchs **256×256**
- Filtrage des patchs non informatifs (fond, flou, faible contenu)

### 2. Embeddings patch-level
- **ViT-B/16** (baseline ImageNet)
- **DINOv2 ViT-B/14** (choix final)
- Dimension : 768
- Embeddings **gelés** (pas de fine-tuning)

### 3. Représentation spatiale : SPPR
- Génération de **chemins spatiaux de patchs** (random walks)
- Chemins indépendants, partiellement redondants
- Capture de la **continuité morphologique locale**

### 4. Modèle séquentiel
- Transformer Encoder
- Entrée : séquence de patchs (L × 768)
- Sortie : **un score par chemin**

### 5. Agrégation MIL
- Une WSI = sac de chemins
- Agrégation **WSI-level uniquement**
- Pooling principal : **log-sum-exp (LSE)** sur les logits

---

## 📊 Évaluation

- **Niveau d’évaluation** : exclusivement WSI-level
- **Métriques** :
  - ROC-AUC (principale)
  - Accuracy / Balanced Accuracy
  - Matrice de confusion (seuil ajustable)

⚠️ Le jeu de test contient seulement **9 WSI** :
les résultats sont interprétés avec prudence et servent principalement à valider
la cohérence méthodologique.

---

## 📈 Analyses complémentaires

- Courbe ROC WSI-level
- Visualisation des scores WSI et du seuil de décision
- Matrice de confusion
- **Ablation des stratégies d’agrégation MIL** :
  - mean / max / top-K (probas)
  - log-sum-exp (logits)

---

## 📄 Rapport et présentation

- 📘 **Rapport détaillé** : `report/report_sppr_wsi.pdf`
- 🎤 **Présentation Beamer** : `Diapo/Classification_de_lames_histologiques.pdf`

---

## 🔍 Message clé

> Ce travail met l’accent sur la **validité scientifique en supervision faible** :
> aucune prédiction patch-level, décision exclusivement WSI-level,
> et interprétation prudente des résultats compte tenu de la taille du dataset.

---

## 📬 Contact

Pour toute question ou discussion scientifique :

**Wassim Chikhi**  
Master 2 Vision et Machines Intelligentes  
Université Paris Cité

