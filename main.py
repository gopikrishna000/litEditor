# Sample code for some features by @azilefz

from tkinter import *
from tkinter import filedialog, colorchooser, ttk,messagebox
from PIL import Image,ImageTk
from tkinter import simpledialog
import os

window = Tk()
window.geometry("800x750")
window.title("Nameless for now")

# Icon for the window
photo = ImageTk.PhotoImage(Image.open('images/notepad.png'))
window.iconphoto(False,photo)

window.minsize(800,750)

current_file_name = ""


def Copy_Text():
    window.clipboard_clear()
    Text.clipboard_append(string=Text.selection_get())

def Cut_Text():
    Copy_Text()
    Text.delete(index1=SEL_FIRST,index2=SEL_LAST)

def Paste_Text():
    Text.insert(INSERT,window.clipboard_get())

def Delete_Text():
    Text.delete(index1=SEL_FIRST,index2=SEL_LAST)

def Undo_Action():
    Text.edit_undo()

def Redo_Action():
    Text.edit_redo()

def Select_All():
    Text.tag_add(SEL,1.0,END)

def Delete_All():
    Text.delete(1.0,END)

Text.bind('<Control-X>', Cut_Text())
Text.bind('<Control-x>', Cut_Text())

Text.bind('<Control-C>', Copy_Text())
Text.bind('<Control-c>', Copy_Text())

Text.bind('<Control-V>', Paste_Text())
Text.bind('<Control-v>', Paste_Text())

Text.bind('<Control-z>', Undo_Action())
Text.bind('<Control-Z>', Undo_Action())

Text.bind('<Control-y>', Redo_Action())
Text.bind('<Control-Y>', Redo_Action())

def new_file():
    global current_file_name
    current_file_name = ""
    x = messagebox.askquestion(title='Save File', message="Save the File?")
    if x is None:
        save_file()
    Delete_All()

def Save_File():
    global current_file_name
    if current_file_name == "":
        path = filedialog.asksaveasfile()
        current_file_name = path
    window.title(current_file_name)
    file = open(current_file_name,mode='w')
    file.write(Text.get(1.0, END))

def Save_As_File():
    # havent saved it once
    if current_file_name == "":
        Save_File()
        return "break"
    file = filedialog.asksaveasfile(mode='w')
    # Do nothing
    if file is None:
        return ''
    data = str(Text.get(1.0, END))
    file.write(data)
    file.close()

def Open_Any_File():
    global current_file_name
    new_file()
    f = filedialog.askopenfile()
    # f.name is the path or directory of the file
    current_file_name = f.name
    Text.insert(INSERT, file.read())

def Exit_Window():
    Save_File()
    window.quit()

Text.bind('<Control-n>', new_file())
Text.bind('<Control-N>', new_file())

Text.bind('<Control-s>', Save_File())
Text.bind('<Control-S>', Save_File())

Text.bind('<Control-o>', Open_Any_File())
Text.bind('<Control-O>', Open_Any_File())

Text.bind('<Control-Shift-s>', Save_As_File())
Text.bind('<Control-Shift-S>', Save_As_File())

# Renaming the File
new_file_name = ""

def Rename_Me():
    global current_file_name
    # Empty means no file opened
    if current_file_name == "":
        Open_Any_File()

    parts = current_file_name.split('/')
    edited_path = ""
    for i in range(0, len(parts)-1):
        edited_path += parts[i] + '/'

    new_file_name = simpledialog.askstring(title="Renaming File",prompt="Enter New Name for the file:")
    new_file_name = str(edited_path) + str(new_file_name)
    os.rename(current_file_name,new_file_name)
    window.title(new_file_name)

Text.bind('<Control-R>', Rename_Me())
Text.bind('<Control-r>', Rename_Me())