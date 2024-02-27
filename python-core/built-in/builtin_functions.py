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
def bin_int2():
    num = 15
    bi = bin(num)
    print("bin: bin({}) = '{}'".format(num, bin(num)))
    print("int: int('{}', 2) = {}".format(bin(num), num))


"""
    dir(): Lấy danh sách tất cả các tên biến, hàm, lớp,... của một đối tượng
"""
def dir_method():
    my_list = [1, 2, 3]
    print(dir(my_list))

"""
    eval(): Tính giá trị một biểu thức kiểu string
"""
def eval_method():
    s3 = "3 * (1 + 6/2)"
    s1 = "5 == 5"
    s2 = "10 ** 2"
    s4 = "'Hello' * 5"
    print("eval: '{}' => {}".format(s1, eval(s1)))
    print("eval: '{}' => {}".format(s2, eval(s2)))
    print("eval: '{}' => {}".format(s3, eval(s3)))
    print("eval: '{}' => {}".format(s4, eval(s4)))


"""
    globals(): Trả về 1 dictionary chứ các biến global
"""
def _globals():
    print(globals())

"""
    locals(): Trả về dictionary chưa các biến local
"""
def _locals():
    x = 1
    y = 2
    print(locals())

"""
    callable(): Kiểm tra 1 đối tượng có thể gọi được không
"""
def callable_method():
    pass


"""
    hasattr(): Kiểm tra một đối tượng có chứa thuộc tính nào đó hay không
"""
def hasattr_method():
    the_dict = {}
    # Kiểm tra có thuộc tính 'items' hay không
    h = hasattr(the_dict, 'items')
    # Kiểm tra 'items' có thể gọi được hay không
    x = callable(the_dict.items)
    print(f"hasattr = {h}, callable = {x}")


"""
    hash(): Tạo mã băng của một đối tượng
"""
def hash_method():
    # Băm số nguyên
    gia_tri_bam = hash(42)
    print(gia_tri_bam)

    # Băm chuỗi
    chuoi_bam = hash("xin chào")
    print(chuoi_bam)

    # Băm tuple
    tuple_bam = hash((1, 2, 3))
    print(tuple_bam)


"""
    help(): Hiển thị document của một đối tượng
"""
def help_method():
    help(list)


"""
    input(): Lấy dữ liệu nhập vào từ bàn phím
"""
def _input():
    # Read multiple value
    # a, b, c = input().split(",")
    # print(a, b, c)
    user_input = input("Nhập vào một giá trị: ")
    print("Bạn đã nhập:", user_input)

def _int():
    print("For '123', int is:", int("123"))
    print("For 123.45, int is:", int(123.45))

    # converting a string (that is in binary format) to integer
    print("For 0b101, int is:", int("0b101", 2))

    # converting a string (that is in octal format) to integer
    print("For 0o16, int is:", int("0o16", 8))

    # converting a string (that is in hexadecimal format) to integer
    print("For 0xA, int is:", int("0xA", 16))

"""
    isinstance(): Kiểm tra kiểu dữ liệu của một đối tượng
"""
def _isinstance():
    x = 5
    print(isinstance(x, int))  # Kết quả: True, x là số nguyên
    print(isinstance("Hello", str))  # Kết quả: True, y là xâu ký tự
    print(isinstance([1, 2, 3], list))  # Kết quả: True, z là danh sách
    print(isinstance(x, (int, float)))  # Kết quả: True

if __name__ == '__main__':
    # all_any()
    # ascii_repr()
    # bin_int2()
    # dir_method()
    # eval_method()
    _locals()
    # _globals()
    # callable_method()
    # hasattr_method()
    # hash_method()
    # help_method()
    # _input()
    # _int()
    # _isinstance()
