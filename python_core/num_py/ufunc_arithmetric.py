import numpy as np

# Cộng phần tử 2 mảng
a1 = [5, 6, 7, 8]
a2 = [1, 2, 3, 4]

# a1 + a2
print(np.add(a1, a2))

# a1 - a2
print(np.subtract(a1, a2))

# a1 * a2
print(np.multiply(a1, a2))

# a1 / a2
print(np.divide(a1, a2))

# a1 ^ a2
print(np.power(a1, a2))

# a1 mod a2 = a1 // a2
print(np.mod(a1, a2))

# = hàm abs()
arr = np.array([-1, -2, 1, 2, 3, -4])
print(np.absolute(arr))
