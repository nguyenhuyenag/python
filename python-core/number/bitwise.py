"""
    from_bytes(): Chuyển mảng byte thành số nguyên dương
"""

"""
    Chuyển đổi decimal <=> binary
"""
def to_binary():
    n = 5
    # bin(n) = 0bxxx
    binary = format(17, 'b')
    binary = format(n, '032b')  # Convert integer to 32-bit binary string
    print("binary:", binary)
    print("decimal:", int(binary, 2))


"""
    Đếm bit '1' trong biểu diễn nhị phân của n
"""
def bit_count():
    n = 5
    print("binary:", format(n, 'b'))
    print("bit_count:", n.bit_count())
    print("bit_length:", n.bit_length())


if __name__ == '__main__':
    # to_binary()
    bit_count()
