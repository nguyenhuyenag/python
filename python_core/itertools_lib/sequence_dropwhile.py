from random import shuffle
from itertools import dropwhile

# Từ phần tử đầu tiên không thỏa điều kiện
li = [0, 1, 2, 3, 4, 5, 6]
shuffle(li)
print(li)
result = list(dropwhile(lambda x: x < 3, li))
print("x < 3: ", result)
