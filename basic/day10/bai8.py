# http://www.cse.net.vn/c/assignment04.html

gia_phong = {"A": 250000, "B": 200000, "C": 150000}

p = {"A": 0.1, "B": 0.08, "C": 0.08}

loai = input("Chon loai phong (A, B, C): ")

day = int(input("So ngay: "))

s = gia_phong[loai] * day

if day > 12:
    s *= 1 - p[loai]

print("Tien phong: ", int(s))
