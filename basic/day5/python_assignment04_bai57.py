def isIncrease(n):
    while n >= 10:
        ss = n % 10
        n //= 10
        st = n % 10
        if ss < st:
            return False
    return True


n = int(input("Nhap n: "))
if isIncrease(n):
    print("so tang")
else:
    print("khong tang")
