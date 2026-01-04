# Knowledge Distillation Lab — CIFAR-10 (ResNet50 → ResNet18)

Ce dépôt contient le notebook **final** (session-proof) et les éléments nécessaires pour reproduire les expériences de **Knowledge Distillation (KD)** sur **CIFAR-10**.

## Contenu

- `EfficientDL_KD_Lab.ipynb` (ou ton notebook final renommé)  
  Notebook Jupyter/Colab avec :
  - Teacher **ResNet50** (pré-entraîné ImageNet + fine-tuning CIFAR-10)
  - Student **ResNet18** (pré-entraîné ImageNet) baseline
  - KD **logits/scores**
  - KD **logits + feature maps**
  - Stratégie 2 : Student **from scratch** (baseline + KD logits)
  - Comparaisons + figures
- Checkpoints **persistants** sur Google Drive (dossier `KD_checkpoints`)
- Figures exportées (ex : `comparaison_finale.png`)

---

## Résultats (exécution notebook)

D’après les sorties de ta session (extraits) :

| Modèle | Test accuracy |
|---|---:|
| Teacher (ResNet50) | **0.9297** |
| Student baseline (ResNet18, pretrained) | **0.9213** |
| Student KD logits (ResNet18, pretrained) | **0.9312** |

> Remarque : la figure de comparaison globale (validation) inclut aussi **KD features** et la stratégie **scratch**.

---

## Prérequis

- Google Colab recommandé (GPU)
- Python ≥ 3.10
- PyTorch / torchvision
- matplotlib, tqdm

Dans Colab, tu peux installer/mettre à jour si nécessaire :

    pip install -U torch torchvision tqdm matplotlib

---

## Organisation des checkpoints (important)

Les checkpoints sont sauvegardés sur Drive dans :

    /content/drive/MyDrive/KD_checkpoints

Le notebook utilise un mode **train OR load** :
- Si un checkpoint existe → **load**
- Sinon → **train + save**

### Fichiers attendus

- `teacher_resnet50_best.pt`
- `student_pretrained_baseline_best.pt`
- `student_pretrained_kd_logits_best.pt`
- `student_pretrained_kd_features_best.pt`
- `student_scratch_baseline_best.pt`
- `student_scratch_kd_scores_best.pt`

---

## Exécution recommandée (Colab)

### 1) Monter Google Drive + définir CKPT_DIR

Exécuter la cellule **Drive + Audit** (au début du notebook) :

    from google.colab import drive
    drive.mount('/content/drive')

    import os
    CKPT_DIR = "/content/drive/MyDrive/KD_checkpoints"
    os.makedirs(CKPT_DIR, exist_ok=True)
    print("✅ CKPT_DIR =", CKPT_DIR)
    print("Fichiers:", os.listdir(CKPT_DIR))

### 2) Lancer le notebook

Tu peux exécuter dans l’ordre :
- Imports / seed / config
- Dataset + loaders
- Build models
- **Train OR load** (teacher, student baseline, KD logits, KD features, scratch)
- Tests + figures

> ⚠️ Si tu fais “Tout exécuter”, les blocs *train OR load* ne ré-entraîneront pas si les checkpoints existent.

---

## Export des figures

Le notebook sauvegarde la figure globale sur Drive :

- `comparaison_finale.png`

Optionnel : pour sauvegarder aussi la figure “test (3 modèles)”, ajoute :

    plt.savefig(f"{CKPT_DIR}/comparison_test_accuracy.png")

Puis copie tes figures depuis Drive vers le dossier local `figures/` (si tu compiles un rapport LaTeX en local).

---

## Rapport LaTeX

Le rapport suit une structure type M2 (Introduction → Données → Méthodes → Résultats → Discussion → Conclusion) et inclut :
- Hyperparamètres (lr, wd, epochs, batch size)
- Tailles de splits (45000/5000/10000)
- Comparaisons graphiques
- Table de résultats test

---

## Reproductibilité

- Seed fixée : `seed=42`
- Split train/val reproductible via `torch.Generator().manual_seed(42)`
- Checkpoints persistants sur Drive : pas de perte entre sessions/comptes

---

## Notes & dépannage

### 1) “Ça ré-entraîne alors que j’ai un checkpoint”
Vérifie :
- que Drive est monté
- que `CKPT_DIR` pointe exactement au bon dossier
- que tu utilises bien le pattern :

    if os.path.exists(ckpt_path):
        load()
    else:
        train()

### 2) `teacher_hist is None`
Normal si tu as chargé un checkpoint (pas d’historique d’entraînement).  
Utilise des plots “robustes” ou évalue directement les modèles.

---

## Auteur

**Wassim Chikhi** — M2 VMI (2025/2026)
