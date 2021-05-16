# logic for generating html string from markdown string
from tkinter import StringVar

from markdown2 import Markdown


def use_html_logic(markdown_var: StringVar, html_var: StringVar):
    # markdown to html logic
    md = Markdown()

    def on_markdown_change(*_):
        markdown_text = markdown_var.get()
        print(markdown_text)
        html_text = md.convert(markdown_text)
        html_var.set(html_text)

    on_markdown_change()
    markdown_var.trace_add('write', on_markdown_change)
