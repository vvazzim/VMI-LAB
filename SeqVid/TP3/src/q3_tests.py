from pathlib import Path
import subprocess

def run(cmd):
    print(">>>", " ".join(cmd))
    subprocess.check_call(cmd)

# Walk1 : tester parametres
configs = [
    (0.25, 0.20),
    (0.35, 0.30),
    (0.50, 0.40),
]

for conf, iou in configs:
    out = f"tracking_results/q3_walk1_conf{conf}_iou{iou}.mp4"
    run(["python", "src/q2_yolo_iou.py",
         "--video", "tracking/Walk1.mpeg",
         "--out", out,
         "--conf", str(conf),
         "--iou_thr", str(iou),
         "--max_frames", "600"])

print("✅ Q3 terminé (Walk1).")
