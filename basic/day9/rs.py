import os
import rs


def getPath():
    realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)
    return dirname


def toNumber(a):
    for i in range(len(a)):
        a[i] = eval(a[i])
    return a


def matrix(r, c):
    arr = []
    for i in range(r):
        arr.append(c * [0])
    return arr


def createData():
    f = open(getPath() + "/file/data.txt", "r")
    arr = matrix(3, 5)
    for line in f:
        a = toNumber(line.rstrip().split(","))
        arr[a[0]-1][a[1]-1] = a[2]
    f.close()
    return arr


def printMatrix(arr):
    print()
    for i in range(len(arr)):
        print(arr[i])
