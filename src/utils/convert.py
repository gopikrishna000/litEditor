def decode_lit_cache(data: str):
    return [path for path in data.split('\n') if path != '']


def encode_lit_cache(file_paths: list):
    return '\n'.join(file_paths)
