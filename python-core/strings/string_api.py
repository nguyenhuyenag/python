def capitalize():
    s = "I Love apples, Apple are MY Favorite fruit"
    # Viết hoa chữ cái đầu câu, còn lại viết thường
    print("capitalize: " + s.capitalize())
    # Viết hoa chữ cái đầu câi và mỗi chữ cái đầu tiên sau đấu cách
    print("title: " + s.title())


"""
    center(n, fillchar): Canh giữa chuỗi s và thêm những ký tự 2 bên để độ dài = n
"""
def center():
    s = "Hello"
    print(s.center(20, '*'))


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
    print("Find():", s.find("casa"))

    # index()
    print("Index():", s.index("casa"))
    print("Last index of():", s.rindex("casa"))
    print("Index from:", s.index("casa", 4))

    # print("Index:", s.)


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
def trim_a_string():
    txt = "           just                 "
    print("Python is", txt.strip(), "not funny")


# Partition, cắt chuỗi thành 3 phần
def partition():
    txt = "I could eat bananas all day many bananas haha"
    print(txt.partition("bananas"))


def zerofill():
    print("Zfill:", "new_one".zfill(10))


def swapcase():
    s = "aBC"
    print(s.swapcase())


"""
    casefold(): Viết thường chuỗi và loại bỏ dấu 
"""
def lower_casefold():
    s = "ß" # Tiếng đức
    # Chuyển đổi sang lowercase cơ bản
    print("lower: ", s.lower())
    # Áp dụng các quy tắc chuẩn hóa Unicode để loại bỏ các biến thể dấu và ký tự
    print("casefold: ", s.casefold())


if __name__ == '__main__':
    # count()
    # center()
    # capitalize()
    # find_index()
    # check_number_alpha()
    # join_string_array()
    # trim_a_string()
    # partition()
    # zerofill()
    # swapcase()
    lower_casefold()
