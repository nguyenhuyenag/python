from pathlib import Path

# file = Path(__file__).with_name('data.txt')

f = open("file/data.txt")

print(f.readline())

print(f.read())

# For loop
for line in f:
    print(line)
    
f.close()
