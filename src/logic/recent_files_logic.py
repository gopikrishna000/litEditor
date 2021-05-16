from tkinter import StringVar

from src.utils.convert import encode_lit_cache, decode_lit_cache
from src.utils.path import file_from_project_root, open_file

max_cache = 4


def use_recent_files_logic(files_var: StringVar):
    file = open_file(file_from_project_root('.litcache'))
    files_var.set(file.read())

    def add_to_recent(path: str):
        files = decode_lit_cache(files_var.get())

        # return if path already exists
        for p in files:
            if p == path:
                return

        if len(files) == max_cache:
            files.pop()
        files.append(path)
        files_var.set(encode_lit_cache(files))

    def on_files_var_change(*_):
        if file:
            file.seek(0)
            file.write(files_var.get())
            file.truncate()

    files_var.trace_add('write', on_files_var_change)

    return add_to_recent
