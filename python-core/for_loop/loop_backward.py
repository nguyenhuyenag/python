"""
    Loop backwards
"""

n = 5

def _range_three_params():
    # [5, 4, 3, 2, 1]
    print(list(range(n, -1, -1)))


def _reverse():
    # [5, 4, 3, 2, 1, 0]
    print(list(reversed(range(n + 1))))


def _slice_syntax():
    print(list(range(n + 1)[::-1]))


_range_three_params()
_reverse()
# _slice_syntax()
