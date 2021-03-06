from tkinter import Frame, Button, Label

from src.styles.theme import color
from src.utils.convert import decode_lit_cache, encode_lit_cache


def get_recent_files_frame(master, file_path_var, files_var, bg):
    parent = Frame(master, height=100, width=500, bg=bg)

    def on_files_change(*_):
        files = decode_lit_cache(files_var.get())

        for slave in parent.pack_slaves():
            slave.destroy()

        if len(files) == 0:
            label = Label(parent, text='Create or Open File to Edit', font=('arial', 14), fg=color['low'], bg=bg)
            label.pack(expand=True, fill='both')
        elif file_path_var.get() == '':
            label = Label(parent, text='Select file to Edit', font=('arial', 12), pady=16, fg=color['low'], bg=bg)
            label.pack(expand=True, fill='both')

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

                def on_remove(p=path):
                    _files = decode_lit_cache(files_var.get())
                    _files.remove(p)
                    files_var.set(encode_lit_cache(_files))

                remove_button.configure(command=on_remove)
                select_button.configure(command=lambda p=path: file_path_var.set(p))
            else:
                select_button.configure(bg=color['accent'])

            frame.pack(expand=True, fill='both', padx=4, pady=4)

    on_files_change()
    files_var.trace_add('write', on_files_change)
    file_path_var.trace_add('write', on_files_change)

    return parent
