import copy as cp

arr = [1, 2, 3, 4, 5, 6]

shallow_copy = cp.copy(arr)
deep_copy = cp.deepcopy(arr)

print("id=", id(arr))
print("id=", id(shallow_copy))
print("id=", id(deep_copy))
