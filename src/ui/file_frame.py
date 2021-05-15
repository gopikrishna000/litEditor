from tkinter import Frame, Label, Button, filedialog, StringVar

valid_file_types = (
    ("Github Markdown File", "*.(markdown|mdown|mkdn|md|mkd)"),
    ("Elements Markdown File", "*.(markdown|mdown|mdwn|md)"),
    ("Vim Markdown File", "*.(markdown|mdown|mkdn|mdwn|md|mkd)"),
    ("BitBucket Markdown File", "*.(markdown|mdown|mkdn|md|mkd|text)"),
    ("R Studio Markdown File", "*.Rmd"),
    ("Text File", "*.txt")
)


def get_file_frame(master, file_path_var: StringVar):
    # ui declaration

    parent = Frame(master)

    heading_label = Label(parent, text='Currently Editing', font=('arial', 12))
    path_label = Label(parent, textvariable=file_path_var)

    control_frame = Frame(parent)

    browse_btn = Button(control_frame, text='Browse')
    create_btn = Button(control_frame, text='Create')

    heading_label.pack(fill='x', pady=(4, 4))
    path_label.pack(fill='x', pady=(4, 4))

    browse_btn.pack(expand=True, fill='x', side='left', padx=4, pady=4)
    create_btn.pack(expand=True, fill='x', side='left', padx=4, pady=4)
    control_frame.pack()

    def on_browse_btn():
        file_path = filedialog.askopenfilename(filetypes=valid_file_types)
        file_path.set(file_path)

    def on_create_btn():
        file_path = filedialog.asksaveasfilename(filetypes=valid_file_types)
        #   todo: verify file extension
        file_path.set(file_path)

    browse_btn.configure(command=on_browse_btn)
    create_btn.configure(command=on_create_btn)

    return parent
