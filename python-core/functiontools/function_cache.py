import time
from functools import cache


def cal(n):
    if n < 2:
        return n
    else:
        return cal(n - 1) + cal(n - 2)


@cache
def cal_cache(n):
    if n < 2:
        return n
    else:
        return cal(n - 1) + cal(n - 2)


def cal_dp(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])

    return arr[n]


def cal_dp2(n):
    arr = (n + 1) * [0]
    # arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


def method_name():
    n = 30

    # Without @cache
    t1 = time.time()
    f = cal(n)
    t2 = time.time()
    print(f"KQ = {f}")
    print(f"Time (no @cache) = {t2 - t1}")

    # Use @cache
    t1 = time.time()
    f = cal_cache(n)
    t2 = time.time()
    print(f"KQ = {f}")
    print(f"Time (@cache) = {t2 - t1}")

    # Use DP
    t1 = time.time()
    f = cal_dp2(n)
    t2 = time.time()
    print(f"KQ = {f}")
    print(f"Time (DP) = {t2 - t1}")


method_name()
