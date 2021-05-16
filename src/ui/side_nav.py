from tkinter import StringVar, Frame, FLAT, W

from src.logic import tabs
from src.styles.theme import color
from src.ui.tab_button import TabButton


def get_side_nav(master, selected_tab: StringVar):
    tab_frame = Frame(master, bg=color['surface'])

    buttons = dict()
    last_selected_tab = selected_tab.get()

    for index, key in list(enumerate(tabs)):
        button = TabButton(tab_frame, image=key)

        button.grid(row=index, column=0, sticky=W, ipadx=16, ipady=16)
        button.configure(command=lambda k=key: selected_tab.set(k), relief=FLAT, bg=color['surface'])

        buttons.setdefault(key, button)

    def on_tab_selected(*_):
        nonlocal last_selected_tab
        _key = selected_tab.get()

        # get buttons
        _last_button = buttons.get(last_selected_tab)
        _button = buttons.get(_key)

        # remove selected look from this button
        _last_button.anim.animate_to(0)
        _last_button.configure(relief=FLAT, bg=color['surface'])

        # update selected look for this button
        _button.configure(bg=color['surface-dark'])
        _button.anim.animate_to(1)

        last_selected_tab = _key

    on_tab_selected()
    selected_tab.trace_add('write', on_tab_selected)

    return tab_frame
