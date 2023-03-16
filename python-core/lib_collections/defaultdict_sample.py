from collections import defaultdict


def normal():
    arr = 'abdacvcdcscbcbgnmnnb'
    counts = {}
    for key in list(arr):
        if key not in counts:
            counts[key] = 1
        else:
            counts[key] += 1
    print(counts)


def using_defaultdict():
    arr = 'abdacvcdcscbcbgnmnnb'
    counts = defaultdict(lambda : 0)
    for key in arr:
        counts[key] += 1
    print(counts.items())


normal()
using_defaultdict()
