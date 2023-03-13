from collections.abc import Iterable


def using_type():
    var = 1
    if type(var) == int:
        print("Is integer")


# is collections
def is_collections():
    print("[] -> ", isinstance([], Iterable))
    print("{} -> ", isinstance({}, Iterable))
    print("None -> ", isinstance(None, Iterable))


# is string
def is_string():
    print("None -> ", isinstance(None, str))
    print("'av' -> ", isinstance("av", str))
    print("'[1, 2, 3]' -> ", isinstance([1, 2, 3], str))


def is_integer():
    print("'123' -> ", isinstance('123', int))
    print("123 -> ", isinstance(123, int))


def is_byte_array():
    # string = "Python is interesting"
    # arr = bytes(string, 'utf-8')
    arr = b'Python is interesting'
    print(arr)
    print(list(arr))
    print("123 -> ", isinstance(arr, bytes))
    print("123 -> ", isinstance(arr, bytearray))


# is_collections()
# is_string()
# is_integer()
is_byte_array()