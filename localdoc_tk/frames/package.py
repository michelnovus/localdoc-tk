# [MIT License] Copyright (c) 2024 Michel Novus

import customtkinter as ctk
from localdoc_tk.assets import Images


class Package(ctk.CTkFrame):
    def __init__(
        self, images: Images, package_name: str, position: int, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.configure(corner_radius=20)

        self.colors = {
            "serve_button_not_served": {
                "fg_color": "transparent",
                "hover_color": "#00551c",
                "border_color": "#cccccc",
            },
            "serve_button_served": {
                "fg_color": "#6e0000",
                "hover_color": "#550000",
                "border_color": "#cccccc",
            },
        }

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
        self.serve_button = ctk.CTkButton(
            master=self,
            text="",
            corner_radius=5,
            border_width=1,
            border_color=self.colors["serve_button_not_served"]["border_color"],
            image=self.images.get("check-filled.svg", (26, 26)),
            compound="top",
            fg_color=self.colors["serve_button_not_served"]["fg_color"],
            hover_color=self.colors["serve_button_not_served"]["hover_color"],
            width=0,
            border_spacing=4,
        )

        self.grid_columnconfigure(0, minsize=30)
        self.name.grid(row=0, column=1, sticky="e", pady=10)
        self.grid_columnconfigure(2, minsize=5)
        self.served_in.grid(row=0, column=3, padx=0, sticky="e")
        self.grid_columnconfigure(4, weight=1)
        self.serve_button.grid(row=0, column=5, padx=10, pady=5, sticky="nsew")
        self.grid_columnconfigure(6, weight=1)

    def change_state_serve_button(self, state: str):
        """Change color and symbol state of serve_button. The parameter state
        should be string: {"SERVED" | "NOT_SERVED"}."""
        if state == "NOT_SERVED":
            self.serve_button.configure(
                image=self.images.get("check-filled.svg", (26, 26))
            )
            self.serve_button.configure(
                fg_color=self.colors["serve_button_not_served"]["fg_color"]
            )
            self.serve_button.configure(
                hover_color=self.colors["serve_button_not_served"][
                    "hover_color"
                ]
            )
            self._state = False
        elif state == "SERVED":
            self.serve_button.configure(
                image=self.images.get("close-filled.svg", (26, 26))
            )
            self.serve_button.configure(
                fg_color=self.colors["serve_button_served"]["fg_color"]
            )
            self.serve_button.configure(
                hover_color=self.colors["serve_button_served"]["hover_color"]
            )
            self._state = True
        else:
            raise ValueError(
                'state parameter should be: {"SERVED" | "NOT_SERVED"}'
            )
