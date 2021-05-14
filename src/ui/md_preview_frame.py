from src.utils import Lifecycle, Observable


class MdPreviewFrame(Lifecycle):
    def __init__(self, html_string: Observable):
        super().__init__()
        # todo: observe changes from html_string
