# TP3 — GAN & VAE : Génération de sprites Pokémon

**Master 2 VMI — Multi-modalité et IA générative**

Ce TP porte sur la génération d'images de sprites Pokémon à l'aide de **Variational Autoencoders (VAE)** et de **Generative Adversarial Networks (GAN / DCGAN)**.

---

## 🎯 Objectifs du TP

- Implémenter et entraîner un **VAE convolutionnel** pour la reconstruction et la génération d'images
- Implémenter un **GAN de type DCGAN** pour générer des sprites Pokémon réalistes
- Étudier l'influence des hyperparamètres (learning rate, dimension latente, nombre d'époques)
- Comparer qualitativement les résultats du VAE et du GAN

---

## 📁 Structure du projet

```
TP 3 GaN-VAE/
├── ganlab-completed-by-wassim.ipynb   # Notebook principal
├── TP_GaN_VAE_WASSIM (1).pdf         # Rapport final
└── README.md
```

---

## 📌 Contenu du notebook

- Implémentation du **VAE** (encodeur, décodeur, loss ELBO)
- Implémentation du **DCGAN** (générateur, discriminateur)
- Essais d'hyperparamètres
- Courbes de loss et visualisations des images générées

---

## 📊 Résultats principaux

- Le **VAE** permet de bonnes reconstructions mais génère des images floues lors de l'échantillonnage
- Le **GAN (DCGAN)** produit des images visuellement plus réalistes, mais son entraînement est plus sensible aux hyperparamètres
- Paramètres stables pour le GAN : learning rate `2e-4`, dimension latente `100`

---

## ⚙️ Environnement

- Python 3, PyTorch, torchvision, matplotlib
- **GPU CUDA** recommandé (entraînement GAN)

```bash
pip install torch torchvision matplotlib jupyter
```

---

## ▶️ Exécution

```bash
jupyter notebook ganlab-completed-by-wassim.ipynb
```

Exécuter les cellules dans l'ordre.

---

## 👤 Auteur

**Wassim Chikhi** — Master 2 VMI — Université Paris Cité — 2025/2026
