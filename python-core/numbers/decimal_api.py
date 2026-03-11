from decimal import Decimal, getcontext

"""
    Tăng giới hạn số thập phân
"""


def prec():
    getcontext().prec = 77
    d = Decimal(1) / Decimal(69)
    print(d)


"""
    Tìm dạng phân số của một số thập phân (kết quả không phải là duy nhất hoặc tốt nhất) 
"""
def as_integer_ratio():
    n = 0.1
    print(n.as_integer_ratio())


if __name__ == '__main__':
    # prec()
    as_integer_ratio()
