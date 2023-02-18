from itertools import dropwhile

int_list = [0, 1, 2, 3, 4, 5, 6]
result = list(dropwhile(lambda x: x < 3, int_list))
print(result)
