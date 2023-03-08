import numpy as np


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


def split4(alist, chunk_size):
    my_list2 = [alist[i:i + chunk_size] for i in range(0, len(alist), chunk_size)]
    print(my_list2)


# def split5(alist, sub_list):
#     my_list2 = [alist[i::n] for i in range(sub_list)]
#     print(my_list2)

def split5(alist, sub_list):
    splitted = []
    for i in reversed(range(1, sub_list + 1)):
        split_point = len(alist) // i
        splitted.append(alist[:split_point])
        alist = alist[split_point:]
    print(splitted)


n = 3
arr = [1, 2, 3, 4, 5, 6, 7, 8]

# split1(arr, n)
# split2(arr, n)
# split3(arr, n)
# split4(arr, n)
split5(arr, n)
