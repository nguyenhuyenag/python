# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))

#======#
_max = a
if _max < b:
    _max = b
if _max < c:
    _max = c
print("max(%d, %d, %d) = %d" % (a, b, c, _max))

#======#
if a > b and a > c: # a la max
    print("max = ", a)
elif b > c: # a khong the la max
    print("max = ", b)
else:
    print("max = ", c)

#======#
print("max = ", max(a,b,c))