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
    arr = [1, 2, 3, 4, 5]

    arr.pop()           # = arr.pop(-1) Get and remove the last item
    arr.pop(2)          # Get and remove the iteam at the give index, de

    print(arr)


# append_first()
list_api()