from itertools import pairwise

"""
    pairwise('ABCDEFG') --> AB BC CD DE EF FG
"""

l = [1, 2, 3, 4, 5, 6, 7]
print(list(pairwise(l)))
