import numpy as np
from PIL import Image


def decode_lit_cache(data: str):
    return [path for path in data.split('\n') if path != '']


def encode_lit_cache(file_paths: list):
    return '\n'.join(file_paths)


def generate_colored_icon(icon, _color):
    pixels = np.array(icon)
    non_alpha = (pixels.T[3] != 0)
    rgb = hex_to_rgb(_color)
    pixels[..., :-1][non_alpha.T] = rgb  # Transpose back needed

    return Image.fromarray(pixels)


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
