import os
# file = Path(__file__).with_name('data.txt')
"""
Open parameters
    'r'  -   Open a file for reading (default)
    'a'  -   Append, will append to the end of the file
    'w'  -   Write, will overwrite any existing content
    'x'  -   Create, will create a file, returns an error if the file exist

    't'  -   Open in text mode. (default)
    'b'  -   Open in binary mode.
    '+'  -   Open a file for updating (reading and writing)
"""


def to_read():
    with open("data-file.txt") as f:
        for line in f:
            print(line)


def to_write():
    with open("data-file.txt", "w") as f:
        for i in range(10):
            f.write("Content %d\n" % i)


def to_delete():
    if os.path.exists("data-file.txt"):
        os.remove("data-file.txt")
    else:
        print("The file doesn't exist")


def delete_dir():
    os.rmdir("my_folder")


# to_write()
to_read()
# to_delete()
