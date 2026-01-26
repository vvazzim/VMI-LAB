from pathlib import Path
import cv2

def export_frames(video_path, out_dir, frames=(76, 96 , 150)):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    for k in frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, k)
        ok, fr = cap.read()
        if ok:
            out = out_dir / f"{Path(video_path).stem}_frame_{k}.png"
            cv2.imwrite(str(out), fr)
            print("saved", out)
    cap.release()

if __name__ == "__main__":
    export_frames("tracking_results/q1_csrt.mp4", "tracking_results/frames")
    export_frames("tracking_results/q2_yolo_iou.mp4", "tracking_results/frames")
