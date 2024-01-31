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
                "fg_color": "#940000",
                "hover_color": "#6e0000",
                "border_color": "#cccccc",
            },
            "info_button": {
                "fg_color": "transparent",
                "hover_color": "#005dd6",
                "border_color": "#cccccc",
            },
            "edit_button": {
                "fg_color": "transparent",
                "hover_color": "#bb3006",
                "border_color": "#cccccc",
            },
            "delete_button": {
                "fg_color": "transparent",
                "hover_color": "#940000",
                "border_color": "#cccccc",
            },
        }

        self.images = images
        self.position = position

        self.name = ctk.CTkLabel(
            master=self,
            text=package_name,
            justify="left",
            font=ctk.CTkFont(size=16),
            text_color="#e0e0e0",
        )
        self.served_in = ctk.CTkButton(
            master=self,
            text="",
            anchor="w",
            font=ctk.CTkFont(size=16, underline=True, slant="italic"),
            text_color="#3399ff",
            fg_color="transparent",
            hover=False,
            border_width=0,
        )
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
            width=70,
            border_spacing=4,
        )
        self.info_button = ctk.CTkButton(
            master=self,
            text="",
            corner_radius=5,
            border_width=1,
            border_color=self.colors["info_button"]["border_color"],
            image=self.images.get("help-filled.svg", (26, 26)),
            compound="top",
            fg_color=self.colors["info_button"]["fg_color"],
            hover_color=self.colors["info_button"]["hover_color"],
            width=0,
            border_spacing=4,
        )
        self.edit_button = ctk.CTkButton(
            master=self,
            text="",
            corner_radius=5,
            border_width=1,
            border_color=self.colors["edit_button"]["border_color"],
            image=self.images.get("pen.svg", (26, 26)),
            compound="top",
            fg_color=self.colors["edit_button"]["fg_color"],
            hover_color=self.colors["edit_button"]["hover_color"],
            width=0,
            border_spacing=4,
        )
        self.delete_button = ctk.CTkButton(
            master=self,
            text="",
            corner_radius=5,
            border_width=1,
            border_color=self.colors["delete_button"]["border_color"],
            image=self.images.get("trash-1.svg", (26, 26)),
            compound="top",
            fg_color=self.colors["delete_button"]["fg_color"],
            hover_color=self.colors["delete_button"]["hover_color"],
            width=0,
            border_spacing=4,
        )

        self.grid_columnconfigure(0, minsize=70)
        self.name.grid(row=0, column=1, sticky="e", pady=10)
        self.grid_columnconfigure(2, minsize=5)
        self.served_in.grid(row=0, column=3, padx=0, sticky="e")
        self.grid_columnconfigure(4, weight=1)
        self.serve_button.grid(row=0, column=5, padx=10, pady=5, sticky="nsew")
        self.grid_columnconfigure(6, minsize=15)
        self.info_button.grid(row=0, column=7, padx=10, pady=5, sticky="nsew")
        self.edit_button.grid(row=0, column=8, padx=10, pady=5, sticky="nsew")
        self.delete_button.grid(row=0, column=9, padx=10, pady=5, sticky="nsew")
        self.grid_columnconfigure(10, minsize=70)

    def change_serve_state(self, state: str):
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

    def change_position(self, position: int):
        self.position = position

    def set_serve_location(self, text: str):
        self.served_in.configure(text=text)

    def change_state_serve_button(self, state: bool):
        if state:
            self.serve_button.configure(state="normal")
        else:
            self.serve_button.configure(state="disabled")
