import numpy as np

"""
    bin(): Chuyển đổi int <-> binary
    int('111', 2)
"""
def bin_int2():
    num = 15
    bi = bin(num)
    print("bin: bin({}) = '{}'".format(num, bin(num)))
    print("int: int('{}', 2) = {}".format(bin(num), num))

"""
    Đổi cơ số bất kỳ
"""
def conver_any():
    n = 12
    print(np.base_repr(n, base=2))

if __name__ == '__main__':
    bin_int2()
    conver_any()
