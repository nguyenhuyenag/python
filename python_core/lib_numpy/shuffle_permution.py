import itertools

import numpy as np
from numpy import random

# Shuffle
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print("Shuffle: ", arr)

# Permution
print("Permution:", random.permutation(arr))

# Find all permuton
print("Find all permution")
for e in list(itertools.permutations([1, 2, 3])):
    print(e)


def perm(a, k=0):
    if k == len(a):
        print(a)
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            perm(a, k + 1)
            a[k], a[i] = a[i], a[k]


print("Find all permutation")
perm([1, 2, 3])
