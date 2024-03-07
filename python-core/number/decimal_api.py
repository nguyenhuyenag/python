from decimal import Decimal, getcontext

"""
    Tăng giới hạn số thập phân
"""
getcontext().prec = 1_00
d = Decimal(1) / Decimal(69)
print(d)
