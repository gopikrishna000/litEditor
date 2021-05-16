import os
from tkinter import Button, FLAT

import numpy as np
from PIL import ImageTk, Image

from src.anim.anim_controller import AnimController
from src.styles.theme import color


class TabButton(Button):
    def __init__(self, master, **kw):
        self.img = None
        image_name = kw.pop('image')

        # get icon of the tab
        script_dir = os.path.dirname(__file__)
        rel_path = "../../assets/" + image_name + ".png"
        abs_file_path = os.path.join(script_dir, rel_path)
        icon = Image.open(abs_file_path).resize((32, 32), ).convert('RGBA')

        # create icon variants
        self.default_icon = generate_colored_icon(icon, color['low'])
        self.selected_icon = generate_colored_icon(icon, color['accent'])

        # styling
        kw['activebackground'] = color['surface']
        kw['bd'] = 0

        super().__init__(master, **kw)
        # initialize anim controller
        self.anim = AnimController(self, 0, 250, self.update_icon)

    def update_icon(self, blend):
        self.img = ImageTk.PhotoImage(Image.blend(self.default_icon, self.selected_icon, blend))
        self.configure(image=self.img)


def generate_colored_icon(icon, _color):
    pixels = np.array(icon)
    non_alpha = (pixels.T[3] != 0)
    rgb = hex_to_rgb(_color)
    pixels[..., :-1][non_alpha.T] = rgb  # Transpose back needed

    return Image.fromarray(pixels)


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
