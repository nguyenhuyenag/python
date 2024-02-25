"""
    Built-in Functions
"""

"""
    any() -> True nếu có một phần tử = True
    all() -> True nếu tất cả các phần tử = True
"""
boolean_list = [True, False, True]
print("any: [True, False, True] -> {}".format(any(boolean_list)))
print("all: [True, False, True] -> {}".format(all(boolean_list)))
print()

"""
    ascii() & repr(): Trả về một chuỗi được biểu diễn bởi các ký tự ASCII,
                      nếu không thể biểu diễn bởi ASCII nó sẽ chuyển đổi thành 
                      một chuỗi chứa các ký tự thoả mãn các ràng buộc ASCII.
"""
arr = [1, 2, 'a', 'ả']
print("repr: ", repr(arr))
print("ascii: ", ascii(arr))
print()

"""
    bin(): Chuyển đổi int <-> binary
    int('111', 2)
"""
num = 15
bi = bin(num)
print("bin: bin({}) = '{}'".format(num, bin(num)))
print("int: int('{}', 2) = {}".format(bin(num), num))
print()
