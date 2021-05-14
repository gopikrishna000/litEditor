from src.utils import Lifecycle, Observable


class FileFrame(Lifecycle):
    def __init__(self, file_path_string: Observable):
        super().__init__()
