# Notebooks — Pipeline expérimental

Ce dossier contient l’ensemble des notebooks Jupyter implémentant
le pipeline expérimental du projet **Sujet 7 — Méthode 1**.

Les notebooks sont conçus pour être lus et exécutés dans l’ordre.

---

## 🧪 Étapes du pipeline

- 00 — Extraction et filtrage des patchs WSI
- 01 — Split stratifié au niveau WSI
- 02 — Extraction des embeddings patch-level (ViT / DINOv2)
- 03 — Génération des chemins spatiaux (SPPR)
- 04 — Entraînement Transformer + agrégation MIL
- 05 — Évaluation et analyses complémentaires

---

## ⚠️ Notes importantes

- Aucun label patch-level n’est utilisé
- Pas de fuite de données (split WSI-level)
- Objectif méthodologique et reproductibilité
