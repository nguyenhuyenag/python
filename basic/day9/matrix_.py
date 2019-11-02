import rs

arr = []

for i in range(3):
    arr.append(5 * [0])

f = open(rs.getPath() + "/file/data.txt")

for line in f:
    a = rs.toNumber(line.rstrip().split(","))
    # set value
    arr[a[0]-1][a[1]-1] = a[2]

f.close()

rs.printMatrix(arr)
