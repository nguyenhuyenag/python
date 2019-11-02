def abs(a, b):
    x = a - b
    return x if x > 0 else -x

a, b = int(input("a = ")), int(input("b = "))

print("|%d - %d| = %d" % (a, b, abs(a, b)))
