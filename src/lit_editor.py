# main window of the app
from tkinter import Tk

from src.logic import use_file_logic, use_html_logic
from src.ui import get_md_edit_frame, get_md_preview_frame, get_file_frame
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

    # declare ui
    root = Tk()

    file_frame = get_file_frame(root, file_path_string)
    edit_frame = get_md_edit_frame(root, markdown_string)
    preview_frame = get_md_preview_frame(root, html_string)

    # todo: layout ui
    # directly packing for now
    edit_frame.pack()

    return root
