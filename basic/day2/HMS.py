h = int(input("gio: "))
m = int(input("phut: "))
s = int(input("giay: "))
k = int(input("k: "))

t = (h * 3600 + m * 60 + s + k) % (24 * 3600)  # 1 ngay
h = t // 3600
m = (t // 60) % 60
s = t % 60
print("%d:%d:%d" % (h, m, s))
