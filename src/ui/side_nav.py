from tkinter import *

from src.logic import tabs


def get_side_nav(master, selected_tab: StringVar):
    tab_frame = Frame(master, bg='#92C569')

    buttons = dict()
    last_selected_tab = selected_tab.get()

    for index, key in list(enumerate(tabs)):
        button = Button(tab_frame, height=2, width=10, text=key, bg='#92C569',relief=FLAT)
        button.grid(row=index, column=0, sticky=W)
        buttons.setdefault(key, button)
        button.configure(command=lambda k=key: selected_tab.set(k))

    def on_tab_selected(*_):
        nonlocal last_selected_tab
        _key = selected_tab.get()

        _last_button = buttons.get(last_selected_tab)
        # remove selected look from this button
        _last_button.configure(relief=FLAT)
        _button = buttons.get(_key)
        # update selected look for this button
        _button.configure(relief=SUNKEN)
        print(_key)
        last_selected_tab = _key

        last_selected_tab = key

    selected_tab.trace_add('write', on_tab_selected)

    return tab_frame
