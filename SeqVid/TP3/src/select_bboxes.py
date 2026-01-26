import cv2
import matplotlib.pyplot as plt

def select_bboxes_from_frame(frame_bgr, n_boxes=2):
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 8))
    plt.imshow(frame_rgb)
    plt.title(
        f"Clique 2 points par objet : haut-gauche puis bas-droit "
        f"(total {2*n_boxes} clics)"
    )
    plt.axis("off")

    pts = plt.ginput(2 * n_boxes, timeout=0)
    plt.close()

    bboxes = []
    for i in range(n_boxes):
        (x1, y1) = pts[2*i]
        (x2, y2) = pts[2*i + 1]

        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        x = min(x1, x2)
        y = min(y1, y2)
        w = abs(x2 - x1)
        h = abs(y2 - y1)

        bboxes.append((x, y, w, h))

    return bboxes
