# Converts the first character of a string_character to an uppercase letter and all other alphabets to lowercase
def capitalize():
    s = "I Love apples, Apple are MY Favorite fruit"
    print(s.capitalize())


# Return the number of times the value S appears in the string_character
def count():
    s = "I Love apples, apple are MY Favorite fruit"
    print("Count 'apple' -> ", s.count("apple"))


# find() ~ index(), the only difference is that the 'index()' method raises an exception if not found
def find_and_index():
    s = "Mi casa, su casa";
    print("Index:", s.index("casa"))
    print("Find:", s.find("casa"))


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


# Trim a string_character
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


# count()
# capitalize()
# find_and_index()
# check_number_alpha()
# join_string_array()
# trim_a_string()
# partition()
# zerofill()
swapcase()
