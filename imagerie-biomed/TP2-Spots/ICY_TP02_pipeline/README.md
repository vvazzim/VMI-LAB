# ICY_TP02_pipeline (Python/Jython only)

Ce dossier contient les outils pour finaliser et archiver le TP2 ICY **sans protocole .icy** ni Groovy.

## Contenu
- `TP02_tracking_script.py` : sauvegarde **UN** fichier XML ICY ré-ouvrable (pixels + ROIs + tracks) depuis la **séquence active**.
- `TP02_semi_auto_pipeline.py` : workflow **semi-automatique**. Le script s'arrête, vous faites détection+tracking, puis cliquez **OK** pour que le script sauvegarde et rappelle les exports.
- `TP02_tracking_blocks.txt` : spécification des blocs au cas où vous voulez reconstruire le pipeline visuellement.
- `TP02_tracking_howto.md` : pas-à-pas (Script Editor).
- `TP02_tracking_params.json` : paramètres de référence (chemins, seuils, linking, gap).

## Prérequis
- ICY (Windows)
- Script Editor disponible en **Lang: Python** (Jython)
- Avoir déjà exécuté **Spot Detector** puis **Spot Tracking** dans l'interface ICY (pour obtenir les trajectoires)

## Usage rapide

### A. Sauvegarder 1 seul XML ré-ouvrable
1. Dans ICY, cliquez sur la fenêtre qui **affiche les trajectoires** (elle devient séquence **active**).
2. `Plugins → Scripting → Script Editor → Lang: Python`
3. Ouvrez `TP02_tracking_script.py`
4. Éditez `OUT_PATH` si besoin (chemin de sortie).
5. **Run** → produit: `result/cell2D_timelapse_with_tracks.xml`

### B. Mode semi-automatique (pause → OK → export)
1. Script Editor (Lang: Python) → ouvrez `TP02_semi_auto_pipeline.py`
2. Laissez `inputPath` vide pour utiliser la séquence active, réglez `outDir` si besoin.
3. **Run** → faites **détection + tracking** → **OK** → sauvegarde XML unique et rappel des exports Track Manager.
   - Exports attendus dans `result/` :
     - `Interior.xlsx` (ROI Statistics)
     - `trackManager.xml` (Track Manager)

## Résultats à conserver (dossier `result/`)
- `cell2D_timelapse_with_tracks.xml`  ← séquence ICY ré-ouvrable (pixels+ROIs+tracks)
- `trackManager.xml`                  ← structure des pistes (Track Manager)
- `Interior.xlsx`                     ← mesures (durée, longueur, vitesse, intensité)

## Dépannage
- **Non-ASCII**: ouvrez les `.py`, vérifiez `# -*- coding: utf-8 -*-` en première ligne et **pas d'accents** dans le code.
- **Plusieurs XML _t0000…**: vous avez sauvé “en multiples fichiers”. Re-sauver via `TP02_tracking_script.py` (un seul fichier).
- **Pas de ROIs dans le XML**: la fenêtre active n’était pas la bonne. Cliquez la séquence avec trajectoires, relancez.
- **Mémoire ICY**: augmentez “Maximum memory” dans Preferences ou réduisez le nombre de spots (threshold ↑, scale 1 décochée).

---

📍 **Emplacement :**
`TP2-Spots/ICY_TP02_pipeline/README.md`
