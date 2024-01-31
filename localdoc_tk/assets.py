# [MIT License] Copyright (c) 2024 Michel Novus
"""Defines useful things to obtain the program assets."""

import os.path
import customtkinter as ctk
from PIL import Image as PILImage
from io import BytesIO
from cairosvg import svg2png
from localdoc_tk.constants import IMAGES_DIR


def get_image(name: str) -> str:
    """It returns the absolute path to image file into assets folder."""
    return os.path.join(IMAGES_DIR, name)


class Images(object):
    """It's contains the program images in memory."""

    def __init__(self):
        self.images = {}

    def load(self, path: str):
        """It loads the SVG images into memory."""
        png_image: bytes = svg2png(url=path)  # type: ignore
        buffer = BytesIO(png_image)
        self.images[os.path.split(path)[1]] = PILImage.open(buffer)

    def get(self, name: str, size: tuple[int, int] = (20, 20)) -> ctk.CTkImage:
        """It returns a CTkImage object with the identifying `name`, optionally
        change image size with `size` parameter."""
        image = ctk.CTkImage(self.images[name], size=size)
        return image
