from tkinter import StringVar, Frame, FLAT, W, SUNKEN

from src.logic import tabs
from src.ui.tab_button import TabButton


def get_side_nav(master, selected_tab: StringVar):
    tab_frame = Frame(master, bg='#92C569')
    buttons = dict()
    last_selected_tab = selected_tab.get()

    for index, key in list(enumerate(tabs)):
        button = TabButton(tab_frame, image=key)
        button.grid(row=index, column=0, sticky=W, ipadx=8, ipady=8)
        buttons.setdefault(key, button)
        button.configure(command=lambda k=key: selected_tab.set(k), relief=FLAT)

    def on_tab_selected(*_):
        nonlocal last_selected_tab
        _key = selected_tab.get()

        _last_button = buttons.get(last_selected_tab)
        # remove selected look from this button
        _last_button.anim.animate_to(0)
        _last_button.configure(relief=FLAT)
        _button = buttons.get(_key)
        # update selected look for this button
        _button.configure(relief=SUNKEN)
        _button.anim.animate_to(1)
        last_selected_tab = _key

    on_tab_selected()
    selected_tab.trace_add('write', on_tab_selected)

    return tab_frame
