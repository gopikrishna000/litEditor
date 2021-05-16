from tkinter import StringVar

from tkhtmlview import HTMLLabel

from src.styles.theme import color


def get_md_preview_frame(master, html_var: StringVar):
    md_prev_frame = HTMLLabel(master, width='1', height='1', background=color['shell-dark'], padx=16, pady=16)

    def on_html_change(*_):
        # todo: find if there is any simpler way to change font color
        html_text = '<div style=\"color:' + color['on-shell'] + ';\">' + html_var.get() + '</div>'
        md_prev_frame.set_html(html_text)

    on_html_change()
    html_var.trace_add('write', on_html_change)
    return md_prev_frame
