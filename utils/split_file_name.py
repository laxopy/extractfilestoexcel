from pathlib import Path


def split_file_name(file_name):
    path = Path(file_name)
    file_folder = path.parents[0]
    file_name = path.stem
    file_suffix = path.suffix
    return file_folder, file_name, file_suffix
