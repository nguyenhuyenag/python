from functools  import reduce

# reduce(function, sequence)
def add(x, y):
    return x + y

fruit = reduce(add, range(1, 11))

print(fruit)