import os
from tkinter import Button

import numpy as np
from PIL import ImageTk, Image

from src.anim.anim_controller import AnimController


class TabButton(Button):
    def __init__(self, master, **kw):
        image_name = kw.pop('image')

        script_dir = os.path.dirname(__file__)
        rel_path = "../../assets/" + image_name + ".png"
        abs_file_path = os.path.join(script_dir, rel_path)

        self.default_icon = Image.open(abs_file_path).resize((32, 32), ).convert('RGBA')
        self.selected_icon = self.generate_selected_icon()

        super().__init__(master, **kw)
        self.anim = AnimController(self, 0, 250, self.update_icon)

    def update_icon(self, blend):
        self.img = ImageTk.PhotoImage(Image.blend(self.default_icon, self.selected_icon, blend))
        self.configure(image=self.img)

    def generate_selected_icon(self):
        pixels = np.array(self.default_icon)
        non_alpha = (pixels.T[3] != 0)

        pixels[..., :-1][non_alpha.T] = (255, 0, 0)  # Transpose back needed

        return Image.fromarray(pixels)
