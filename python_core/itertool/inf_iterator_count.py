import time
from itertools import count


def func_count():
    iterator = count(start=3, step=3)
    print("Even list:", list(next(iterator) for _ in range(5)))


# count(10) --> 10 11 12 13 14 ...
# count(2.5, 0.5) --> 2.5 3.0 3.5 ...
def func_count1():
    # for i in count():
    # for i in count(step=2):
    for i in count(start=2, step=2):
        print(i, end=" ")
        time.sleep(1)
        if i > 4:
            break


def func_count2():
    for i in count(10, -1):
        print(i, end=" ")  # 10, 9, 8, 7
        if i < 8:
            break


def func_count3():
    for i in count(0.1, 1.5):
        print(i, end=", ")
        if i > 3:
            break


def func_count4():
    l1 = ['a', 'b', 'c']
    l2 = ['x', 'y', 'z']
    # [(0, 'a', 'x'), (1, 'b', 'y'), (2, 'c', 'z')]
    for i, v1, v2 in zip(count(), l1, l2):
        print(1, v1, v2)


func_count()
# func_count1()
# func_count2()
# func_count3()
# func_count4()
