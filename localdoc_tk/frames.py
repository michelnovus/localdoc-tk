# [MIT License] Copyright (c) 2024 Michel Novus

import customtkinter as ctk
from localdoc_tk.assets import Images


class ToolBar(ctk.CTkFrame):
    def __init__(self, images: Images, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.button_add = ctk.CTkButton(
            master=self,
            text="insertar",
            font=ctk.CTkFont(size=16, weight="bold"),
            image=images.get("add-filled.svg", (30, 30)),
            compound="left",
            corner_radius=0,
            fg_color="transparent",
            hover_color="#404040",
            border_width=2,
            border_color="#cccccc",
            width=130,
        )
        self.button_update = ctk.CTkButton(
            master=self,
            text="actualizar",
            font=ctk.CTkFont(size=16, weight="bold"),
            image=images.get("refresh.svg", (30, 30)),
            compound="left",
            corner_radius=0,
            fg_color="transparent",
            hover_color="#404040",
            border_width=2,
            border_color="#cccccc",
            width=130,
        )
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(0, minsize=10)
        self.button_add.grid(row=0, column=1, padx=10, pady=6, sticky="ew")
        self.button_update.grid(row=0, column=2, padx=10, pady=6, sticky="ew")


class StatusBar(ctk.CTkFrame):
    def __init__(self, app_version: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        version_label = ctk.CTkLabel(
            master=self,
            text=f"localdoc-tk v{app_version}",
            text_color="#e0e0e0",
            font=ctk.CTkFont(
                size=14,
                weight="bold",
                slant="italic",
            ),
        )
        self.grid_columnconfigure(1, weight=1)
        version_label.grid(row=0, column=2, padx=15, sticky="e")


class PackageStack(ctk.CTkScrollableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.stack: list[Package] = []


class Package(ctk.CTkFrame):
    def __init__(self, position: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(corner_radius=20)
        self.configure(height=45)

        self.position = position
