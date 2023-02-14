from itertools import cycle
import time


def cycle_array():
    arr = [1, 3, 9, -5, 4]
    count_cycle = 0;
    for v in cycle(arr):
        print(v, end=" ")
        time.sleep(1)


def cyc_string():
    for v in cycle("ABCD"):
        print(v, end=" ")
        time.sleep(1)


def cyc_range():
    count_cycle = 0;
    for v in cycle(range(5)):
        print(v, end=" ")
        time.sleep(1)


def cycle_zip():
    for (v1, v2) in cycle(zip([1, 2, 3, 4], "ABCD")):
        print("({}, {}),".format(v1, v2), end=" ")
        time.sleep(1)


# cycle_array()
# cyc_string()
# cyc_range()
cycle_zip()
