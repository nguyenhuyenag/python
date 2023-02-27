from random import shuffle
from itertools import takewhile

# Trả về các phần tử thỏa mãn điều kiện cho đến khi có 1 giá trị sai
li = [0, 5, 2, 4, 8, 22, 34, 6, 67]
shuffle(li)
print(li)
filter_list = list(takewhile(lambda x: x % 2 == 0, li))
print("x % 2 == 0: ", filter_list)
