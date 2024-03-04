""""
    String methods
"""

"""
    - lower(), uppper(), swapcase()
    - islower(), isuppper()
    - split()
    - replace()
    - endswith()
    - encode(): String to bytes
    - isspace(): Kiểm tra chuỗi có phải là khoảng trắng (có thể 1 hoặc nhiều)
    - isprintable(): Kiểm tra chuỗi có in ra màn hình được không, ký tự không in ra màn hình 
                     là những ký tự như \t, \n
"""


def capitalize():
    s = "I Love apples, Apple are MY Favorite fruit"
    # Viết hoa chữ cái đầu câu, còn lại viết thường
    print("capitalize: " + s.capitalize())
    # Viết hoa chữ cái đầu câi và mỗi chữ cái đầu tiên sau đấu cách
    print("title: " + s.title())


"""
    center(n, fill_char): Canh giữa chuỗi s và thêm những ký tự 2 bên để độ dài = n
    ljust(n, fill_char): Tương tự nhưng chuỗi s ở bên trái
    rjust(n, fill_char): Tương tự nhưng chuỗi s ở bên phải
"""
def center_ljust():
    s = "Hello"
    n = 11
    print("center():", s.center(n, '*'))
    print("ljust():", s.ljust(n, '*'))
    print("rjust()", s.rjust(n, '*'))


# Return the number of times the value S appears in the strings
def count():
    s = "I Love apples, apple are MY Favorite fruit"
    print("Count 'apple' -> ", s.count("apple"))


"""
    string.index(value, start, end)
    find() ~ index(), the only difference is that the 'index()' -> raises an exception if not found
"""
def find_index():
    s = "Mi casa, su casa"

    # find()
    print("find():", s.find("casa"))
    print("rfind():", s.rfind("casa"))

    # index()
    print("index():", s.index("casa"))
    print("Last index of():", s.rindex("casa"))
    print("Index from:", s.index("casa", 4))


def check_number_alpha():
    # Check digits & numeric
    print("IsDigit: 'new_one' ->", "new_one".isdigit())
    print("IsDigit: '123456' ->", "123456".isdigit())
    print("IsNumeric: '123456' ->", "123456".isnumeric())

    # Check alpha
    print("IsAlpha: 'new_one' ->", "new_one".isalpha())
    print("IsAlpha: 'abc1234' ->", "abc123".isalpha())

    # Alpha OR numerical
    print("IsAlphaNumeric: 'abc123' ->", "abc123".isalnum())


# Join all items in a 'iterable', using a hash character as separator
def join_string_array():
    di = ["a", "b", "c"]
    print("{} -> {}".format(di, "*".join(di)))


# Trim a strings
def strip():
    s = "        just                "
    # Trim
    print("strip():", s.strip())
    # Left trim
    print("lstrip():", s.lstrip())
    # Right trim
    print("rstrip():", s.rstrip())


# Partition: Cắt chuỗi thành 3 phần (left, key, right)
def partition():
    s = "I could eat bananas all day many bananas haha"
    print(s.partition("bananas"))


def zerofill():
    print("Zfill:", "new_one".zfill(10))


# def swapcase():
#     s = "aBC"
#     print(s.swapcase())


"""
    casefold(): Viết thường chuỗi và loại bỏ dấu 
"""
def lower_casefold():
    s = "ß"  # Tiếng đức
    # Chuyển đổi sang lowercase cơ bản
    print("lower: ", s.lower())
    # Áp dụng các quy tắc chuẩn hóa Unicode để loại bỏ các biến thể dấu và ký tự
    print("casefold: ", s.casefold())


"""
    "separator".join(): Dùng separator để nối một iterable thành chuỗi
"""
def join():
    arr = ['a', 'b', 'c', 'd']
    print("join():", "*".join(arr))


"""
    - isalnum(): Chuỗi chỉ chứa ký tự chữ cái hoặc số
    - isdigit(): Chỉ chứ số
    - isalpha(): Chỉ chứa ký tự chữ cái
    - isdecimal() = is_all_digit (0-9)
    - isnumeric() = is_all_numeric
"""
def is_digit_letter():
    s1 = "Python3"
    print(s1.isalnum())  # True
    s2 = "Python 3"
    print(s2.isalnum())  # False
    "".isnumeric()


if __name__ == '__main__':
    # count()
    # center()
    # capitalize()
    # find_index()
    # check_number_alpha()
    # join_string_array()
    # trim_a_string()
    partition()
    # zerofill()
    # swapcase()
    # lower_casefold()
    # join()
    # is_digit_letter()
    # center_ljust()
    # strip()

