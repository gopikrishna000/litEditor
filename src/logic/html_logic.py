# logic for generating html string from markdown string
from markdown2 import Markdown

from src.utils import Observable


def use_html_logic(markdown_string: Observable, html_string: Observable):
    # markdown to html logic
    md = Markdown()

    def on_markdown_change(markdown_text):
        html_text = md.convert(markdown_text)
        html_string.dispatch(html_text)

    markdown_string.observe(on_markdown_change)
