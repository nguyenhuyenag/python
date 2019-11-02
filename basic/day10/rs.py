import os


def getPath():
    realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)
    return dirname


def toNumber(arr):
    for i in range(len(arr)):
        arr[i] = eval(arr[i])
    return arr


def matrix(row, col):
    arr = []
    for i in range(row):
        arr.append(col * [0])
    return arr


def printMatrix(arr):
    print()
    for i in range(len(arr)):
        print(arr[i])
