str = "I love apples, apple are MY favorite fruit."

# First latter uppercase
print(str.capitalize())

# Return the number of times the value S appears in the string
print("Count:", str.count("apple"))

print("Endswith:", str.endswith("."))

# The 'find()' method is almost the same as the 'index()' method, the only difference is that the 'index()' method
# raises an exception if the value is not found
str = "Mi casa, su casa";
print("Index:", str.index("casa"))
print("RIndex:", str.rindex("casa"))
print("Find:", str.find("casa"))
print("RFind:", str.rfind("casa"))

# Check if all the characters in the text are digits
print("IsDigit:", "abc".isdigit())
print("IsDigit:", "123456".isdigit())
print("IsNumeric:", "123456".isnumeric())

print("IsAlpha:", "abc".isalpha())
print("IsAlpha:", "abc123".isalpha())

# Alpha OR numerical
print("IsAlNum:", "abc123".isalnum())

# Check if all the characters in the text are whitespaces:
print("IsSpace:", "   ".isspace())

# Join all items in a 'iterable', using a hash character as separator
dict = ["a", "b", "c"]
print("Join", "=====".join(dict))

# Trim a string: strip, lstrip, rstrip
txt = "     banana     "
print("of all fruits", txt.strip(), "is my favorite")

# Partition, cắt chuỗi thành 3 phần, rpartition() cắt từ vị trí cuối cùng
txt = "I could eat bananas all day, many bananas haha"
print(txt.partition("bananas"))
print(txt.rpartition("bananas"))

print("Zfill:", "abc".zfill(10))


