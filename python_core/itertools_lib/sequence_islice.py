from itertools import islice
"""
    islice(iterable, start, stop, step)
    islice('ABCDEFG', 2)            --> A B
    islice('ABCDEFG', 2, 4)         --> C D
    islice('ABCDEFG', 2, None)      --> C D E F G
    islice('ABCDEFG', 0, None, 2)   --> A C E G
"""

# Slicing the range function
print(list(range(20)))
for i in islice(range(20), 5):
    print(i)