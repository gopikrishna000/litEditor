from tkinter import Frame

from src.ui import get_md_edit_frame, get_md_preview_frame
from src.utils import Observable


def get_fire_frame(master, markdown_string: Observable, html_string: Observable):
    parent = Frame(master)
    edit_frame = get_md_edit_frame(parent, markdown_string)
    preview_frame = get_md_preview_frame(parent, html_string)

    edit_frame.grid(row=0, column=0, sticky="nsew")
    preview_frame.grid(row=0, column=1, sticky="nsew")

    parent.grid_columnconfigure(0, weight=1, uniform="group1")
    parent.grid_columnconfigure(1, weight=1, uniform="group1")

    parent.grid_rowconfigure(0, weight=1)

    return parent
