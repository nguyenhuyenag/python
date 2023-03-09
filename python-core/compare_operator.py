"""
    A is B    ->  True if both variables are the same object in memory, else False
    A == B    ->  Compares the equality of values that these 2 objects hold
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)  # True   because z is the same object as x
print(x is y)  # False  because x is not the same object as y, even if they have the same content
print(x == y)  # True
