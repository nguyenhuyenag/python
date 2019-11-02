f = open("data/toeic.txt")

# read line 1
listening = f.readline().split()

# read line 2
reading = f.readline().split()

# print(listening)
# print(reading)

l = int(input("Listening: "))
r = int(input("Reading: "))

dl = listening[l]
dr = reading[r]

print("Listening: %s, Reading: %s, Total: %d" % (dl, dr, int(dl) + int(dr)))

f.close()
