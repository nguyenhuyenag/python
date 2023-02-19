from itertools import product

# Cartesian product of input iterables
# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
for v in product(['a', 'b', 'c'], [1, 2]):
    print(v, end=" ")
