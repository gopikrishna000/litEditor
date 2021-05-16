import os


def file_from_project_root(file: str):
    script_dir = os.path.dirname(__file__)
    root = os.path.join(script_dir, '..\\..\\')
    return os.path.join(root, file)


def open_file(path):
    if not os.path.exists(path):
        with open(path, 'w'):
            pass
    return open(path, 'r+')
