# main window of the app
from tkinter import Frame, StringVar

from src.logic import use_file_logic, use_html_logic
from src.logic.tab_page_ui_logic import use_tab_page_ui_logic
from src.ui import get_md_edit_frame, get_md_preview_frame, get_file_frame, get_side_nav
from src.ui.fire_frame import get_fire_frame


def lit_editor(master):
    # observables
    file_path_var = StringVar()
    markdown_var = StringVar()
    html_var = StringVar()
    selected_tab = StringVar(value="file_tab")

    # logic
    use_file_logic(file_path_var, markdown_var)
    use_html_logic(markdown_var, html_var)

    # ui
    root = Frame(master)

    side_nav = get_side_nav(root, selected_tab)
    page_frame = Frame(root)

    side_nav.pack(expand=False, fill='both', side='left', anchor='nw')
    page_frame.pack(expand=True, fill='both', side='right')

    pages = [
        get_file_frame(page_frame, file_path_var),
        get_md_edit_frame(page_frame, markdown_var),
        get_fire_frame(page_frame, markdown_var, html_var),
        get_md_preview_frame(page_frame, html_var),
    ]

    # ui logic
    use_tab_page_ui_logic(selected_tab, pages)

    return root
