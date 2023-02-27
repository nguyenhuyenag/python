from itertools import combinations

"""
    combinations('ABCD', 2) --> AB AC AD BC BD CD
    combinations(range(4), 3) --> 012 013 023 123
    n! / (r! * (n-r)!) when 0 <= r <= n or zero when r > n
"""


def combinate():
    for v in combinations('ABCD', 2):
        print("".join(v), end="  ")


combinate()
