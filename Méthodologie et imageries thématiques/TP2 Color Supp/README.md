# 🧪 TP Couleur – Vision & Computational Pathology

**Auteur :** Wassim Chikhi  
**Master 2 Vision et Machine Intelligente — Université Paris Cité**  
**Module :** IFLCE075 – Méthodologie et Imageries Thématiques  
**Responsable :** Nicolas Loménie  

---

## 🔎 Introduction

Ce TP explore la perception et le traitement numérique de la couleur dans le contexte de la vision par ordinateur et de la pathologie computationnelle.  
La coloration histologique (H&E, H-DAB) repose sur des colorants dont la séparation est essentielle pour l’analyse morphologique et biochimique.  
Le TP met en œuvre les notions de perception, espaces couleur, luminance, densité optique et déconvolution couleur.

---

## 🎯 Objectifs du TP

- Manipuler et comprendre les espaces couleur **RGB** et **CIELab**.  
- Illustrer la nature vectorielle de la couleur et le **Color Display Paradox**.  
- Comparer la luminance physique **Y** et la luminance perceptuelle **L\***.  
- Implémenter la **déconvolution couleur (Ruifrok & Johnston)** pour les colorations **H&E** et **H-DAB**.  
- Étudier l’impact de matrices correctes vs incorrectes lors de la séparation des colorants.  
- Appliquer les méthodes à des images naturelles et à des images histologiques réelles.

---

## 📘 Architecture du notebook

### 1. **Image de Normandie**
- Split des canaux R, G, B  
- Permutation des canaux → *Color Display Paradox*  
- Explication : dépendance du gamut et du dispositif d’affichage  

### 2. **Image du Clown**
- Split RGB  
- Histogrammes des canaux  
- Calcul de la luminance **Y**  
- Conversion en espace **CIELab (L\*, a\*, b\*)**  
- Comparaison L\* vs Y  

### 3. **Image du Mandrill**
- RGB + Lab  
- Analyse des histogrammes  
- Étude des contrastes perceptuels  

### 4. **Déconvolution couleur (Ruifrok & Johnston, 2001)**
Pipeline implémenté :

1. Conversion **RGB → Densité optique (OD)**  
2. Normalisation des vecteurs de taches  
3. Construction de la matrice inverse  
4. Séparation des colorants  
5. Reconstruction H, E, DAB  

Cas abordés :

- Déconvolution **H&E standard**  
- Déconvolution **H&E incorrecte** (artefacts → instabilité)  
- Déconvolution **H-DAB** (ZoomBrownish)  
- Tests avec vecteurs faux  
- Application finale sur **YTMA10**  

---

## 🧠 Concepts essentiels expliqués dans le README

### 🔸 Pourquoi RGB n’est pas suffisant ?
- Dépend du matériel → pas perceptuellement uniforme  
- Le même triplet peut donner des couleurs différentes : *Color Display Paradox*

### 🔸 Avantages du CIELab
- Sépare **luminance (L\*)** et **chrominance (a\*, b\*)**  
- Uniformité perceptuelle → distances cohérentes visuellement

### 🔸 Le marron DAB n’est pas une couleur fondamentale
- Couleur composite (orange sombre + faible luminance)  
- Nécessite un passage en **densité optique (OD)** pour une séparation linéaire

### 🔸 Sensibilité extrême de la déconvolution
- Une matrice de taches incorrecte → artefacts, inversions, bruit  
- Importance de la calibration

### 🔸 Pourquoi utiliser la densité optique ?
- Suit la loi de Beer–Lambert :  
  OD = -log(I / I0)  
- Les contributions des colorants sont linéaires uniquement en OD

---

## 📁 Données utilisées

- `normandy.jpg`  
- `clown.png`  
- `mandrill.tif`  
- `sampleHE.tif`  
- `ZoomBrownish.tif`  
- `ytma10_010704_benign1_ccd.tif`

---

## ⚙️ Installation

### Librairies requises :

```bash
pip install numpy scipy scikit-image matplotlib opencv-python pillow
```

---

## ▶️ Exécution du notebook

```bash
git clone https://github.com/vvazzim/Tp-VMI-Wassim
cd tp-couleur
```

Ouvrir ensuite le notebook (Jupyter / VSCode / Google Colab).

---

## 📊 Exemples de résultats

- Illustrations du **Color Display Paradox**  
- Comparaison **Y vs L\***  
- Séparation correcte H&E (H violet, E rose)  
- Effets d’une mauvaise matrice (artefacts visibles)  
- Déconvolution **H-DAB**  
- Déconvolution sur tissu réel (YTMA10)  

---

## 📚 Références

- *ColorDisplayParadox.pdf*  
- Ruifrok & Johnston, *Quantification of histochemical staining by color deconvolution*, J Histochem Cytochem, 2001  
- CIE, *Colorimetry*, Third Edition, 2004  

---

## 📄 Rapport associé

Le rapport PDF est disponible dans :

```
report/TP_Couleur_Wassim.pdf
```

---

## © Licence

Projet académique – Master VMI  
© 2025 — Wassim Chikhi  
