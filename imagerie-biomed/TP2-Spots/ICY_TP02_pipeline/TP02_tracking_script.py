# -*- coding: utf-8 -*-
# === ICY TP02 — Save active sequence (pixels + ROIs + tracks) into ONE XML ===
# Run in: Plugins → Scripting → Script Editor → Lang: Python

from icy.main import Icy
from icy.file import Saver
from java.io import File
import os, time

# >>>>>>>>>>>>>>>>>>>> ADAPTE CE CHEMIN <<<<<<<<<<<<<<<<<<<<<
out_path = r"C:\Users\firmforme\Desktop\Tp-VMI-Wassim\imagerie-biomed\TP2-Spots\result\cell2D_timelapse_with_tracks.xml"
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 1) Récupère la séquence active (celle où tu vois les trajectoires)
seq = Icy.getMainInterface().getActiveSequence()
if seq is None:
    print("[ERREUR] Aucune séquence active. Clique d'abord sur la fenêtre avec les ROIs/Tracks puis relance le script.")
    raise SystemExit

# 2) Feedback rapide
name = seq.getName()
n_t = seq.getSizeT()
n_rois = 0 if seq.getROIs() is None else seq.getROIs().size()
print("[TP02] Séquence active: %s | T=%d | ROIs(tracks inclus)=%d" % (name, n_t, n_rois))

# 3) Crée le dossier si besoin
out_dir = os.path.dirname(out_path)
if out_dir and not os.path.exists(out_dir):
    os.makedirs(out_dir)

# 4) Sauvegarde en un seul fichier XML ICY
ok = Saver.save(seq, File(out_path), True)  # True = allow overwrite
print(("[OK] Sauvegarde:", out_path) if ok else ("[ERREUR] Echec de la sauvegarde:", out_path))

# 5) Petit check
time.sleep(0.5)
if os.path.exists(out_path):
    size_kb = os.path.getsize(out_path) / 1024.0
    print("[TP02] Fichier écrit (%.1f KB) → %s" % (size_kb, out_path))
else:
    print("[ERREUR] Le fichier n'existe pas après save(). Vérifie le chemin et les droits d'écriture.")
