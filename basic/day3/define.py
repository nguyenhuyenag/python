# def sum(a, b):
#     return a + b

# x, y = eval(input("x = ")), eval(input("y = "))
# print("%d + %d = %d" % (x, y, sum(x, y)))

# y = int(input("Nam: "))
# if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#     print("%d la nam nhuan" % y)
# else:
#     print("%d khong la nam nhuan" % y)

# def foo(*args):
#     for a in args:
#         print(a)

# foo(1, "2", 3, 4, 5, 9)


def isLeap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


def getDayOfmonth(m, y):
    if m > 13:
        return
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    elif m == 2:
        if isLeap(y):
            return 29
        else:
            return 28
    else:
        return 31


m, y = int(input("month = ")), int(input("year = "))

print("Thang %d, nam %d co %d ngay" % (m, y, getDayOfmonth(m, y)))
