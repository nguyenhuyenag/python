# It's a function that takes a series of iterables and return one iterable
from itertools import chain

l1 = [0, 2, 4]
l2 = [1, 3, 5]
l3 = chain(l1, l2)
print("L3:", l3)

# Because string is considered to be an iterable
l4 = list(chain("ABC", "DEF", "GHK"))
print("l4:", l4)
