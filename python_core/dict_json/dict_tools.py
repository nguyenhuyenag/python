# {'a': 1, 'b': 2}  ->  {'1': 'a', '2': 'b'}
def inverting_dict():
    dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print({v: k for k, v in dic.items()})


inverting_dict()
