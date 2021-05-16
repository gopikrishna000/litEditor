import os

from PIL import Image


def file_from_project_root(file: str):
    script_dir = os.path.dirname(__file__)
    root = os.path.join(script_dir, '..\\..\\')
    return os.path.join(root, file)


def open_file(path):
    if not os.path.exists(path):
        with open(path, 'w'):
            pass
    return open(path, 'r+')


def open_icon(icon_name, size=(32, 32)):
    script_dir = os.path.dirname(__file__)
    rel_path = "../../assets/" + icon_name + ".png"
    abs_file_path = os.path.join(script_dir, rel_path)
    return Image.open(abs_file_path).resize(size).convert('RGBA')
