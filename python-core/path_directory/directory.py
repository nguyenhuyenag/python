import pathlib
from os import path
import os, ntpath, posixpath, shutil
from pathlib import Path, PurePosixPath, PureWindowsPath


def get_parent(your_path):
    from_path = Path(your_path)
    return from_path.parent.absolute()


def get_current_path_file():
    path_of_file = pathlib.Path(__file__)
    print(path_of_file)


# Get Current Directory in Python
def get_current_dir():
    d = path.dirname(path.dirname(__file__))
    print("Project Directory:", d)
    print(Path.cwd())
    print(os.getcwd())
    # d = dirname(dirname(abspath(__file__)))
    # print("Abspath: ", d)
    # ROOT_DIR = os.path.abspath(os.curdir)
    # print("ROOT_DIR: ", ROOT_DIR)


def create_folder():
    os.mkdir('test')


def rename_folder():
    if os.path.isdir('test') and not os.path.isdir('new_one'):
        os.rename('test', 'new_one')
        print("Done")
    else:
        print("Fail")


def delete_empty_folder():
    if os.path.isdir('new_one'):
        os.rmdir("new_one")


def delete_any_folder():
    if os.path.isdir('new_one'):
        shutil.rmtree("new_one")


def join_path():
    rel_path = r"2091\data.txt"
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, rel_path)

    print("Unix -> ", abs_file_path.replace(os.sep, posixpath.sep))
    print("Windows -> ", abs_file_path.replace(os.sep, ntpath.sep))


def fixpath():
    # Windows -> Posix
    win = r'foo\bar\file.txt'
    posix = str(PurePosixPath(PureWindowsPath(win)))
    print(posix)  # foo/bar/file.txt

    # Posix -> Windows
    posix = 'foo/bar/file.txt'
    win = str(PureWindowsPath(PurePosixPath(posix)))
    print(win)  # foo\bar\file.txt


# get_current_path_file()
# get_current_dir()
# create_folder()
# rename_folder()
# delete_empty_folder()
# delete_any_folder()
# join_path()
# fixpath()
# get_parent()
