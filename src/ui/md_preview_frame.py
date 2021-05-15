from tkinter import Frame
from tkhtmlview import HTMLLabel

from src.utils import Observable


def get_md_preview_frame(master, html_string: Observable):

    md_prev_frame = HTMLLabel(master, background='white')
    val = md_prev_frame.get()

    def on_html_change():
        if val or val == '':
            html_string.dispatch(val)

    html_string.observe(on_html_change)
    return md_prev_frame
