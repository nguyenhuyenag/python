# Init
arr = 5 * [0]
print("Init: ", arr)

# append first
arr = ['a', 'b']
arr = [0] + arr
arr.insert(0, -1)
arr = [-2, *arr]
print("Append first: ", arr)

# append & extend
arr.append([1, 2, 3])
print("Append: ", arr)
arr = ['a', 'b']
arr.extend([1, 2, 3])
print("Extend: ", arr)
