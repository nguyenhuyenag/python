from numpy import random

print(random.rand())

x = random.randint(100)
print("Random a number < 100:", x)

# Mảng 1 chiều 5 phần từ
print(random.randint(100, size=5))

# Mảng 2 chiều 5 phần tử
print(random.randint(100, size=(2, 5)))

# Generate random number from array
print("From array:", random.choice([1, 3, 6, 9, 0]))

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0
# The sum of p should be 1
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=100)
print(x)
