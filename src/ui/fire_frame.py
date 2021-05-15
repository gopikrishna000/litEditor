from tkinter import Frame

from src.ui import get_md_edit_frame, get_md_preview_frame
from src.utils import Observable


def get_fire_frame(master, markdown_string: Observable, html_string: Observable):
    parent = Frame(master)
    edit_frame = get_md_edit_frame(parent, markdown_string)
    preview_frame = get_md_preview_frame(parent, html_string)

    # todo: pack it properly
    edit_frame.pack()
    preview_frame.pack()

    return parent
