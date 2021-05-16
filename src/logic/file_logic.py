# logic for updating the file, importing it's content
from tkinter import StringVar

from src.utils.path import open_file


def use_file_logic(file_path_var: StringVar, markdown_var: StringVar):
    file = None

    # file opening logic
    def on_file_selected(*_):
        nonlocal file
        path = file_path_var.get()

        if file:
            file.close()

        if path == '':
            markdown_var.set('')  # clear markdown_string
            return

        file = open_file(path)
        content = file.read()

        markdown_var.set(content)

    # file updating logic todo: maybe with throttle
    def on_markdown_change(*_):
        if file:
            mdn_text = markdown_var.get()
            file.seek(0)
            file.write(mdn_text)
            file.truncate()

    on_file_selected()
    file_path_var.trace_add('write', on_file_selected)
    on_markdown_change()
    markdown_var.trace_add('write', on_markdown_change)
