# [MIT License] Copyright (c) 2024 Michel Novus
"""Builds the logical relationships of the program in the `Application` class
and provides the funtion `main` access point."""

import os
import os.path
import customtkinter as ctk
from localdoc_tk.assets import Images
from localdoc_tk.frames import *
from localdoc_tk.constants import *


class Application(ctk.CTk):
    def __init__(self, images: Images, app_version: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.images = images
        self.title("Localdoc")
        self.bind("<Control-q>", lambda event: self.destroy())

        self.toolbar = ToolBar(
            images,
            master=self,
            corner_radius=0,
            height=50,
            fg_color="#131313",
        )

        self.package_stack = PackageStack(
            master=self,
            corner_radius=15,
            fg_color="#191919",
        )

        self.status_bar = StatusBar(
            master=self,
            corner_radius=0,
            height=16,
            fg_color="#131313",
            app_version=app_version,
        )

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.toolbar.grid(row=0, column=1, padx=0, pady=0, sticky="ew")
        self.package_stack.grid(
            row=1, column=1, padx=12, pady=12, sticky="nsew"
        )
        self.status_bar.grid(row=2, column=1, padx=0, pady=0, sticky="ew")


def main():
    images = Images()
    with os.scandir(IMAGES_DIR) as dir_iter:
        for entry in dir_iter:
            if entry.is_file() and entry.name.endswith(".svg"):
                images.load(entry.path)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = Application(images, APP_VERSION)
    app.mainloop()
