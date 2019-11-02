# http://www.cse.net.vn/rs123.html
import rs

def toNumber(arr):
    for i in range(len(arr)):
        arr[i] = eval(arr[i])
    return arr


def printMatrix(arr):
    print()
    for i in range(len(arr)):
        print(arr[i])


def createMatrix(row, col):
    arr = []
    for i in range(row):
        arr.append(col * [0])
    return arr


# Tao ma tran tu file
def getData():
    A = createMatrix(4, 5)
    f = open(rs.getPath() + "/MoviesHistory.txt", "r")
    for line in f:
        arr = toNumber(line.rstrip().split(','))
        A[arr[0] - 1][arr[1] - 1] = arr[2]
    f.close()
    return A


# Ma tran he so
def getCoeff(arr):
    b = createMatrix(5, 5)
    for i in range(5):
        for j in range(i, 5):
            c = 0
            for k in range(4):
                if arr[k][i] * arr[k][j] != 0:
                    c += 1
            b[i][j] = c
            b[j][i] = c
    return b


# Tinh vector V
def sumOnCol(arr):
    dong = len(arr)
    cot = len(arr[0])
    u = [0] * cot
    for j in range(cot):
        for i in range(dong):
            u[j] += arr[i][j]
    return u


# Nhan 2 ma tran
def multiMatrix(a, b):
    dong = len(a)
    cot = len(a[0])
    p = len(b[0])
    c = createMatrix(dong, cot)
    for i in range(dong):
        for j in range(cot):
            for k in range(p):
                c[i][k] += a[i][j] * b[j][k]

    return c

# Lam tron so
def fixed(x):
    return eval("%.3f" % x)

def chuanHoa(arr, v):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            #arr[i][j] /= v[j]
            arr[i][j] = fixed(arr[i][j]/v[j])
    return arr



A = getData()
B = getCoeff(A)
V = sumOnCol(B)
C = multiMatrix(A,B)

print("Ma tran A", end="")
printMatrix(A)
print()
print("Ma tran B", end="")
printMatrix(B)
print()
print("Ma tran C", end="")
printMatrix(C)
print()
print("Vector V")
print(V)
print()
CH = chuanHoa(C,V)
print("Chuan hoa ma tran C", end="")
printMatrix(CH)
