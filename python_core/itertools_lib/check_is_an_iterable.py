from collections.abc import Iterable

a = None
b = []
c = {}
print("a: ", isinstance(a, Iterable))
print("b: ", isinstance(b, Iterable))
print("c: ", isinstance(c, Iterable))