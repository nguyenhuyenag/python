# map(function, sequence)
def square(i):
    return i * i


lst = map(square, [1, 2, 3, 4, 5])

lst = map(lambda i: i ** 2, [1, 2, 3, 4, 5])

for x in lst:
    print(x, end=" ")

seq = range(8)

print()


def add(x, y):
    return x + y


rel = map(add, seq, seq)

for x in rel:
    print(x, end=" ")
