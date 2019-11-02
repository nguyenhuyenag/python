f = open("data/data.txt")

# read line
print(f.readline())

# read all
print(f.read())

for x in f:
    print(x)

f.close()
