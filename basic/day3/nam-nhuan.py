y = int(input("Nam: "))
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print("%d la nam nhuan" % y)
else:
    print("%d khong la nam nhuan" % y)
