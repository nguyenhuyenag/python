"""
    Toán tử walrus
"""

"""
    Old type
"""
x = 5
if x > 0:
    print(x)

"""
    New type
"""
if (x := 5) > 0:
    print(x)