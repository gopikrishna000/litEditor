from tkinter import Button
from PIL import ImageTk, Image

from src.anim.anim_controller import AnimController
from src.styles.theme import color
from src.utils import open_icon, generate_colored_icon


class TabButton(Button):
    def __init__(self, master, **kw):
        self.img = None
        image_name = kw.pop('image')

        # get icon of the tab
        icon = open_icon(image_name)

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
