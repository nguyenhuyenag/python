import numpy as np

arr = np.array([1, 9, -8, 12, 50, 11, 84, 3, 0])

filter_arr = arr > 15
print(arr[filter_arr])

print(arr[arr % 2 == 0])

print(arr[arr % 2 != 0])

