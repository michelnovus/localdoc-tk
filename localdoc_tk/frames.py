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
    def __init__(
        self, images: Images, package_name: str, position: int, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.configure(corner_radius=20)

        self.images = images
        self.position = position

        self.name = ctk.CTkLabel(
            master=self,
            text=package_name,
            font=ctk.CTkFont(size=16),
            text_color="#e0e0e0",
        )
        self.served_in = ctk.CTkButton(
            master=self,
            text="algun lao",
            font=ctk.CTkFont(size=16, underline=True, slant="italic"),
            text_color="#3399ff",
            fg_color="transparent",
            hover=False,
            border_width=0,
        )
        self._state = False
        self.on_off_button = ctk.CTkButton(
            master=self,
            text="",
            corner_radius=5,
            border_width=1,
            border_color="#cccccc",
            image=self.images.get("check-filled.svg", (26, 26)),
            compound="top",
            fg_color="transparent",
            hover_color="#006622",
            width=0,
            border_spacing=4,
            command=self._change_check,
        )

        self.grid_columnconfigure(0, minsize=30)
        self.name.grid(row=0, column=1, sticky="e", pady=10)
        self.grid_columnconfigure(2, minsize=5)
        self.served_in.grid(row=0, column=3, padx=0, sticky="e")
        self.grid_columnconfigure(4, weight=1)
        self.on_off_button.grid(row=0, column=5, padx=10, pady=5, sticky="nsew")
        self.grid_columnconfigure(6, weight=1)

    # TEMP
    def _change_check(self, event=None):
        if self._state:
            self.on_off_button.configure(
                image=self.images.get("check-filled.svg", (25, 25))
            )
            self.on_off_button.configure(fg_color="transparent")
            self.on_off_button.configure(hover_color="#006622")
            self._state = False
        else:
            self.on_off_button.configure(
                image=self.images.get("close-filled.svg", (25, 25))
            )
            self.on_off_button.configure(fg_color="#990000")
            self.on_off_button.configure(hover_color="#660000")
            self._state = True
