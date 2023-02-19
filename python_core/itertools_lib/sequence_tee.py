import copy, itertools


def tee1():
    global a, b, c
    it = [1, 2, 3, 4]
    a, b = itertools.tee(it)
    c = copy.copy(a)
    print("a:", a, list(a))
    print("b:", b, list(b))
    print("c:", c, list(c))


def tee2():
    # global a, b, c
    a = [1, 2, 3, 4]
    b, c = itertools.tee(a)
    next(b)
    print("a:", a, list(a))
    print("b:", b, list(b))
    print("c:", c, list(c))


tee1()
# tee2()


