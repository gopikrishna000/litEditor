#from src.utils import Lifecycle
from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter.constants import NO
from PIL import Image,ImageTk
  
    

def get_side_nav(master,selected_tab,tabs):

    buttondict = dict.fromkeys(tabs,None)
    
    tab_frame=Frame(master,bg='#92C569')  
    i=0
    for name in tabs:
        buttondict[name]=Button(tab_frame,height=2,width=10,text=name,bg='#92C569')
        buttondict[name].grid(row=i,column=0,sticky=W) 
        i=i+1

    funcdict ={'new.png':create_file,'folder.jpg':select_folder,'edit.png':edit_markdown,'lit.jpg':lit,'preview.png':preview,'setting.jpg':setting,'exit.png':exit}
    
    
    for name in buttondict:
            buttondict[name].configure(command=funcdict[name])

    return tab_frame    



def select_folder():
    pass
def create_file():
    pass
def edit_markdown():
    pass
def lit():
    pass
def preview():
    pass
def setting():
    pass
def exit():
    pass

'''
tk=Tk()
tabs=['new.png','folder.jpg','edit.png','lit.jpg','preview.png','setting.jpg','exit.png']
tab_frame=get_side_nav(tk,tabs)
tab_frame.pack(fill='y',side='left',ipadx=0,ipady=0)
tk.mainloop()
'''