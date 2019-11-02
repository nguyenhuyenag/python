x = int(input("Nhap x "))
countMax = 0
max = 0
while x != 0:
    if max < x % 10:
        max = x % 10
        countMax = 1
    elif max == x % 10:
        countMax += 1
    x //= 10
print(countMax)
"""
Bai 4
x = int(input("Nhap so X "))
r = 0
while(x != 0):
    r = r * 10 + x % 10
    x //= 10
print(r)
Bai 3
x = 1;
while(x <= 10):
    print(x)
    x += 1
print(x)
Bai 1
n = int(input("Nhap so N "))
s = 0

for i in range(1, n * 2 + 2, 2):
    s += 1/i
print(s)
// Bai 2
n = int(input("Nhap so N "))
x = eval(input("Nhap x "))
s = 1 + x
p = 1
t = 1
for i in range(1, n+1):
    p *= (n * 2) + (n * 2 + 1)
    t *= x * x
    s += t/p
print (s)
"""
