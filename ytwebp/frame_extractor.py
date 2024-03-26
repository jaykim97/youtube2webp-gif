import cv2
from typing import List
from numpy import ndarray
from PIL.Image import Image 
from PIL import Image as Img

def extract_frames(video_link: str) -> List[Image]:
    vidcap = cv2.VideoCapture(video_link)
    success, image = vidcap.read()
    frames = []
    while success:
        image = _convert_cv2img_to_pilimg(image)
        frames.append(image)
        success,image = vidcap.read() #extract frame from video
    return frames


def _convert_cv2img_to_pilimg(cv2_image: ndarray) -> Image:
    cv2_image  = cv2.cvtColor(cv2_image , cv2.COLOR_BGR2RGB) #convert cv2 color for PIL image
    return Img.fromarray(cv2_image)

def get_video_duration_seconds(video_link: str) -> float:
    vidcap = cv2.VideoCapture(video_link)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    numOfFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    durationInSeconds = numOfFrames//fps
    return durationInSeconds