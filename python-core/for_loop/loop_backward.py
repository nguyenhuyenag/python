"""
    Loop backwards
"""

n = 5

def _range_three_params():
    print(list(range(n, 0, -1)))


def _reverse():
    print(list(reversed(range(n + 1))))


def _slice_syntax():
    print(list(range(n + 1)[::-1]))


_range_three_params()
_reverse()
_slice_syntax()
