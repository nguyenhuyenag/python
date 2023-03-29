import random
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


def random_using_index():
    arr = [1, 4, 2, 7, 0, 2, 2]
    num_items = len(arr)
    random_index = random.randrange(num_items)
    print("Random value:", arr[random_index])


# Xem thêm 'random_func.py'
def random_using_choice():
    arr = [1, 4, 2, 7, 0, 2, 2]
    winner = random.choice(arr)
    print(winner)

def random_multiple_value():
    arr = [1, 4, 2, 7, 0, 2, 2]
    winners = random.sample(arr, 2)
    print(winners)


# shuffle_list()
# shuffle_string()
# random_using_index()
# random_using_choice()
random_multiple_value()
