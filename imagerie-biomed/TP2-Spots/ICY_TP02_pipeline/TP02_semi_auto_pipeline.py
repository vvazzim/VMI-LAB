from icy.sequence import Sequence

# Récupérer la séquence active
seq = getSequence()

# Créer crop spatial (180x173) et temporel (0-100)
newSeq = Sequence()
newSeq.setName("Cropped_" + seq.getName())

for t in range(0, 101):  # Frames 0 à 100
    img = seq.getImage(t, 0)
    cropped = img.getSubimage(11, 29, 180, 173)  # x, y, width, height
    newSeq.setImage(t, 0, cropped)

addSequence(newSeq)