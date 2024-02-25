"""
    Built-in Functions
"""

"""
    any() -> True nếu có một phần tử = True
    all() -> True nếu tất cả các phần tử = True
"""
def all_any():
    boolean_list = [True, False, True]
    print("any: [True, False, True] -> {}".format(any(boolean_list)))
    print("all: [True, False, True] -> {}".format(all(boolean_list)))


"""
    ascii() & repr(): Trả về một chuỗi được biểu diễn bởi các ký tự ASCII,
                      nếu không thể biểu diễn bởi ASCII nó sẽ chuyển đổi thành 
                      một chuỗi chứa các ký tự thoả mãn các ràng buộc ASCII.
"""
def ascii_repr():
    arr = [1, 2, 'a', 'ả']
    print("repr: ", repr(arr))
    print("ascii: ", ascii(arr))


"""
    bin(): Chuyển đổi int <-> binary
    int('111', 2)
"""
def bin_int_2():
    num = 15
    bi = bin(num)
    print("bin: bin({}) = '{}'".format(num, bin(num)))
    print("int: int('{}', 2) = {}".format(bin(num), num))


"""
    dir(): Lấy danh sách tất cả các tên biến, hàm, lớp,... của một đối tượng
"""
def dir_method():
    my_list = [1, 2, 3]
    list_names = dir(my_list)
    print(list_names)


if __name__ == '__main__':
    # all_any()
    # ascii_repr()
    # bin_int_2()
    dir_method()
