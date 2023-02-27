def create_dict():
    # zip() creates an iterable in Python 3
    numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
    print('numbers3 =', numbers3)


def merge_dict():
    x = {"age": 22}
    y = {"name": 'Green'}
    y.update(x)
    print("Merge by update(): ", y)

    y = {**x, **y}
    print("Merge by **: ", y)

    z = dict(x, **y)
    print("Merge by dict(): ", y)


def get_dict_value():
    di = {'age': 22, 'name': 'Green'}
    # print(di['class'])            # -> KeyError: 'class'
    # print(di.get('class'))        # -> None
    print(di.get('class', '0'))  # -> 0


def dict_api():
    thedict = {'age': 22, 'name': 'Green', "country": "US"}
    thedict.pop("age")          # remove the item with the specified key
    thedict["name"] = "Red"     # change value
    thedict.popitem()           # remove the last item
    # thedict.clear()           # remove dict
    print(thedict)

create_dict()
# merge_dict()
# get_dict_value()
# dict_api()
