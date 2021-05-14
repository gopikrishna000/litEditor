# logic for updating the file, importing it's content
from src.utils import Lifecycle, Observable


class FileLogic(Lifecycle):
    def __init__(self, file_path_string: Observable, markdown_string: Observable):
        super().__init__()
        # todo: file opening logic
        # todo: file updating logic maybe with throttle
