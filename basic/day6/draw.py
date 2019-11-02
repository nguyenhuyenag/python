n = 0
while n != -1:
    n = int(input("Nhap n: "))
    if n % 2 == 0:
        print("n phai la so le")
    else:
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
