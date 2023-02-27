from os import listdir
from os.path import isfile, join
from os import walk
import glob


path = "D:/Dev/Projects/Github/python/python_core/"


def list_file_without_subdir():
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(onlyfiles)


def using_walk():
    for (dirpath, dirnames, filenames) in walk(path):
        for file in filenames:
            if file.endswith(".py"):
                print(file)


def using_glob1():
    print(glob.glob(path + "*"))


def using_glob2():
    txtfiles = []
    for file in glob.glob(path + "*.py"):
        txtfiles.append(file)
    print(txtfiles)



using_walk()
# using_glob1()
# using_glob2()
# list_file_without_subdir()
