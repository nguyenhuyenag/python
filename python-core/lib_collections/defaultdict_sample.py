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


def todo():
    arr = 'abdacvcdcscbcbgnmnnb'
    counts = defaultdict(lambda : 0)
    for key in list(arr):
        counts[key] += 1
    print(counts.items())


normal()
todo()