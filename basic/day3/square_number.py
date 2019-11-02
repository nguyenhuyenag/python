def isSquareNumber(n):
    return int(n ** 0.5) * int(n ** 0.5) == n

n = int(input("n = "))

if isSquareNumber(n):
    print(n, "la so chinh phuong")
else:
    print("%d khong la so chinh phuong" % n)