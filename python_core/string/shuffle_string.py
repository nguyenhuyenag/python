from random import shuffle
# import string_utils
# print string_utils.shuffle("random_string")

def shuffle_string():
    s = "shuffle_this_string"
    print(s)
    l = list(s)
    shuffle(l)
    result = ''.join(l)
    print(result)


shuffle_string()
