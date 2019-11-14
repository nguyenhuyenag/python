a = int(input("Nhap: "))
dv = a % 10
ch =  (a // 10) % 10
tr = a // 100
b = dv * 100 + ch * 10 + tr
print(b)
