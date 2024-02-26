import csv
import inspect


def using_hasattr_callable():
    with open(__file__) as csv_file:
        print(__file__)
        reader = csv.reader(csv_file)
        if hasattr(csv, 'close') and callable(reader.close()):
            print('Yes')
        else:
            print('No')


# Using inspect
def get_methods(cls_):
    methods = inspect.getmembers(cls_, inspect.isfunction)
    return dict(methods)


# Example
class A(object):
    pass


class B(object):
    def foo(self):
        print('B')


# If you only have an object, you can use `cls_ = obj.__class__`
if 'foo' in get_methods(A):
    print('A has foo')

if 'foo' in get_methods(B):
    print('B has foo')
