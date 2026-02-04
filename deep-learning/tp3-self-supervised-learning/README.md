# TP3 — Apprentissage Auto-Supervisé (SSL)
**Auteur : Wassim CHIKHI — M2 VMI 2025**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vvazzim/Tp-VMI-Wassim/blob/main/deep-learning/tp3-self-supervised-learning/notebooks/Self_Supervised_Learning_Demos_final.ipynb)

---

## Objectif
Explorer et comparer plusieurs **tâches prétextes** en apprentissage auto-supervisé (SSL) sur **CIFAR-10** et **STL-10**, afin d’évaluer leur capacité à apprendre des représentations transférables vers des tâches de classification supervisée (linear probe).

---

## Configuration
- **Encodeur** : ResNet-18  
- **Optimiseur** : Adam *(lr = 0.001, batch = 256)*  
- **Datasets** : CIFAR-10 (32×32), STL-10 (96×96)  
- **Entraînement** : 20 epochs (prétexte) + 5 epochs (linear probe)  
- **Plateforme** : Google Colab (GPU T4)

---

## Méthodologie
- Implémentation de la tâche prétexte **Relative Patch Location** (Doersch et al., 2015).  
- Comparaison avec trois autres approches : **Rotation Prediction**, **Inpainting**, **SimCLR**.  
- Évaluation : entraînement d’un **classifieur linéaire** sur les représentations gelées.  
- Mesure : **Accuracy downstream** sur les deux datasets.

---

## Résultats (linear probe)

| Tâche prétexte | CIFAR-10 | STL-10 |
|----------------|-----------|--------|
| Relative Patch | **35.8 %** | **25.1 %** |
| Rotation       | **43.7 %** | **43.1 %** |
| Inpainting     | **40.2 %** | **27.3 %** |
| SimCLR         | **44.6 %** | **41.1 %** |

**Analyse :**  
- *Relative Patch* → capte bien la géométrie locale mais peine à généraliser.  
- *Rotation* → meilleure compréhension globale, très stable entre datasets.  
- *Inpainting* → correct sur CIFAR-10, limité sur STL-10.  
- *SimCLR* → excellentes performances grâce à son apprentissage contrastif.

---

## Conclusion
Les tâches **globales ou contrastives** (SimCLR, Rotation) fournissent les meilleures représentations pour le transfert.  
*Relative Patch* reste pertinente comme complément géométrique dans des approches multi-tâches.

**Perspectives :**
- Entraînement plus long (epochs ↑)  
- Fine-tuning de l’encodeur  
- Fusion de plusieurs tâches prétextes

---

## Liens utiles  
- Notebook Colab : [`notebooks/Self_Supervised_Learning_Demos_final.ipynb`](./notebooks/Self_Supervised_Learning_Demos_final.ipynb)  
- Rapport PDF : [`rapport/rapport_SSL.pdf`](./rapport/rapport_SSL.pdf)

---

## 📚 Références
- Doersch M. et al. *Unsupervised visual representation learning by context prediction* (ICCV 2015).  
- Gidaris S. et al. *Unsupervised representation learning by predicting image rotations* (arXiv 2018).  
- Chen T. et al. *SimCLR: A Simple Framework for Contrastive Learning* (arXiv 2020).  
- Pathak D. et al. *Context Encoders: Feature Learning by Inpainting* (CVPR 2016).  
