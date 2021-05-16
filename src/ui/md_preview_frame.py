from tkinter import StringVar

from tkhtmlview import HTMLLabel


def get_md_preview_frame(master, html_var: StringVar):
    md_prev_frame = HTMLLabel(master, width='1', height='1', background='white')

    def on_html_change(*_):
        html_text = html_var.get()
        md_prev_frame.set_html(html_text)

    on_html_change()
    html_var.trace_add('write', on_html_change)

    return md_prev_frame
