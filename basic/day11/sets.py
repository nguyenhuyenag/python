a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {0, 2, 4, 6, 8}
# print(a)
# print(b)

#c = a.union(b)
c = a | b
print(c)

#d = a.intersection(b)
d = a & b
print(d)

#e = a.difference(b)
e = b - a
print(e)
