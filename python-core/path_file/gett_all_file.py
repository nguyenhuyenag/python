import glob
from os import walk, listdir
from os.path import isfile, join


def list_file_without_subdir(p):
    onlyfiles = [f for f in listdir(p) if isfile(join(p, f))]
    print(onlyfiles)


def using_walk(p):
    for (dirpath, dirnames, filenames) in walk(p):
        for file in filenames:
            if file.endswith(".py"):
                print(file)


def using_glob1(p):
    print(glob.glob(p + "*"))


def using_glob2(path):
    txtfiles = []
    for file in glob.glob(path + "*.py"):
        txtfiles.append(file)
    print(txtfiles)


if __name__ == '__main__':
    p = r"/path_file"
    using_walk(p)
    # using_glob1()
    # using_glob2()
    # list_file_without_subdir()
