from pathlib import Path
import cv2
import numpy as np
from ultralytics import YOLO
from tqdm import tqdm
from utils_io import read_video_info, make_writer, ensure_dir

def iou(a, b):
    xA = max(a[0], b[0])
    yA = max(a[1], b[1])
    xB = min(a[2], b[2])
    yB = min(a[3], b[3])
    inter = max(0, xB-xA) * max(0, yB-yA)
    areaA = (a[2]-a[0])*(a[3]-a[1])
    areaB = (b[2]-b[0])*(b[3]-b[1])
    return inter / (areaA + areaB - inter + 1e-6)

def q2_yolo_iou(video_path, out_path, max_frames=600):
    model = YOLO("yolov8n.pt")
    info = read_video_info(video_path)

    cap = cv2.VideoCapture(str(video_path))
    writer = make_writer(out_path, info.fps, info.w, info.h)

    tracks = {}
    next_id = 0

    for _ in tqdm(range(min(max_frames, info.n)), desc="Q2 YOLO+IoU"):
        ok, frame = cap.read()
        if not ok:
            break

        res = model(frame, conf=0.35, verbose=False)[0]
        dets = []

        for b in res.boxes:
            if int(b.cls[0]) == 0:  # person
                x1,y1,x2,y2 = map(int, b.xyxy[0])
                dets.append((x1,y1,x2,y2))

        new_tracks = {}
        used = set()

        for tid, tb in tracks.items():
            best, bj = 0, -1
            for j, db in enumerate(dets):
                if j in used: continue
                v = iou(tb, db)
                if v > best:
                    best, bj = v, j
            if best > 0.3:
                new_tracks[tid] = dets[bj]
                used.add(bj)

        for j, db in enumerate(dets):
            if j not in used:
                new_tracks[next_id] = db
                next_id += 1

        tracks = new_tracks

        for tid,(x1,y1,x2,y2) in tracks.items():
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame,f"ID {tid}",(x1,y1-5),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

        writer.write(frame)

    cap.release()
    writer.release()
    print("✅ Q2 export:", out_path)

if __name__ == "__main__":
    video = Path("tracking/Walk1.mpeg")
    out   = Path("tracking_results/q2_yolo_iou.mp4")
    ensure_dir(out.parent)
    q2_yolo_iou(video, out)
