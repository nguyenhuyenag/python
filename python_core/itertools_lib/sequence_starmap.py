from itertools import starmap

li = [(2, 3), (3, 1), (4, 6), (5, 3), (6, 2), (7, 2)]


def default_method():
    new_li = list(starmap(pow, li))
    for x, y in zip(li, new_li):
        print("{}^{} = {}".format(x[0], x[1], y))


# (lambda x, y, z: x + y + z, arr)
def with_lambda():
    new_li = list(starmap(lambda x, y: x + y, li))
    for x, y in zip(li, new_li):
        print("{} + {} = {}".format(x[0], x[1], y))


# default_method()
with_lambda()
