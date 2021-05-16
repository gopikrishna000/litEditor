from tkinter import Frame, Label, Button, filedialog, StringVar, Listbox, END

valid_file_types = (
    ("Github Markdown File", "*.(markdown|mdown|mkdn|md|mkd)"),
    ("Elements Markdown File", "*.(markdown|mdown|mdwn|md)"),
    ("Vim Markdown File", "*.(markdown|mdown|mkdn|mdwn|md|mkd)"),
    ("BitBucket Markdown File", "*.(markdown|mdown|mkdn|md|mkd|text)"),
    ("R Studio Markdown File", "*.Rmd"),
    ("Text File", "*.txt")
)

recent_file = open('src/rcsave.txt', 'r+')


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

    test_frame = Frame(parent)
    test_label = Label(test_frame, text='Recently Opened Files', font=('arial', 12))
    recent_drop = Listbox(test_frame, height=5, width=50, font=('arial', 10))

    test_label.pack(fill='x', padx=4, pady=4)
    recent_drop.pack(expand=True, side='right', padx=4, pady=4)
    test_frame.pack()

    def on_browse_btn():
        file_path = filedialog.askopenfilename(filetypes=valid_file_types)
        file_path_var.set(file_path)
        update_recent_drop(file_path_var.get())

    def on_create_btn():
        file_path = filedialog.asksaveasfilename(filetypes=valid_file_types)
        #   todo: verify file extension
        file_path_var.set(file_path)
        update_recent_drop(file_path_var.get())

    def update_recent_drop(x):
        for i, ele in enumerate(recent_drop.get(0, END)):
            if ele == x + "\n":
                recent_drop.delete(i)
        recent_drop.insert(0, x + "\n")
        if (x + "\n") not in recent_file.readlines():
            recent_file.write(x + "\n")

    def retain_recent_drop():
        path = recent_file.readlines()
        for i, ele in enumerate(path):
            recent_drop.insert(i, ele)

    retain_recent_drop()

    browse_btn.configure(command=on_browse_btn)
    create_btn.configure(command=on_create_btn)

    return parent
