"""
    Built-in Functions
"""

"""
    a = b*m + n     ->      divmod(a, b) = (m, n)
"""

result = divmod(9, 4)
print("divmod = ", result)  # Output: (2, 1)

# Sử dụng kết quả của divmod trong một cách khác
quotient, remainder = divmod(17, 5)
print("Quotient:", quotient)
print("Remainder:", remainder)
