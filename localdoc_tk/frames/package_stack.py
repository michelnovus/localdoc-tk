# [MIT License] Copyright (c) 2024 Michel Novus

import customtkinter as ctk


class PackageStack(ctk.CTkScrollableFrame):
    """It's the container of entries `Package`."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
