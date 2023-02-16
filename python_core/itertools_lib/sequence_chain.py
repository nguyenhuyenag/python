# It's a function that takes a series of iterables and return one iterable
from itertools import chain

l1 = [0, 2, 4]
l2 = [1, 3, 5]
L = list(chain(l1, l2))
print("L:", L)

# Because string is considered to be an iterable
l4 = list(chain("ABC", "DEF", "GHK"))
print("l4:", l4)

# Chain from iterable
li = ['123', '456', '789']
print("Chain:", list(chain(li)))

from_iterable = list(chain.from_iterable(li))
print("Chain from iterable:", from_iterable)

# li = ['123', '456', '789'] -> 1 + 2 + 3 + 4 + ... = 45
from_iterable = list(map(int, from_iterable))
print("Sum: ", sum(from_iterable))
