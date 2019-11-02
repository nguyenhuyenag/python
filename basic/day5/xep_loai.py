a = [3, 5, 7, 8.5, 9, 10]

b = ["Kem", "Yeu", "TB", "Kha", "Gioi", "Xuat sac"]

avg = eval(input("Nhap diem: "))

for i in range(len(a)):
    if avg <= a[i]:
        print("Xep loai", b[i])
        break

# cach 2
# i = 0
# while avg >= a[i]:
#     i += 1
# print("Xep loai", b[i])