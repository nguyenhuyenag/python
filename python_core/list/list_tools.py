from itertools.chain import from_iterable


def flaten_list():
    lst = [[1, 2], [3, 4], [5, 6]]
    lst = from_iterable(lst)
    print(list(lst))


flaten_list()
