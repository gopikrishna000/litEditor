# entry point to the program
import ctypes
from tkinter import Tk

from src import lit_editor

ctypes.windll.shcore.SetProcessDpiAwareness(1)

window = Tk()

window.title('litEditor')
window.minsize('720', '480')
# window.tk.call('tk', 'scaling', 2.0)

editor = lit_editor(window)
editor.pack(expand=True, fill='both')

window.mainloop()
