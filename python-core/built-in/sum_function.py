from decimal import Decimal
from fractions import Fraction

"""
    Builtin Functions
"""
"""
    sum(iterable, start): Tính tổng với giá trị bắt đầu
"""
the_list = [1, 2, 3, 4, 5]

print(sum(the_list, 100))
print(sum(the_list, start=100))

# Sum complex numbers
print("Complex: ", sum([3 + 2j, 5 + 6j]))

# Sum Decimal numbers
print("Decimal: ", sum([Decimal(0.2), Decimal(0.3), Decimal("0.4")]))

# Sum Fraction numbers
print("Faction: ", sum([Fraction(51, 5), Fraction(25, 2), Fraction(59, 5)]))

"""
    Concatenating Sequences
"""
list_of_list = [[1, 2, 3], [4, 5, 6]]
# Tương đương: [] + [1,2,3] + [4,5,6] = [1,2,3,4,5,6]
flat_list = sum(list_of_list, start=[])
print(f"Flat: {list_of_list} -> {flat_list}")
