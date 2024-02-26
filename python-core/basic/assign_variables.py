"""
    Một số cách gán giá trị cho biến
"""

# Assign multiple variables
def assign1():
    x, y, z = 1, 2, "3"
    x = y = z = "orange"


# Unpack a collection
def assign2():
    fruits = ["banana", "strawberry", "cherry"]
    x, y, z = fruits
    print(x, y, z)


# Get all items in the middle of the list_type
def assign3():
    _, *elements_in_the_middle, _ = [1, 2, 3, 4, 5]
    print(elements_in_the_middle)  # [2, 3, 4]


# assign1()
# assign2()
assign3()
