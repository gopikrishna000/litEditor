from tkinter import *

from src.logic import tabs


def get_side_nav(master, selected_tab):
    tab_frame = Frame(master, bg='#92C569')

    buttons = dict()
    last_selected_tab = selected_tab.value

    for index, key in enumerate(tabs):
        button = Button(tab_frame, height=2, width=10, text=key, bg='#92C569')
        button.grid(row=index, column=0, sticky=W)
        button.configure(command=lambda: selected_tab.dispatch(key))
        buttons.setdefault(key, button)

    def on_tab_selected(_key):
        nonlocal last_selected_tab

        _last_button = buttons.get(last_selected_tab)
        # remove selected look from this button

        _button = buttons.get(key)
        # update selected look for this button

        last_selected_tab = key

    selected_tab.observe(on_tab_selected)

    return tab_frame
