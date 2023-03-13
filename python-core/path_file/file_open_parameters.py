import os
# path_file = Path(__file__).with_name('data.txt')
"""
Open parameters
    'r'  -   Open a path_file for reading (default)
    'a'  -   Append, will append to the end of the path_file
    'w'  -   Write, will overwrite any existing content
    'x'  -   Create, will create a path_file, returns an error if the path_file exist

    't'  -   Open in text mode (default)
    'b'  -   Open in binary mode
    '+'  -   Open a path_file for updating (reading and writing)
"""


def to_read():
    with open("data-path_file.txt") as f:
        for line in f:
            print(line)


def to_write():
    with open("data-path_file.txt", "w") as f:
        for i in range(10):
            f.write("Content %d\n" % i)


def to_delete():
    if os.path.exists("data-path_file.txt"):
        os.remove("data-path_file.txt")
    else:
        print("The path_file doesn't exist")


def delete_dir():
    os.rmdir("my_folder")


# to_write()
to_read()
# to_delete()
