from PIL.Image import Image
from typing import List

def animate_images_array(images_array: List[Image], fps: int, output_file: str) -> None:
    duration = _duration_calculation(fps)
    images_array[0].save(f"{output_file}.webp", save_all = True, append_images = images_array[1:], duration = duration, optimize=False, loop=0)
    return

def _duration_calculation(video_fps:int) -> float:
    duration = 1000/video_fps
    return duration