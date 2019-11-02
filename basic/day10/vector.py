# http://www.cse.net.vn/python/pr.html
import rs

def error(u, v):
    s = 0
    for i in range(len(u)):
        s += abs(u[i] - v[i])
    return s


def multi(m, v):
    row = len(m)
    col = len(m[0])
    result = col * [0]
    for i in range(row):
        for j in range(col):
            result[i] += m[i][j] * v[j]
    return result

m = [
    [0,   0, 0.5, 0.5, 1/3],
    [0,   0,   0,   0, 1/3],
    [1/3, 0,   0, 1/2, 1/3],
    [1/3, 0, 0.5,   0,   0],
    [1/3, 1,   0,   0,   0]
]

# u = [0, 3, 5, 7]
# v = [2, 4, 6, 8]
# e = error(u, v)
# print(e)

c = len(m[0])

p = c * [1]

q = multi(m, p)

e = 1
epsilon = 0.1

while e > epsilon:
    q = multi(m, p)
    e = error(p, q)
    print(e)
    p = q

print(p)
