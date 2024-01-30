# [MIT License] Copyright (c) 2024 Michel Novus

import customtkinter as ctk


class Application(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = Application()
    app.mainloop()
