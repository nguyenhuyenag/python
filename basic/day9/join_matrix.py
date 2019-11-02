import rs
a = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]
b = [
    [1, 3, 5],
    [1, 1, 1]
]
ra = len(a)
rb = len(b)
ca = len(a[0])
cb = len(b[0])

# init c[]
c = []
for i in range(ra + rb):
    c.append((ca + cb) * [0])

# add value
for i in range(ra):
    for j in range(ca):
        c[i][j] = a[i][j]

for i in range(rb):
    for j in range(cb):
        c[i + ra][j + ca] = b[i][j]

rs.printMatrix(c)
