from tkinter import *
from tkinter import Text, font

from src.styles.theme import color
from src.ui.text_area import get_text_area


def get_md_edit_frame(master, markdown_var: StringVar):
    md_edit_text = get_text_area(master,
                                 textvariable=markdown_var,
                                 width='1',
                                 height='1',
                                 bd=0,
                                 bg=color['shell'],
                                 fg=color['on-shell'],
                                 font=font.Font(family='arial', size=14),
                                 padx=16, pady=16,
                                 insertbackground=color['on-shell']
                                 )
    return md_edit_text
