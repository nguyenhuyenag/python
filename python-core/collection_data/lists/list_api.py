"""
    5 * [0] = [0, 0, 0, 0, 0]

    A = [1, 2]
    B = [3, 4]

    A.append(B) = [1, 2, [3, 4]]
    B.extend(B) = [1, 2, 3, 4]
"""


def append_first():
    arr = ['a', 'b']
    arr = [0] + arr
    arr.insert(0, "z")
    arr = [-2, *arr]
    print("Append first: ", arr)


def list_api():
    arr = [1, 2, 1, 3, 4, 1, 5]

    arr.count(1)            # Return the number of times the specified element appears in the lists

    arr.pop()               # ~ arr.pop(-1) Get and remove the last item
    arr.pop(2)              # Get and remove the item at the give index

    arr.reverse()           # Reverse lists
    arr = arr[::-1]
    arr = reversed(arr)

    print(arr)


# append_first()
list_api()
