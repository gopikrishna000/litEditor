from src.utils import Lifecycle, Observable


class MdEditFrame(Lifecycle):
    def __init__(self, markdown_string: Observable):
        super().__init__()
        # todo: observe changes from markdown_string
        # todo: update markdown_string on changes
