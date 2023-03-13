import pathlib
from os import path


def api():
    p = 'C:/soft\\data/text.txt'
    print("abspath:", path.abspath(p))

    # Split the pathname path into a pair (root, ext) such that root + ext == path
    print("splitext:", path.splitext(p))
    print("suffix:", pathlib.Path('C:/soft\\data/text.txt').suffix)

    print("basename:", path.basename(p))
    print("commonprefix:", path.commonprefix(['/usr/lib', '/usr/local/lib']))
    print("commonpath:", path.commonpath(['/home/User/Desktop', '/home/User/Documents']))
    # Get the directory name from the specified path
    print("dirname:", path.dirname(p))
    print("expanduser:", path.expanduser("~/data.txt"))
    p2 = 'directory.py'
    # Return the size (bytes)
    print("getsize:", path.getsize(p2))
    print("isfile:", path.isfile(p2))
    print("isdir:", path.isdir(p2))
    print("join:", path.join('home', 'User', 'Downloads'))


api()
