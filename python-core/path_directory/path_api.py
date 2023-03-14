import os
import pathlib
from os import path

"""
            path                             head                       tail
    '/home/user/Desktop/file.txt'       '/home/user/Desktop/'       'file.txt'
    '/home/user/Desktop/'               '/home/user/Desktop/'       {empty}
    'file.txt'                          {empty}                     'file.txt'
"""
def split():
    # path
    p = '/home/User/Desktop/file.txt'
    # Split the path in
    # head and tail pair
    head_tail = os.path.split(p)
    # print head and tail of the specified path
    print("Head of '% s:'" % p, head_tail[0])
    print("Tail of '% s:'" % p, head_tail[1], "\n")


def path_api():
    p = 'C:/soft\\data/text.txt'
    print("abspath:", path.abspath(p))

    # Split the pathname path into a pair (root, ext) such that root + ext == path
    # root, ext = path.splitext(p)
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

    # On Windows, any forward slash (‘/’) in the path is converted to backslash (‘\’)
    print("normpath:", path.normpath('/home\\user/temp/../Documents'))
    print("realpath:", path.realpath('path_api.py'))


# path_api()
split()
