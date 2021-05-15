from tkinter import Text,font

from src.utils import Observable


def get_md_edit_frame(master, markdown_string: Observable):

    md_edit_frame = Text(master, font=font.Font(family='arial', size=14))

    def on_md_change():
        val = md_edit_frame.get()
        if val or val == '':
            markdown_string.dispatch(val)

    markdown_string.observe(on_md_change)
    return md_edit_frame
