"""
    list1 = [10, 15, 20, 25, 30, 35, 40]
    list2 = [25, 40, 35]
    list_ = list1 - list2 = [10, 20, 30, 15]
"""


def using_list_comprehention(li1, li2):
    s = set(li2)
    print([x for x in li1 if x not in s])


def diff3(a, b):
    xa = [i for i in set(a) if i not in b]
    xb = [i for i in set(b) if i not in a]
    return xa + xb


def diff2(li1, li2):
    set(li1).difference(set(li2))


def using_symmetric_difference(li1, li2):
    set_dif = set(li1).symmetric_difference(set(li2))
    print(set_dif)


def using_set_constructor(li1, li2):
    print(set(li1) - set(li2))


def get_diff(li1: list, li2: list) -> list:
    return list(set(li1) ^ set(li2))


def diff1(list1, list2):
    c = set(list1).union(set(list2))  # or c = set(list1) | set(list2)
    d = set(list1).intersection(set(list2))  # or d = set(list1) & set(list2)
    return list(c - d)


l1 = [10, 15, 20, 25, 30, 35, 40]
l2 = [25, 40, 35]

# using_set_constructor(li1, li2)
# using_list_comprehention(li1, li2)
# using_symmetric_difference(li1, li2)

for v in set(l1) ^ set(l2):
    print(v)
