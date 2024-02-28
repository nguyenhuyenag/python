# Tạo một từ điển mới
from oop.inheritance import NhanVien

my_dict1 = dict()
print("Default: ", my_dict1)  # Output: {}

"""
    Tạo một từ điển từ các cặp key-value được chuyển vào
"""
my_dict2 = dict(name='John', age=25, city='New York')
print("From key-value: ", my_dict2)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}

"""
    Tạo một từ điển từ một iterable
"""
iterable = [('name', 'Alice'), ('age', 30), ('city', 'London')]
my_dict3 = dict(iterable)
print("From iterable: ", my_dict3)  # Output: {'name': 'Alice', 'age': 30, 'city': 'London'}

"""
    Tạo từ điển từ một đối tượng
"""
nv = NhanVien("Mike", 2000)
print("From Object 1: ", vars(nv))
print("From Object 2: ", nv.__dict__)
