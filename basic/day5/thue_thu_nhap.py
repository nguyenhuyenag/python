income = int(input("Thu nhap: "))

a = [0, 4, 6, 9, 14, 24, 44, 84, 9999999]

s = 0
t = 0

for i in range(1, len(a)):
    if income > a[i]:
        s += (a[i] - a[i-1])*t
    else:
        s += (income - a[i-1])*t
        break
    t += 0.5
print("Thue phai dong: ", s)