import ast, heapq
from itertools import chain


def flaten_list():
    lst = [[1, 2], [3, 4], [5, 6]]
    lst = chain.from_iterable(lst)
    print(list(lst))


def heapq_lib():
    arr = [1, 4, 0, 2, 3, 4, 5, 6]
    # Lấy ra n số nhỏ nhất
    print("nsmallest: ", heapq.nsmallest(2, arr))
    # Lấy ra n số lớn nhất
    print("nlargest: ", heapq.nlargest(3, arr))


def stringlist_to_list():
    arr = "[1,2,3]"
    print(type(arr))
    arr = ast.literal_eval(arr)
    print(type(arr))


# heapq_lib()
# flaten_list()
stringlist_to_list()