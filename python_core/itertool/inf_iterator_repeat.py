from time import sleep
from itertools import repeat


def repeat_value():
    for v in repeat(5):
        print(v, end=" ")
        sleep(1)

def repeat_two():
    for v1, v2 in repeat([1, 2]):
        print("{}, {}".format(v1, v2))
        sleep(1)


def repeat_times():
    for v in repeat("Python", 7):  # repeat 7 lần
        print(v, end=" ")
        sleep(1)


# repeat_one()
repeat_two()
# repeat_times()
