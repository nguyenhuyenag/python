# filter(function, sequence)
def func(x):
    return x % 2 != 0 and x % 3 != 0


fil = filter(func, range(2, 25))

for x in fil:
    print(x)
