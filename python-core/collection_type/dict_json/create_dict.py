# Tạo một từ điển mới
my_dict1 = dict()
print(my_dict1)  # Output: {}

# Tạo một từ điển từ các cặp key-value được chuyển vào
my_dict2 = dict(name='John', age=25, city='New York')
print(my_dict2)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}

# Tạo một từ điển từ một iterable
iterable = [('name', 'Alice'), ('age', 30), ('city', 'London')]
my_dict3 = dict(iterable)
print(my_dict3)  # Output: {'name': 'Alice', 'age': 30, 'city': 'London'}
