# GAN & VAE – Génération de sprites Pokémon

Ce dépôt contient le travail réalisé dans le cadre du TP de **Generative AI (M2 VMI)**,
portant sur la génération d’images de sprites Pokémon à l’aide de
**Variational Autoencoders (VAE)** et de **Generative Adversarial Networks (GAN / DCGAN)**.

---

## 📌 Contenu du dépôt

- `GANLab_To_complete2_Wassim_Chikhi.ipynb`  
  Notebook principal contenant :
  - l’implémentation du VAE
  - l’implémentation du GAN (DCGAN)
  - les essais d’hyperparamètres
  - les courbes de loss et visualisations

- `rapport_GAN_VAE.tex`  
  Rapport d’expérience au format LaTeX.

- `figures/`  
  Dossier contenant les figures utilisées dans le rapport :
  - courbes de loss GAN
  - images générées par le GAN
  - reconstructions et échantillons du VAE

---

## 🧠 Objectifs du TP

- Implémenter et entraîner un **VAE convolutionnel** pour la reconstruction et la génération d’images.
- Implémenter un **GAN de type DCGAN** pour générer des sprites Pokémon réalistes.
- Étudier l’influence des hyperparamètres (learning rate, dimension latente, nombre d’époques).
- Comparer qualitativement les résultats du VAE et du GAN.

---

## ⚙️ Environnement

- Python 3
- PyTorch
- torchvision
- matplotlib
- Jupyter Notebook
- GPU CUDA (optionnel)

---

## ▶️ Exécution

Ouvrir le notebook principal :

```bash
jupyter notebook GANLab_To_complete2_Wassim_Chikhi.ipynb
```

Puis exécuter les cellules dans l’ordre.

---

## 📊 Résultats principaux

- Le **VAE** permet de bonnes reconstructions mais génère des images floues lors de l’échantillonnage.
- Le **GAN (DCGAN)** produit des images visuellement plus réalistes, mais son entraînement est plus sensible aux hyperparamètres.
- Un learning rate de `2e-4` et une dimension latente de `100` donnent les résultats les plus stables pour le GAN.

---

## 📎 Remarques

- Plusieurs essais intermédiaires ont été réalisés pour explorer les hyperparamètres.
- Tous les essais ne sont pas systématiquement sauvegardés visuellement ; les choix finaux sont justifiés dans le rapport.

---

## 👤 Auteur

**Wassim Chikhi**  
Master 2 Vision et Machine Intelligente  
Université Paris Cité  
Année universitaire 2025–2026
