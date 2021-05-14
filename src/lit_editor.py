# main window of the app
from src.logic import FileLogic, HtmlLogic
from src.utils import Observable


class LitEditor:
    def __init__(self):
        # observables
        self.file_path_string = Observable()
        self.markdown_string = Observable()
        self.html_string = Observable()

        # logic
        self.file_logic = FileLogic(self.file_path_string, self.markdown_string)
        self.html_logic = HtmlLogic(self.markdown_string, self.html_string)

        # todo: ui
