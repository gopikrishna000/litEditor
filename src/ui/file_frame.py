from tkinter import Frame, Button, filedialog, StringVar, FLAT

from PIL.ImageTk import PhotoImage

from src.logic import use_recent_files_logic
from src.styles.theme import color
from src.ui.recent_files_frame import get_recent_files_frame
from src.utils import open_icon, generate_colored_icon

valid_file_types = (
    ("Github Markdown File", "*.md"),
    ("Text File", "*.txt")
)


def get_file_frame(master, file_path_var: StringVar):
    # colors
    bg = color['surface-dark']
    fg = color['high']

    files_var = StringVar()

    parent = Frame(master, bg=bg)

    recent_files_frame = get_recent_files_frame(parent, file_path_var, files_var, bg)

    recent_files_frame.pack(expand=True)

    add_to_recent = use_recent_files_logic(files_var)

    def on_browse_btn():
        file_path = filedialog.askopenfilename(filetypes=valid_file_types)
        add_to_recent(file_path)
        file_path_var.set(file_path)

    def on_create_btn():
        file_path = filedialog.asksaveasfilename(filetypes=valid_file_types)
        add_to_recent(file_path)
        file_path_var.set(file_path)

    control_frame = Frame(parent, bg=bg)

    file_icon = PhotoImage(generate_colored_icon(open_icon('file_tab', (24, 24)), '#FFFFFF'))
    add_icon = PhotoImage(generate_colored_icon(open_icon('add_icon', (24, 24)), '#FFFFFF'))

    browse_btn = Button(control_frame, text='Open File', bg=color['accent'], fg=fg, relief=FLAT, image=file_icon,
                        compound='left')
    browse_btn.image = file_icon

    create_btn = Button(control_frame, text='Create File', bg=color['accent'], fg=fg, relief=FLAT, image=add_icon,
                        compound='left')
    create_btn.image = add_icon
    browse_btn.pack(expand=True, fill='both', side='left', padx=16, pady=16)
    create_btn.pack(expand=True, fill='both', side='left', padx=16, pady=16)
    control_frame.pack()

    browse_btn.configure(command=on_browse_btn)
    create_btn.configure(command=on_create_btn)

    return parent
