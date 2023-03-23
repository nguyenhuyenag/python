import itertools_lib.sequence_ziplongest as zp


def method_name():
    n = 10
    for i, j in zip(range(n), range(n - 1, -1, -1)):
        print(i, j)


# method_name()
zp.zip_loop()
zp.zip_longest_loop()
