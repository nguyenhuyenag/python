u = [19, 26, 1, 0, 77]
v = [1, 2, 5, 9, 10]
n = len(u)
x = n * [0]
for i in range(n):
    x[i] = u[i] + v[i]
print(x)
