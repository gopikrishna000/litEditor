import os
from tkinter import Button

from PIL import ImageTk, Image


class TabButton(Button):
    def __init__(self, master, **kw):
        image_name = kw.get('image')

        script_dir = os.path.dirname(__file__)
        rel_path = "../../assets/" + image_name + ".png"
        abs_file_path = os.path.join(script_dir, rel_path)

        self.icon = ImageTk.PhotoImage(Image.open(abs_file_path).resize((48, 48), ).convert('RGBA'))
        kw['image'] = self.icon
        super().__init__(master, **kw)
