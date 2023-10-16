from random import shuffle


def shuffle_string():
    s = "character_string"
    l = list(s)
    shuffle(l)
    result = ''.join(l)
    print("Before:", s)
    print("After: ", result)


shuffle_string()
