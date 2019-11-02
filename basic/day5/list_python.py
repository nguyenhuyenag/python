def isLeap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m = int(input("Thang: "))
y = int(input("Nam: "))

if isLeap(y):
    arr[1] = 29

print("Thang %d nam %d co %d ngay" % (m, y, arr[m - 1]))
