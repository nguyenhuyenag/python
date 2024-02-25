# Assign multiple variables
def assign1():
    x, y, z = 1, 2, "3"
    print(x, y, z)


# One value to multiple variables
def assign2():
    x = y = z = "orange"
    print(x, y, z)


# Unpack a collection
def assign3():
    fruits = ["banana", "strawberry", "cherry"]
    x, y, z = fruits
    print(x, y, z)


# Get all items in the middle of the list_type
def assign4():
    _, *elements_in_the_middle, _ = [1, 2, 3, 4, 5]
    print(elements_in_the_middle)  # [2, 3, 4]


assign4()
