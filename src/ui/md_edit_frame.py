from tkinter import *
from tkinter import Text, font

from src.ui.text_area import get_text_area


def get_md_edit_frame(master, markdown_var: StringVar):
    md_edit_text = get_text_area(master,
                                 textvariable=markdown_var,
                                 width='1',
                                 height='1',
                                 font=font.Font(family='arial', size=14)
                                 )
    return md_edit_text
