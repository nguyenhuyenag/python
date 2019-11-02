# http://www.cse.net.vn/python/linearregression.html


def toNumber(a):
    for i in range(len(a)):
        a[i] = eval(a[i])
    return a


f = open("data.txt", "r")
x = []
y = []
avgX = 0
avgY = 0
for line in f:
    # print(line)
    a = toNumber(line.rstrip().split("\t"))
    # print(a)
    x.append(a[0])
    y.append(a[1])
    avgX += a[0]
    avgY += a[1]
f.close()

# print(avgX)
# print(avgX)

# Tinh trung binh
n = len(x)
avgX /= n
avgY /= n
t = 0
z = 0

for i in range(n):
    t += (x[i] - avgX) * (y[i] - avgY)
    z += (x[i] - avgX)**2

# print(t)
# print(z)

b1 = t / z

b0 = avgY - b1 * avgX

# PTHQUL: y = b0 + b1x

print("y = %.0f + %.0fx" % (b0, b1))
