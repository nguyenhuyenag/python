import ast, heapq
from itertools import chain
from operator import countOf
from collections import Counter


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


# Count items
# Xem thêm counter_sample.py
def count_by_counter():
    source_list = [1, 0, 3, 4, 3, 8, 3]
    print("Count:", source_list.count(3))
    print("CountOf:", countOf(source_list, 3))
    print("Counter:", Counter(source_list))


# heapq_lib()
# flaten_list()
# stringlist_to_list()
count_by_counter()
