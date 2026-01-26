from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import cv2
import time

@dataclass
class VideoInfo:
    fps: float
    w: int
    h: int
    n: int

def ensure_dir(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p

def read_video_info(video_path: Path) -> VideoInfo:
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise FileNotFoundError(f"Impossible d'ouvrir: {video_path}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return VideoInfo(float(fps), w, h, n)

def make_writer(out_path: Path, fps: float, w: int, h: int) -> cv2.VideoWriter:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    return cv2.VideoWriter(str(out_path), fourcc, float(fps), (w, h))

class SimpleTimer:
    def __init__(self):
        self.t0 = time.time()
    def elapsed(self) -> float:
        return time.time() - self.t0
