from random import shuffle


def shuffle_list():
    arr = [i for i in range(5)]
    print(arr)
    shuffle(arr)
    print(arr)


def shuffle_string():
    s = "abcdefgh"
    li = list("abcdefgh")
    shuffle(li)
    result = ''.join(li)
    print("Shuffle string_character: {} -> {}".format(s, result))


shuffle_list()
shuffle_string()
