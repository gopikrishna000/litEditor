from tkinter import Text

from src.utils import Observable


def get_md_edit_frame(master, markdown_string: Observable):
    # todo: observe changes from markdown_string
    # todo: update markdown_string on changes
    return Text()
