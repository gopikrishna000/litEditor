# logic for updating the file, importing it's content

def use_file_logic(file_path_string, markdown_string):
    file = None

    # file opening logic
    def on_file_selected(path):
        nonlocal file
        if file:
            file.close()

        if path == '':
            markdown_string.dispatch('')  # clear markdown_string
            return
        file = open(path, 'w')
        content = file.read()
        markdown_string.dispatch(content)

    # file updating logic todo: maybe with throttle
    def on_markdown_change(mdn_text):
        if file:
            file.write(mdn_text)

    file_path_string.observe(on_file_selected)
    markdown_string.observe(on_markdown_change)
