import glob
from os import walk, listdir
from os.path import isfile, join


def list_file_without_subdir(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(onlyfiles)


def using_walk(path):
    for (dirpath, dirnames, filenames) in walk(path):
        for file in filenames:
            if file.endswith(".py"):
                print(file)


def using_glob1(path):
    print(glob.glob(path + "*"))


def using_glob2(path):
    txtfiles = []
    for file in glob.glob(path + "*.py"):
        txtfiles.append(file)
    print(txtfiles)


if __name__ == '__main__':
    path = r"/path_file"
    using_walk(path)
    # using_glob1()
    # using_glob2()
    # list_file_without_subdir()
