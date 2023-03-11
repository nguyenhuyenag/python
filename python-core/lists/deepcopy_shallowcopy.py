import copy as cp


def method_name():
    arr = [1, 2, 3, 4, 5, 6]
    shallow_copy = cp.copy(arr)
    deep_copy = cp.deepcopy(arr)
    print("id=", id(arr))
    print("id=", id(shallow_copy))
    print("id=", id(deep_copy))

def method():
    a = [1, 2, 3]

    b = a[:]
    # or:
    # b = a.copy()
    # b = lists(a)
    # b = cp.copy(a)

    b.append(4)

    print(b)  # [1, 2, 3, 4]
    print(a)  # [1, 2, 3]


# method_name()
method()