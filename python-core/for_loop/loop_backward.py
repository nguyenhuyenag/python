# Loop backwards
n = 5


def _range_three_params():
    print(list(range(n, -1, -1)))


def _reverse():
    print(list(reversed(range(n + 1))))


def _slice_syntax():
    print(list(range(n + 1)[::-1]))


_reverse()
_range_three_params()
_slice_syntax()
