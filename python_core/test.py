import copy, itertools
it = [1,2,3,4]
a, b = itertools.tee(it)
c = copy.copy(a)
print("a:", a)
print("b:", b)
print("c:", c)