"""
    Built-in Functions
"""

"""
    Mã hóa chuỗi thành mảng byte
    
    + encode(): Là phương thức của đối tượng chuỗi (str)
        
    + bytes(): Là hàm xây dựng để tạo đối tượng bytes từ một chuỗi hoặc iterable.
        
    + bytearray(): Là một lớp để tạo đối tượng mảng byte có thể thay đổi từ một chuỗi hoặc iterable.
"""

text = "Hello, world!"


# Mutable: Mảng tạo ra có thể thay đổi
def _bytearray():
    arr = bytearray(text, encoding='utf8')
    print(list(arr))


# Immutable: Mảng tạo ra không thể thay đổi
def _bytes_encode():
    arr1 = text.encode('utf-8')
    arr2 = bytes(text, encoding='utf-8')
    print(list(arr1))
    print(list(arr2))


def _other():
    arr = b'Hello, world!'
    print(list(arr))


if __name__ == '__main__':
    # _bytearray()
    # _bytes_encode()
    _other()
