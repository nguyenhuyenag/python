# Mảng nhiều chiều
import numpy as np

arr1 = np.array(42)
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr1.ndim) # = 0
print(arr2.ndim) # = 1
print(arr3.ndim) # = 2
print(arr4.ndim) # = 3

arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5)
print('number of dimensions :', arr5.ndim)