# {'a': 1, 'b': 2}  ->  {'1': 'a', '2': 'b'}
def swap_key_and_value():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    new_dict = {v: k for k, v in my_dict.items()}
    my_inverted_dict = dict(map(reversed, my_dict.items()))
    print(new_dict)
    print(my_inverted_dict)


# Sort a dictionary by values¶
def sort_dict():
    data = {"a": 4, "e": 1, "b": 99, "d": 0, "c": 3}
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
    print(sorted_data)


if __name__ == '__main__':
    sort_dict()
    # swap_key_and_value()
