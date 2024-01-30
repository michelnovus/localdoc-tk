# [MIT License] Copyright (c) 2024 Michel Novus

import customtkinter as ctk

APP_VERSION = "0.1.0"


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


class ToolBar(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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


class Application(ctk.CTk):
    def __init__(self, app_version: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Localdoc")
        self.bind("<Control-q>", lambda event: self.destroy())

        self.toolbar = ToolBar(
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
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = Application(APP_VERSION)
    app.mainloop()
