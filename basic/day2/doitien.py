m = int(input("Nhap tien: "))
tmp = m
# đổi ra tờ 50
to50 = m // 50
# dư lại
m %= 50

to20 = m // 20
m %= 20

to10 = m // 10
m %= 10

to5 = m // 5
m %= 5

to1 = m

print(to50, to20, to10, to5, to1)

print("Check: %d = %d" % (to50 * 50 + to20 * 20 + to10 * 10 + to5 * 5 + to1, tmp))
