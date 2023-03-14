import os
from pathlib import Path

from path_directory.directory import get_parent


def write_bytes_to_file(filepath, filebytes):
    parent = get_parent(filepath)
    if not os.path.exists(parent):
        os.mkdir(parent)
    with open(filepath, 'wb') as f:
        f.write(filebytes)
    return filepath


def read_file_to_string(path_file: str) -> str:
    byte_array = read_file_to_bytes(path_file)
    return str(byte_array, 'utf-8')  # Or -> byte_array.decode('utf-8')


def read_file_to_bytes(path_file: str) -> bytearray:
    with open(path_file, 'rb') as file_content:
        f = file_content.read()
        return bytearray(f)


def read_file_into_list(_file):
    return [line.strip() for line in open(_file, "r")]


def rename(path_file):
    # os.rename(old_name, new_name)
    f = Path(path_file)
    new_name = f"{f.stem}_new{f.suffix}"
    f.rename(new_name)


if __name__ == '__main__':
    # file = "data.txt"
    # data = read_file_to_bytes(path_file)
    # data = read_file_to_string(path_file)
    # data = read_file_into_list(file)
    # print(data)

    myfile = r'C:\Users\huyennv\Desktop\test\test1.txt'
    rename(myfile)
