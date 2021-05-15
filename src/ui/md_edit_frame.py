from tkinter import *
from tkinter import Text, font

from src.utils import Observable


def get_md_edit_frame(master, markdown_string: Observable):
    md_edit_frame = Text(master, width='1', height='1', font=font.Font(family='arial', size=14))

    def on_md_change(event=None):
        md_edit_frame.edit_modified(0)
        val = md_edit_frame.get("1.0", END)
        if val or val == '':
            markdown_string.dispatch(val)

    md_edit_frame.bind("<<Modified>>", on_md_change)
    return md_edit_frame
