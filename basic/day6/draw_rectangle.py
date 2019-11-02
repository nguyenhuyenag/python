m = int(input("Dong: "))
n = int(input("Cot: "))

for i in range(m):
    for j in range(n):
        #if i == 0 or i == m - 1 or j == 0 or j == n - 1:\
        if i in (0, m - 1) or j in (0, n - 1) :
            print("*", end = ' ')
        else:
            print(" ", end = ' ')
    print()
