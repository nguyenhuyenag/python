# A_mn x B_np = C_mp
a = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

b = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

dong = len(a)
cot = len(a[0])
p = len(b[0])
c = []

for i in range(dong):
    c.append(p * [0])

for i in range(dong):
    for j in range(cot):
        for k in range(p):
            c[i][k] += a[i][j] * b[j][k]

for i in range(dong):
    print(c[i])
