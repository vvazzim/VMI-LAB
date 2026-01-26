from __future__ import annotations
from pathlib import Path
import argparse
import cv2
from tqdm import tqdm
from select_bboxes import select_bboxes_from_frame
from utils_io import read_video_info, make_writer, ensure_dir, SimpleTimer

def q1_csrt(video_path, out_path, max_frames=600, n_boxes=2):
    info = read_video_info(video_path)

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise FileNotFoundError(f"Impossible d'ouvrir {video_path}")

    # 1) Lire frame0 (pour sélectionner)
    ok, frame0 = cap.read()
    if not ok:
        cap.release()
        raise RuntimeError("Impossible de lire la première frame")

    # 2) Sélection bboxes (matplotlib)
    bboxes = select_bboxes_from_frame(frame0, n_boxes=n_boxes)
    if len(bboxes) == 0:
        cap.release()
        raise RuntimeError("Aucune bbox sélectionnée.")
    print("BBOXES sélectionnées :", bboxes)

    # 3) IMPORTANT: revenir au début pour traiter toute la vidéo
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ok, frame0 = cap.read()
    if not ok:
        cap.release()
        raise RuntimeError("Impossible de relire la frame 0 après reset")

    # 4) Init trackers
    trackers = []
    for bb in bboxes:
        trk = cv2.TrackerCSRT_create()
        trk.init(frame0, tuple(bb))
        trackers.append(trk)

    # 5) Writer
    writer = make_writer(out_path, info.fps, info.w, info.h)

    # Option: dessiner et sauver la 1ère frame aussi
    for i, (x, y, w, h) in enumerate(bboxes):
        cv2.rectangle(frame0, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame0, f"ID {i}", (x, max(0,y-8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
    writer.write(frame0)

    # 6) Boucle
    timer = SimpleTimer()
    n_iter = min(max_frames, max(0, info.n - 1))

    processed = 0
    for _ in tqdm(range(n_iter), desc="Q1 CSRT"):
        ok, frame = cap.read()
        if not ok:
            break

        for i, trk in enumerate(trackers):
            ok_t, bb = trk.update(frame)
            if ok_t:
                x, y, w, h = map(int, bb)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(frame, f"ID {i}", (x, max(0,y-8)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            else:
                cv2.putText(frame, f"ID {i} LOST", (20, 30+30*i),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

        writer.write(frame)
        processed += 1

    cap.release()
    writer.release()
    dt = timer.elapsed()
    print(f"✅ Q1 export: {out_path} | frames traitées={processed} | time={dt:.1f}s")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", type=str, default="tracking/Tracking2min.avi")
    ap.add_argument("--out", type=str, default="tracking_results/q1_csrt.mp4")
    ap.add_argument("--max_frames", type=int, default=600)
    args = ap.parse_args()

    video = Path(args.video)
    out = Path(args.out)
    ensure_dir(out.parent)
    q1_csrt(video, out, max_frames=args.max_frames)

if __name__ == "__main__":
    main()
