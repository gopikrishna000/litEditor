from tkinter import StringVar

tabs = ['file_tab.png', 'md_edit_tab.png', 'fire_tab.png', 'md_preview_tab.png']


def use_tab_page_ui_logic(selected_tab_var: StringVar, pages: list):
    # change ui according to selected_tab
    def on_tab_selected(*_):
        for page in pages:
            page.pack_forget()

        tab = selected_tab_var.get()
        selected_tab_index = tabs.index(tab)

        pages[selected_tab_index].pack(expand=True, fill='both')

    on_tab_selected()
    selected_tab_var.trace_add('write', on_tab_selected)
