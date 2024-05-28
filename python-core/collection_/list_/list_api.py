import operator

"""
    5 * [0] = [0, 0, 0, 0, 0]

    A = [1, 2]
    B = [3, 4]

    A.append(B) = [1, 2, [3, 4]]
    B.extend(B) = [1, 2, 3, 4]
"""
def append_first():
    arr = ['a', 'b']
    arr = [1] + arr
    arr.insert(0, "2")
    arr = [3, *arr]
    print("Append first: ", arr)


def list_api():
    arr = [1, 2, 1, 3, 4, 1, 5, 8, 0, 11, 7]

    arr.count(1)                    # Count 1

    idx = arr.index(7)              # Return the index of the first of occurrence
    # operator.indexOf(arr, 7)

    del arr[2]                      # Remove the value at index
    # arr.pop()                     # = pop(-1) get and remove the last item
    # arr.pop(2)                    # Get and remove the item at the give index
    # operator.delitem(arr, 0)

    arr.remove(3)                   # Remove first occurrence of value. ValueError if x not in list

    print(arr)

def reverse_list():
    arr = [1, 2, 3, 4, 5]

    """
        Reverse it self -> return None
    """
    arr.reverse()

    """
        Reverse & create a new list
    """
    # arr = arr[::-1]

    """
        reversed() -> Trả về một đối tượng reversed iterator
    """
    # arr = list(reversed(arr))

    print(arr)


if __name__ == '__main__':
    # list_api()
    # append_first()
    reverse_list()
