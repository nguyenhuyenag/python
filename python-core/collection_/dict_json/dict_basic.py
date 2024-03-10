# Tạo một từ điển mới
from oop.inheritance import NhanVien


def create_dict():
    # zip() creates an iterable in Python 3
    numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
    print('numbers3 =', numbers3)


# Tạo dict từ set và 1 list
def fromkeys():
    keys = {'a', 'b', 'c'}
    value = [1]
    vowels = dict.fromkeys(keys, value)
    print(vowels)
    value.append(2)
    print(vowels)


# Gộp 2 dict
def merge_dict():
    x = {"age": 22}
    y = {"name": 'Green'}
    y.update(x)
    print("Merge by update(): ", y)

    y = {**x, **y}
    print("Merge by **: ", y)

    z = dict(x, **y)
    print("Merge by dict(): ", y)

    # z = x | z         #   python 3.9+
    # print(z)


# Get giá trị
def get_value():
    di = {'age': 22, 'name': 'Green'}
    # print(di['class'])            #   KeyError: 'class'
    # print(di.get('class'))        #   Default is None
    print(di.get('class', '0'))  # Default is 0


# Duyệt dict
def keys_and_values():
    dic = {'a': 1, 'b': 2, 'c': 3}

    for k, v in dic.items():
        print(k, v)

    print("Or")

    for k, v in zip(dic.keys(), dic.values()):
        print(k, v)


def dict_api():
    dic = {'age': 17, 'name': 'Green', "country": "US", "job": "Student"}

    dic.pop("age")  # Remove the item with the specified key
    dic.popitem()  # Remove the last item

    dic["name"] = "Red"  # Change value
    dic.setdefault("name", "Red")  # None is default

    dic.keys()  # Return the list_ of keys as a view object
    dic.items()  # Return list_ of (key, value). If list_ is updated, items will change (view object)

    # dic.copy()                    # Shallow copy
    # dict.clear()                  # Delete dict
    print(dic)


if __name__ == '__main__':
    # create_dict()
    # fromkeys()
    # merge_dict()
    # get_dict_value()
    # dict_api()
    keys_and_values()

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
