f = open("data.txt", "r")
a = f.readline().rstrip().split()
#print(line)
dict = {}
for x in a:
    x = int(x)
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] += 1
for k in dict:
    print(k , "=>", dict[k])
