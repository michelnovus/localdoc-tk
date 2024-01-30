# [MIT License] Copyright (c) 2024 Michel Novus

import customtkinter as ctk


class Application(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Localdoc")
        self.bind("<Control-q>", lambda event: self.destroy())


def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = Application()
    app.mainloop()
