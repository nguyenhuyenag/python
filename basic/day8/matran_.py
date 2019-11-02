a = [
    [91, 2, 663, 4, 65, 68],
    [11, 278, 3, 48, 5, 55],
    [20, 12, 34, 47, 5, 44],
    [101, 22, 43, 4, 5, 86]
]

dong = len(a)
cot = len(a[0])

print("Ma tran: %d x %d" % (dong, cot))

for i in range(dong):
    for j in range(cot):
        print(a[i][j], end='  ')
    print()


def sumOnRow(a):
    v = [0] * dong
    for i in range(dong):
        for j in range(cot):
            v[i] += a[i][j]
    return v


def sumOnCol(a):
    u = [0] * cot
    for j in range(cot):
        for i in range(dong):
            u[j] += a[i][j]
    return u


d = sumOnRow(a)
print("Tong tren dong: ", d)

c = sumOnCol(a)
print("Tong tren cot: ", c)

print("Ma tran x Vector")
v = [0] * cot #
u = [1, 4, 6, 9, 8, 0]
for i in range(dong):
    for j in range(cot):
        v[i] += a[i][j] + u[j]
print(v)
