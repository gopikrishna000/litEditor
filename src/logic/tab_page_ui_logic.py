from src.utils import Observable

tabs = ['file_tab', 'md_edit_tab', 'fire_tab', 'md_preview_tab']


def use_tab_page_ui_logic(selected_tab: Observable, pages: list):
    # change ui according to selected_tab
    def on_tab_selected(tab):
        for page in pages:
            page.pack_forget()

        selected_tab_index = tabs.index(tab)

        pages[selected_tab_index].pack()

    selected_tab.observe(on_tab_selected)
