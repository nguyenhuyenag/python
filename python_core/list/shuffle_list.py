from random import shuffle


def shuffle_list():
    arr = [i for i in range(10)]
    print(arr)
    shuffle(arr)
    print(arr)


def shuffle_string():
    s = "abcdefgh"
    print(s)
    l = list("abcdefgh")
    shuffle(l)
    result = ''.join(l)
    print(result)


# shuffle_list()
shuffle_string()
