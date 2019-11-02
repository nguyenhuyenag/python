h1 = int(input("h1: "))
m1 = int(input("m1: "))
s1 = int(input("s1: "))
h2 = int(input("h2: "))
m2 = int(input("m2: "))
s2 = int(input("s2: "))

# s = (s1 + s2) % 60
# m = (m1 + m2 + (s1 + s2)//60) % 60
# h = (h1 + h2 + (m1 + m2 + (s1 + s2) // 60) // 60) % 24

s = s1 + s2
m = h1 + h2 + s // 60
h = h1 + h2 + m // 60
s = s % 60
m = m % 60
h = h % 24


print(h, m, s)
