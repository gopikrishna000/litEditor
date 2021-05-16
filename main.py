# entry point to the program
import ctypes
from tkinter import Tk

from src import lit_editor

ctypes.windll.shcore.SetProcessDpiAwareness(1)

window = Tk()

window.title('litEditor')
window.minsize('1280', '720')
editor = lit_editor(window)
editor.pack(expand=True, fill='both')

window.mainloop()
