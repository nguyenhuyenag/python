from itertools import zip_longest


def zip_loop():
    # zip() iterates up to the length of the shortest iterator
    for v in zip("ABCD", "xy"):
        print(v, end=" ")
    print()


def zip_longest_loop():
    # zip_longest() iterates up to the length of the longest iterator
    # zip_longest() will go through all entries, and if one of the iterators runs out early, it gets replaced with None
    for v in zip_longest("ABCD", "xy", fillvalue="-"):
        print(v, end=" ")


if __name__ == '__main__':
    zip_loop()
    zip_longest_loop()
