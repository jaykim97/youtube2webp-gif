import cv2
from typing import Tuple, List
from numpy import ndarray
from PIL.Image import Image

def extract_frames(video_link: str, output: str) -> List[Tuple[Image, int]]:
    vidcap = cv2.VideoCapture("example.mp4")
    success, image = vidcap.read()
    frames = []
    count = 0
    while success:
        image = _convert_cv2img_to_pilimg(image)
        frames.append((image, count))
        success,image = vidcap.read() #extract frame from video
        count += 1
    return frames


def _convert_cv2img_to_pilimg(cv2_image: ndarray) -> Image:
    cv2_image  = cv2.cvtColor(cv2_image , cv2.COLOR_BGR2RGB) #convert cv2 color for PIL image
    return Image.fromarray(cv2_image)