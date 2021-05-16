from tkinter import *
from tkinter import Text, font


def get_md_edit_frame(master, markdown_var: StringVar):
    md_edit_frame = Text(master, width='1', height='1', font=font.Font(family='arial', size=14))

    def on_md_change(event=None):
        val = md_edit_frame.get()
        if val or val == '':
            markdown_var.set(val)

    # todo: update md_edit_frame on markdown_var changes without creating infinite loop

    #md_edit_frame.bind("<<Modified>>", on_md_change)
    return md_edit_frame
