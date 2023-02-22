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
    print(di.get('class', '0'))     # -> 0


# merge_dict()
get_dict_value()
