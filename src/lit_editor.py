# main window of the app

from src.utils import Observable


class LitEditor:
    def __init__(self):
        self.file_path_string = Observable()
        self.markdown_string = Observable()
        self.html_string = Observable()
