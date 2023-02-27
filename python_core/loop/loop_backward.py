# Loop backwards
n = 5


def by_reverse():
    print(list(reversed(range(n + 1))))


def by_range_three_params():
    print(list(range(n, -1, -1)))


def by_slice_syntax():
    print(list(range(n + 1)[::-1]))


by_reverse()
by_range_three_params()
by_slice_syntax()
