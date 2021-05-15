from tkinter import Frame

from src.utils import Observable


def get_md_preview_frame(master, html_string: Observable):
    # todo: observe changes from html_string
    return Frame(master)
