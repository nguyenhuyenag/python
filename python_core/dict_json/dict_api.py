def create_dict():
    # zip() creates an iterable in Python 3
    numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
    print('numbers3 =', numbers3)


def fromkeys():
    keys = {'a', 'e', 'i', 'o', 'u'}
    value = [1]
    vowels = dict.fromkeys(keys, value)
    print(vowels)
    value.append(2)
    print(vowels)


def merge_dict():
    x = {"age": 22}
    y = {"name": 'Green'}
    y.update(x)
    print("Merge by update(): ", y)

    y = {**x, **y}
    print("Merge by **: ", y)

    z = dict(x, **y)
    print("Merge by dict(): ", y)

    # z = x | z         # ->    python 3.9+
    # print(z)


def get_dict_value():
    di = {'age': 22, 'name': 'Green'}
    # print(di['class'])            # -> KeyError: 'class'
    # print(di.get('class'))        # -> None
    print(di.get('class', '0'))     # -> 0


def dict_api():
    dic = {'age': 17, 'name': 'Green', "country": "US", "job": "Student"}

    dic.pop("age")                  # Remove the item with the specified key
    dic.popitem()                   # Remove the last item

    dic["name"] = "Red"             # Change value
    dic.setdefault("name", "Red")   # None is default

    dic.keys()                  # Return the list of keys as a view object
    dic.items()                 # Return list of (key, value). If list is updated, items will change (view object)

    # dic.copy()                    # Shallow copy
    # dict.clear()                  # Delete dict
    print(dic)


# create_dict()
fromkeys()
# merge_dict()
# get_dict_value()
# dict_api()
