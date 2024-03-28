from PIL.Image import Image
from typing import List

def animate_images_array(images_array: List[Image], output_file) -> None:
    images_array[0].save(f"{output_file}.webp", save_all = True, append_images = images_array[1:],duration= int(1000/30), optimize=False, loop=0)
    return