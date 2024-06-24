"""
    Loop backwards
"""

def _range_three_params():
    arr = [8, 0, 10, 5, 77]
    for i in range(len(arr) - 1, -1, -1):
        print(f"index={i}, value={arr[i]}")


def _reverse():
    # [5, 4, 3, 2, 1, 0]
    n = 5
    print(list(reversed(range(n + 1))))


def _slice_syntax():
    n = 5
    print(list(range(n + 1)[::-1]))


_range_three_params()
# _reverse()
# _slice_syntax()
