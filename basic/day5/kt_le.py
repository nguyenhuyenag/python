n = int(input("Nhap n: "))

# while n % 2 != 0:
#     n //= 10
# if n == 0:
#     print("Co so le")
# else:
#     print("Toan so chang")

# while n != 0:
#     if n % 2 != 0:
#         print("Co so le")
#         break
#     n //= 10
# if n == 0:
#     print("Toan so chang")


def isOdd(n):
    while n % 2 != 0:
        n //= 10
    return n == 0


if isOdd(n):
    print("Co so le")
else:
    print("Toan so chang")

