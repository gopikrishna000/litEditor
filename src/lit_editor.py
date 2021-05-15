# main window of the app
from tkinter import Tk, Frame

from src.logic import use_file_logic, use_html_logic
from src.logic.tab_page_ui_logic import use_tab_page_ui_logic
from src.ui import get_md_edit_frame, get_md_preview_frame, get_file_frame
from src.ui.fire_frame import get_fire_frame
from src.utils import Observable


def lit_editor():
    # observables
    file_path_string = Observable("")
    markdown_string = Observable("")
    html_string = Observable("")
    selected_tab = Observable("file_tab")

    # logic
    use_file_logic(file_path_string, markdown_string)
    use_html_logic(markdown_string, html_string)

    # ui
    root = Tk()

    # todo: side_nav ui

    page_frame = Frame(root)
    page_frame.pack()  # todo: pack properly

    pages = [
        get_file_frame(page_frame, file_path_string),
        get_md_edit_frame(page_frame, markdown_string),
        get_fire_frame(page_frame, markdown_string, html_string),
        get_md_preview_frame(page_frame, html_string),
    ]

    # ui logic
    use_tab_page_ui_logic(selected_tab, pages)

    return root
