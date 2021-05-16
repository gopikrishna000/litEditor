from tkinter import Frame, Button

from src.styles.theme import color
from src.utils.convert import decode_lit_cache


def get_recent_files_frame(master, file_path_var, files_var, bg):
    parent = Frame(master, height=100, width=500, bg=bg)

    def on_files_change(*_):
        files = decode_lit_cache(files_var.get())

        for slave in parent.pack_slaves():
            slave.destroy()

        for index, path in enumerate(files):
            frame = Frame(parent)

            # select button
            select_button = Button(frame, text=path, justify='left', anchor='w', padx=8, pady=8,
                                   bg=color['surface'], fg=color['medium'], bd=0,
                                   activebackground=color['accent'],
                                   activeforeground=color['high'])
            select_button.pack(expand=True, fill='both', side='left')

            # remove button
            if path != file_path_var.get():
                remove_button = Button(frame, width=8, text='X',
                                       bg=color['warn'], fg=color['high'], bd=0,
                                       activebackground=color['warn-dark'])
                remove_button.pack(expand=False, fill='both', side='right')

                remove_button.configure(command=lambda p=path: files_var.set(files_var.get().replace(p + '\n', '')))
                select_button.configure(command=lambda p=path: file_path_var.set(p))
            else:
                select_button.configure(bg=color['accent'])

            frame.pack(expand=True, fill='both', padx=4, pady=4)

    on_files_change()
    files_var.trace_add('write', on_files_change)
    file_path_var.trace_add('write', on_files_change)

    return parent
