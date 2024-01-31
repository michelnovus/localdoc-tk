# [MIT License] Copyright (c) 2024 Michel Novus

import customtkinter as ctk


class ToolBar(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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
