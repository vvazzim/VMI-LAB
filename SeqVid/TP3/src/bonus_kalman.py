from __future__ import annotations
from pathlib import Path
import argparse
import time

import cv2
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# COCO ids (YOLOv8)
COCO = {"person": 0, "car": 2}

def kalman_2d_constant_velocity():
    # Etat: [x, y, vx, vy], mesure: [x, y]
    kf = cv2.KalmanFilter(4, 2)
    kf.transitionMatrix = np.array([[1,0,1,0],
                                    [0,1,0,1],
                                    [0,0,1,0],
                                    [0,0,0,1]], dtype=np.float32)
    kf.measurementMatrix = np.array([[1,0,0,0],
                                     [0,1,0,0]], dtype=np.float32)
    kf.processNoiseCov = np.eye(4, dtype=np.float32) * 1e-2
    kf.measurementNoiseCov = np.eye(2, dtype=np.float32) * 1e-1
    kf.errorCovPost = np.eye(4, dtype=np.float32)
    return kf

def extract_single_object_centroids_yolo(video_path: Path, yolo, class_name="person", conf=0.30, max_frames=300):
    cls_id = COCO[class_name]
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise FileNotFoundError(f"Impossible d'ouvrir {video_path}")

    centroids = []
    for _ in tqdm(range(max_frames), desc=f"Extract centroids ({class_name})"):
        ok, frame = cap.read()
        if not ok:
            break

        res = yolo.predict(frame, conf=conf, verbose=False)[0]

        # prendre la bbox la plus grande de la classe
        best = None
        best_area = 0.0
        for b in res.boxes:
            if int(b.cls[0]) != cls_id:
                continue
            x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
            area = float((x2 - x1) * (y2 - y1))
            if area > best_area:
                best_area = area
                best = (x1, y1, x2, y2)

        if best is None:
            centroids.append(None)
        else:
            x1, y1, x2, y2 = best
            cx = (x1 + x2) / 2.0
            cy = (y1 + y2) / 2.0
            centroids.append((cx, cy))

    cap.release()
    return centroids

def run_kalman_on_centroids(centroids):
    kf = kalman_2d_constant_velocity()

    first = next((c for c in centroids if c is not None), None)
    if first is None:
        raise RuntimeError("Aucune mesure trouvée (YOLO n'a rien détecté).")

    kf.statePost = np.array([[first[0]], [first[1]], [0], [0]], dtype=np.float32)

    pred_xy = []
    meas_xy = []
    for c in centroids:
        pred = kf.predict()
        px, py = float(pred[0]), float(pred[1])
        pred_xy.append((px, py))

        if c is None:
            meas_xy.append((np.nan, np.nan))
        else:
            mx, my = c
            meas_xy.append((mx, my))
            kf.correct(np.array([[mx], [my]], dtype=np.float32))

    return np.array(pred_xy, dtype=np.float32), np.array(meas_xy, dtype=np.float32)

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", type=str, default="tracking/Walk1.mpeg")
    ap.add_argument("--class_name", type=str, default="person", choices=["person", "car"])
    ap.add_argument("--conf", type=float, default=0.30)
    ap.add_argument("--max_frames", type=int, default=250)
    ap.add_argument("--out_png", type=str, default="tracking_results/bonus_kalman.png")
    ap.add_argument("--out_csv", type=str, default="tracking_results/bonus_kalman.csv")
    args = ap.parse_args()

    video = Path(args.video)
    out_png = Path(args.out_png)
    out_csv = Path(args.out_csv)
    ensure_dir(out_png.parent)

    from ultralytics import YOLO
    yolo = YOLO("yolov8n.pt")  # télécharge si besoin

    centroids = extract_single_object_centroids_yolo(video, yolo, class_name=args.class_name, conf=args.conf, max_frames=args.max_frames)
    pred_xy, meas_xy = run_kalman_on_centroids(centroids)

    # Save CSV (frame, meas_x, meas_y, pred_x, pred_y)
    with out_csv.open("w", encoding="utf-8") as f:
        f.write("frame,meas_x,meas_y,pred_x,pred_y\n")
        for i in range(len(pred_xy)):
            mx, my = meas_xy[i]
            px, py = pred_xy[i]
            f.write(f"{i},{mx},{my},{px},{py}\n")

    # Plot
    plt.figure(figsize=(7, 6))
    plt.plot(meas_xy[:, 0], meas_xy[:, 1], marker="o", linewidth=1, label="Mesure (YOLO)")
    plt.plot(pred_xy[:, 0], pred_xy[:, 1], marker="x", linewidth=1, label="Kalman (prédiction)")
    plt.gca().invert_yaxis()
    plt.title(f"Bonus Kalman: {args.class_name} | meas vs pred")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png, dpi=160)
    plt.close()

    print("✅ Bonus Kalman OK")
    print("PNG:", out_png)
    print("CSV:", out_csv)

if __name__ == "__main__":
    main()
