def tuple_init():
    thistuple = ("apple",)
    print(type(thistuple))

    thistuple = tuple(("apple", "banana", "apple", "cherry"))  # note the double round-brackets
    print(type(thistuple))

    # NOT a tuple
    thistuple = ("apple")
    print(type(thistuple))


def unpack_tuple():
    # unpack tuple
    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    (green, yellow, *red) = fruits
    print(green)
    print(yellow)
    print(red)


tuple_init()
# unpack_tuple()
