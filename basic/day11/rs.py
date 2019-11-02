import os


def getPath():
    realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)
    return dirname
