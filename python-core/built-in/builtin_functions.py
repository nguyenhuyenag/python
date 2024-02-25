"""
    Built-in Functions
"""

boolean_list = [True, False, True]

"""
    any() -> True nếu có một phần tử = True
"""
print("any: ", any(boolean_list))

"""
    all() -> True nếu tất cả các phần tử = True
"""
print("all: ", all(boolean_list))

"""
    ascii() & repr(): Trả về một chuỗi được biểu diễn bởi các ký tự ASCII,
                      nếu không thể biểu diễn bởi ASCII nó sẽ chuyển đổi thành 
                      một chuỗi chứa các ký tự thoả mãn các ràng buộc ASCII.
"""
arr = [1, 2, 'a', 'ả']
print("repr: ", repr(arr))
print("ascii: ", ascii(arr))
