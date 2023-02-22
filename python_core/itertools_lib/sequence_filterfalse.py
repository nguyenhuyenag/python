from itertools import filterfalse


def filter_false(y):
    return y > 5


li = [2, 4, 5, 7, 8, 10, 20]

print(list(filterfalse(filter_false, li)))

print("Not even numers: ", list(filterfalse(lambda x: x % 2 == 0, li)))
