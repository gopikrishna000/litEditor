# logic for generating html string from markdown string
from src.utils import Lifecycle, Observable


class HtmlLogic(Lifecycle):
    def __init__(self, markdown_string: Observable, html_string: Observable):
        super().__init__()
        # markdown to html logic
