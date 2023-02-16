# String are arrays
str = "strawberry"

# First and last index
print(str[0] + str[-1])

# looping through a string
for s in str:
    print(s)

# Check string
txt = "The best things in life are free"
print("life" in txt)
print("life" not in txt)

if "life" in txt:
    print("Yes")

# Slicing
print(str[2:5])
print(str[:5])
print(str[2:])
print(str[-1:0])

# Format
str = "Hello, I'm {}, first appeared {}"
print(str.format("Python", 1991))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(3, 576, 10.5))