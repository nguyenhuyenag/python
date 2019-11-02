import rs

def coeffMatrix(arr):
    b = rs.matrix(5, 5)
    for i in range(5):
        for j in range(i, 5):
            c = 0
            for k in range(3):
                if arr[k][i] * arr[k][j] != 0:
                    c += 1
            b[i][j] = c
            b[j][i] = c
    return b


arr = rs.createData()

rs.printMatrix(arr)

print()

b = coeffMatrix(arr)

rs.printMatrix(b)
