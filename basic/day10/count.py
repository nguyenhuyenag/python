import rs

f = open(rs.getPath() + "/file/thongke.txt")
arr = f.readline().rstrip().split()
f.close()

dict = {}

for x in arr:
    x = int(x)
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] += 1

for k, v in dict.items():
    print(k, "=>", v)
