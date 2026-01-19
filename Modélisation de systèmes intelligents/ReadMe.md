# Classification de Whole Slide Images par Chemins Spatiaux (SPPR)

Ce dépôt accompagne le projet de **classification de lames histologiques (WSI)** sous **supervision faible**, basé sur des **chemins spatiaux de patchs (SPPR)** et des **Transformers**, réalisé dans le cadre du **Master 2 Vision et Machines Intelligentes (Université Paris Cité)**.

---

## 🧠 Objectif

L'objectif est de produire une **décision binaire au niveau WSI (normal / tumoral)** à partir :
- d'annotations **uniquement WSI-level**,
- sans prédiction ni supervision patch-level,
- en exploitant la **cohérence spatiale** du tissu via des chemins ordonnés de patchs.

La méthode est conçue pour être **méthodologiquement rigoureuse** dans un cadre de supervision faible.

---

## 📊 Données

- **Dataset** : CAMELYON16 (sous-ensemble)
- **Nombre total de WSI** : 54

| Split | WSI | Normal | Tumoral |
|------|-----|--------|---------|
| Train | 39 | 17 | 22 |
| Validation | 8 | 3 | 5 |
| Test | 9 | 4 | 5 |

⚠️ Le partitionnement est effectué **strictement au niveau WSI** afin d'éviter toute fuite de données.

---

## 🧩 Pipeline global

1. **Extraction des patchs** (256×256)
2. **Filtrage qualité** (fond, flou, non-informatif)
3. **Embeddings patch-level** via DINOv2 ViT-B/14 (gelés)
4. **Construction d'un graphe spatial**
5. **Génération de chemins spatiaux (SPPR)** par random walks
6. **Encodage séquentiel des chemins** via Transformer
7. **Agrégation MIL au niveau WSI**
8. **Décision finale WSI-level**

---

## 🧠 Représentation et Modèle

### Embeddings
- Backbone : **DINOv2 ViT-B/14**
- Dimension : 768
- Auto-supervisé, embeddings gelés

### Chemins spatiaux (SPPR)
- Séquences ordonnées de patchs voisins
- Longueur variable
- Capturent une continuité morphologique locale

### Modèle
- Transformer Encoder
- Projection 768 → 256
- Gestion des longueurs variables (padding + masque)
- Sortie : **un score par chemin** (logit)

---

## 📦 Agrégation MIL (WSI-level)

Une WSI est modélisée comme un **sac de chemins**.

### Méthode principale
- **Top-K mean pooling** sur les probabilités chemin-level
- Compromis entre max-pooling (instable) et mean-pooling (dilution)

### Ablation
- Log-Sum-Exp (LSE) sur logits

La **décision finale est prise exclusivement au niveau WSI**.

---

## 📈 Évaluation

- **Niveau d’évaluation** : WSI uniquement
- **Métriques** :
  - ROC-AUC (principale)
  - Accuracy, Balanced Accuracy
  - Matrice de confusion (seuil ajusté)

🎯 Le seuil de décision peut être ajusté afin de **privilégier la sensibilité**, ce qui est cliniquement pertinent en oncologie.

⚠️ Le jeu de test contient 9 WSI : les résultats sont interprétés avec prudence.

---

## 📂 Contenu du dépôt

```
.
├── notebook.ipynb              # Notebook Jupyter (entraînement + évaluation)
├── figures/                    # Figures utilisées dans le rapport et la présentation
│   ├── pipeline_precis.png
│   ├── roc_curve_wsi.png
│   ├── confusion_matrix_wsi.png
│   └── ablation_pooling_auc.png
├── report.tex                  # Rapport LaTeX
├── presentation.tex            # Slides Beamer
└── README.md                   # Ce fichier
```

---

## 🧪 Reproductibilité

- Code exécuté sous **PyTorch**
- Environnement type : **Kaggle / Google Colab (GPU)**
- Tous les résultats (figures, métriques) sont générés dans le notebook

---

## 📌 Remarques importantes

- Aucune prédiction patch-level n'est interprétée
- Les scores chemin-level ne sont jamais évalués comme résultats finaux
- L'accent est mis sur la **validité méthodologique**, pas sur la performance brute

---

## 👤 Auteur

**Wassim Chikhi**  
Master 2 Vision et Machines Intelligentes  
Université Paris Cité  
Année académique 2025–2026

---

## 📜 Licence

Projet académique – usage pédagogique et scientifique uniquement.

