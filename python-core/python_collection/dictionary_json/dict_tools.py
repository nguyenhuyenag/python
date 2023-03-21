# {'a': 1, 'b': 2}  ->  {'1': 'a', '2': 'b'}
def swap_key_and_value():
    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print({v: k for k, v in dic.items()})

# Sort a dictionary by values¶
def sort_dict():
    data = {"a": 4, "e": 1, "b": 99, "d": 0, "c": 3}
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
    print(sorted_data)


# swap_key_and_value()
sort_dict()