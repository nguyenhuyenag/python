import numpy as np


# Chia list_type thành n list_type con
def split1(alist, sub_list):
    my_list2 = np.array_split(alist, sub_list)
    my_list2 = [v.tolist() for v in my_list2]
    print(my_list2)


def split2(alist, sub_list=1):
    length = len(alist)
    my_list2 = [alist[i * (length // sub_list):(length * (i + 1)) // sub_list] for i in range(sub_list)]
    print(my_list2)


def split3(alist, sub_list):
    k, m = divmod(len(alist), sub_list)
    my_list2 = [alist[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(sub_list)]
    print(my_list2)


def split4(alist, sub_list):
    result = []
    for i in reversed(range(1, sub_list + 1)):
        split_point = len(alist) // i
        result.append(alist[:split_point])
        alist = alist[split_point:]
    print(result)


# Chia list_type thành list_type con có kích thước <= chunk_size <= len(alist)
def split_by_size(alist, chunk_size):
    my_list2 = [alist[i:i + chunk_size] for i in range(0, len(alist), chunk_size)]
    print(my_list2)


if __name__ == '__main__':
    n = 6
    arr = [i for i in range(1, 4 + 1)]
    print(arr)
    print(f"{n} sub list")
    # split1(arr, n)
    # split2(arr, n)
    split3(arr, n)
    # split4(arr, n)
    # split_by_size(arr, n)
