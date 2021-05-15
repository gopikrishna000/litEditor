from tkinter import Frame
from tkhtmlview import HTMLLabel

from src.utils import Observable


def get_md_preview_frame(master, html_string: Observable):
    md_prev_frame = HTMLLabel(master, width='1', height='1', background='white')

    def on_html_change(html_text):
        md_prev_frame.set_html(html_text)

    html_string.observe(on_html_change)
    return md_prev_frame
