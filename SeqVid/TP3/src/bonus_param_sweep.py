from __future__ import annotations
from pathlib import Path
import argparse
import time

import cv2
from tqdm import tqdm


COCO_PERSON = 0  # YOLO: person


def iou(a, b) -> float:
    # a,b: (x1,y1,x2,y2)
    xA = max(a[0], b[0])
    yA = max(a[1], b[1])
    xB = min(a[2], b[2])
    yB = min(a[3], b[3])

    inter = max(0, xB - xA) * max(0, yB - yA)
    areaA = max(0, a[2] - a[0]) * max(0, a[3] - a[1])
    areaB = max(0, b[2] - b[0]) * max(0, b[3] - b[1])
    return inter / (areaA + areaB - inter + 1e-6)


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def read_video_nframes(video_path: Path) -> int:
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise FileNotFoundError(f"Impossible d'ouvrir {video_path}")
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return n if n > 0 else 0


def run_one_setting(video_path: Path, yolo, conf: float, iou_thr: float, max_frames: int, ttl: int = 10):
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise FileNotFoundError(f"Impossible d'ouvrir {video_path}")

    tracks = {}   # tid -> last_box (x1,y1,x2,y2)
    lost = {}     # tid -> lost_count
    next_id = 0
    new_ids_proxy = 0

    t0 = time.time()
    processed = 0

    for _ in range(max_frames):
        ok, frame = cap.read()
        if not ok:
            break

        res = yolo.predict(frame, conf=conf, verbose=False)[0]
        dets = []
        for b in res.boxes:
            if int(b.cls[0]) != COCO_PERSON:
                continue
            x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
            dets.append((x1, y1, x2, y2))

        assigned = set()
        new_tracks = {}

        # init lost counters
        for tid in tracks.keys():
            lost.setdefault(tid, 0)

        # match old tracks -> detections by IoU
        for tid, prev in tracks.items():
            best_j, best_v = -1, 0.0
            for j, box in enumerate(dets):
                if j in assigned:
                    continue
                v = iou(prev, box)
                if v > best_v:
                    best_v, best_j = v, j

            if best_j >= 0 and best_v >= iou_thr:
                new_tracks[tid] = dets[best_j]
                assigned.add(best_j)
                lost[tid] = 0
            else:
                lost[tid] += 1
                if lost[tid] <= ttl:
                    new_tracks[tid] = prev

        # create new tracks for unmatched detections
        for j, box in enumerate(dets):
            if j in assigned:
                continue
            new_tracks[next_id] = box
            lost[next_id] = 0
            next_id += 1
            new_ids_proxy += 1

        # prune dead tracks
        tracks = {tid: box for tid, box in new_tracks.items() if lost.get(tid, 0) <= ttl}

        processed += 1

    cap.release()
    dt = time.time() - t0
    fps = processed / dt if dt > 1e-6 else 0.0

    return {
        "conf": conf,
        "iou_thr": iou_thr,
        "frames": processed,
        "seconds": dt,
        "fps": fps,
        "newIDs_proxy": new_ids_proxy,
        "tracks_end": len(tracks),
    }


def sweep(video_path: Path, out_csv: Path, max_frames: int, ttl: int,
          conf_list=(0.25, 0.35), iou_list=(0.20, 0.30)):
    from ultralytics import YOLO
    yolo = YOLO("yolov8n.pt")

    n_total = read_video_nframes(video_path)
    n_use = max_frames if n_total == 0 else min(max_frames, n_total)

    rows = []
    for conf in conf_list:
        for iou_thr in iou_list:
            print(f"\n=== conf={conf} | iou_thr={iou_thr} | frames={n_use} ===")
            r = run_one_setting(video_path, yolo, conf, iou_thr, n_use, ttl=ttl)
            rows.append(r)
            print(f"-> fps={r['fps']:.2f} | newIDs_proxy={r['newIDs_proxy']} | tracks_end={r['tracks_end']}")

    ensure_dir(out_csv.parent)
    with out_csv.open("w", encoding="utf-8") as f:
        f.write("conf,iou_thr,frames,seconds,fps,newIDs_proxy,tracks_end\n")
        for r in rows:
            f.write(f"{r['conf']},{r['iou_thr']},{r['frames']},{r['seconds']:.4f},{r['fps']:.4f},{r['newIDs_proxy']},{r['tracks_end']}\n")

    print("\n✅ Bonus param sweep OK ->", out_csv)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", type=str, default="tracking/redcaroverlay3.mp4")
    ap.add_argument("--out_csv", type=str, default="tracking_results/bonus_param_sweep.csv")
    ap.add_argument("--max_frames", type=int, default=600)
    ap.add_argument("--ttl", type=int, default=10)
    args = ap.parse_args()

    sweep(Path(args.video), Path(args.out_csv), max_frames=args.max_frames, ttl=args.ttl)


if __name__ == "__main__":
    main()
