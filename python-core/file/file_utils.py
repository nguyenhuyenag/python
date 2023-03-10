import traceback
from contextlib import closing


def read_file_into_list():
    file_contents = [line.strip() for line in open("data-file.txt", "r")]
    print(file_contents)


def read_file_to_string(path_file: str) -> str:
    contents = ""
    try:
        with closing(open(path_file)) as file_contents:
            for line in file_contents:
                contents += line
    except FileNotFoundError as e:
        traceback.print_exc(limit=1)
    return contents


def read_file_to_bytes(path_file: str) -> bytes:
    contents = read_file_to_string(path_file)
    return bytes(contents.encode('utf-8'))


if __name__ == '__main__':
    file = "data.txt"
    data = read_file_to_bytes(file)
    print(data)
