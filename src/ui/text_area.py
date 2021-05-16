from tkinter import Text, END


def get_text_area(master, **kwargs):
    try:
        text_variable = kwargs.pop("textvariable")
    except KeyError:
        text_variable = None

    widget = Text(master, **kwargs)

    def on_widget_change(event=None):
        widget.edit_modified(0)

        md_text = text_variable.get()
        val = widget.get("1.0", 'end-1c')

        if md_text != val:
            text_variable.set(val)

    if text_variable:
        widget.bind("<<Modified>>", on_widget_change)

    def on_md_change(*_):
        md_text = text_variable.get()
        val = widget.get("1.0", 'end-1c')
        if md_text != val:
            widget.delete("1.0", END)
            widget.insert("1.0", md_text)

    if text_variable:
        on_md_change()
        text_variable.trace_add('write', on_md_change)

    return widget
