import os
from importlib.resources import path
from pathlib import Path
from path_directory.directory import get_parent

"""
    Ghi nội dung dạng byte array vào file
"""
def write_bytes_to_file(path_file, byte_array):
    parent = get_parent(path_file)
    if not os.path.exists(parent):
        os.mkdir(parent)
    with open(path_file, 'wb') as f:
        f.write(byte_array)
    return path_file


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


def file_todo(pfile):
    with open(pfile) as file:
        for line in file:
            print(line.rstrip() + ",")


if __name__ == '__main__':
    _path_file = r"file\data.txt"
    # data = read_file_to_bytes(path_file)
    # data = read_file_to_string(path_file)
    # data = read_file_into_list(file)
    file_todo(_path_file)

    # myfile = r'C:\Users\huyennv\Desktop\test\test1.txt'
    # rename(myfile)

    # print(data)
