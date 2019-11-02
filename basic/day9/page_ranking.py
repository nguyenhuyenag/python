# http://www.cse.net.vn/python/pr.html

# C R
# 0 2
# 0 3

import rs

n = 5

b = rs.matrix(n, n)

f = open(rs.getPath() + "/file/page.txt")

for line in f:
    a = rs.toNumber(line.rstrip().split())
    b[a[1]][a[0]] = 1

f.close()

rs.printMatrix(b)

for j in range(n):
    s = 0
    # tinh tong cot
    for i in range(n):
        s += b[i][j]
    for i in range(n):
        b[i][j] /= s

rs.printMatrix(b)
