# entry point to the program
from tkinter import Tk

from src import lit_editor

window = Tk()

window.title('litEditor')
window.minsize('720', '480')

editor = lit_editor(window)
editor.pack(expand=True, fill='both')

window.mainloop()
