from PIL.Image import Image
from typing import List, Tuple

def animate_images_array(images_array: List[Tuple[Image, int]], video_duration, output_file) -> None:
    images_array[0].save(f"{output_file}.webp", save_all = True, append_images = images_array[1:], optimize=False, duration=video_duration, loop=1)
    return