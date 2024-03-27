import cv2
from typing import List
from PIL.Image import Image 
from PIL import Image as Img
from subprocess import Popen
import ffmpeg
import numpy as np


def extract_frames(url: str, process: Popen) -> List[Image]:
    probe = ffmpeg.probe(url)
    video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    width = int(video_info['width'])
    height = int(video_info['height'])
    frames = []
    while True:
        # Read a single frame as raw bytes
        in_bytes = process.stdout.read(width * height * 3)
        if not in_bytes:
            break

        # Convert raw bytes to numpy array
        frame = np.frombuffer(in_bytes, np.uint8).reshape([height, width, 3])

        # Convert numpy array to PIL Image
        frame_pil = Img.fromarray(frame)
        # Append the PIL Image to the list of frames
        frames.append(frame_pil)

    process.wait()
    return frames

def get_video_duration_seconds(video_link: str) -> float:
    vidcap = cv2.VideoCapture(video_link)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    numOfFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    durationInSeconds = numOfFrames//fps
    return durationInSeconds