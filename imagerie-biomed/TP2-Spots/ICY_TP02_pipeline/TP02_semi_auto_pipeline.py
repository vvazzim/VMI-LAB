
# -*- coding: utf-8 -*-
# ICY TP02 – Semi-automatic pipeline (Jython/Python)
# Usage (ICY): Plugins → Scripting → Script Editor → Lang: Python → open this file → Run
# Behavior:
#   1) Optionally load a sequence (if inputPath set), otherwise use the ACTIVE sequence.
#   2) Show a dialog: "Do detection + tracking now, then click OK to continue".
#   3) On OK, export TrackManager (XML/XLS) and save ONE ICY XML with pixels + ROIs + tracks.

from javax.swing import JOptionPane
from icy.main import Icy
from icy.file import Loader, Saver
from java.io import File
import os

# ------------------------ USER PATHS (edit to match your project) ------------------------
inputPath = r""  # e.g. r"C:\Users\you\Desktop\TP2-Spots\data\cell2D_timelapse.tif"
outDir    = r"C:\Users\firmforme\Desktop\Tp-VMI-Wassim\imagerie-biomed\TP2-Spots\result"
xlsName   = "tracking_results.xls"
tmXmlName = "trackManager.xml"
seqXmlName= "cell2D_timelapse_with_tracks.xml"
# ----------------------------------------------------------------------------------------

def ensure_dir(p):
    if p and not os.path.exists(p):
        os.makedirs(p)

def msg(title, text, msgType=JOptionPane.INFORMATION_MESSAGE):
    JOptionPane.showMessageDialog(None, text, title, msgType)

# 1) Load or get active sequence
seq = None
if inputPath and os.path.exists(inputPath):
    try:
        seq = Loader.loadSequence(inputPath, 0, True)  # virtual if available
    except:
        seq = None

if seq is None:
    seq = Icy.getMainInterface().getActiveSequence()

if seq is None:
    msg("TP02 – Erreur", "Aucune séquence. Ouvrez votre time-lapse et relancez le script.", JOptionPane.ERROR_MESSAGE)
    raise SystemExit

# 2) Pause for manual detection & tracking
instructions = u"TP02 – Étape MANUELLE\n\n1) Lancez Spot Detector puis Spot Tracking sur la séquence active.\n2) Vérifiez les trajectoires.\n\nCliquez OK quand le tracking est terminé pour procéder aux exports (XML/XLS)."
JOptionPane.showConfirmDialog(None, instructions, "TP02 – Pause (OK pour continuer)", JOptionPane.OK_CANCEL_OPTION)

# 3) Exports
ensure_dir(outDir)
outXls = os.path.join(outDir, xlsName)
outTm  = os.path.join(outDir, tmXmlName)
outSeq = os.path.join(outDir, seqXmlName)

# 3.a) Save ONE ICY XML (pixels + ROIs + tracks)
ok = Saver.save(seq, File(outSeq), True)
if not ok:
    msg("TP02 – Erreur", u"Échec de sauvegarde de la séquence XML:\n%s" % outSeq, JOptionPane.ERROR_MESSAGE)
else:
    print("[OK] Sequence saved to:", outSeq)

# 3.b) Assist user for TrackManager exports
final_text = u"Sauvegarde terminée.\n\n• Séquence ICY :\n  {seq}\n\nPour exporter depuis Track Manager :\n  • Export to XLS  →  {xls}\n  • Save track groups as XML  →  {tm}\n\n(Placez ces fichiers dans {outDir})".format(seq=outSeq, xls=outXls, tm=outTm, outDir=outDir)
msg("TP02 – Exports", final_text, JOptionPane.INFORMATION_MESSAGE)
print(final_text)
