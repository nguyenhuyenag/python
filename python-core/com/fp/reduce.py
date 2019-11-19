from functools  import reduce

# reduce(function, sequence)
def add(x, y):
    return x + y

s = reduce(add, range(1, 11))

print(s)