def write_bytes_to_file():
    filename = None
    filebytes = None
    with open(filename, 'wb') as f:
        f.write(filebytes)


def read_file_into_list():
    file_contents = [line.strip() for line in open("data-file.txt", "r")]
    print(file_contents)


def read_file_to_string(path_file: str) -> str:
    # contents = ""
    # try:
    #     with closing(open(path_file)) as file_contents:
    #         for line in file_contents:
    #             contents += line
    # except FileNotFoundError as e:
    #     traceback.print_exc(limit=1)
    # return contents
    byte_array = read_file_to_bytes(path_file)
    return str(byte_array, 'utf-8')  # Or -> byte_array.decode('utf-8')


def read_file_to_bytes(path_file: str) -> bytearray:
    with open(path_file, 'rb') as file_content:
        f = file_content.read()
        return bytearray(f)


if __name__ == '__main__':
    file = "data.txt"
    data = read_file_to_bytes(file)
    # data = read_file_to_string(file)
    # print(data)
