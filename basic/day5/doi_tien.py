# a = [500, 200, 100, 50, 20, 10, 5, 2, 1]

a = [200, 100, 20, 10, 5]

t = int(input("So tien can doi: "))

for x in a:
    print(t // x, "tờ", x)
    t %= x
