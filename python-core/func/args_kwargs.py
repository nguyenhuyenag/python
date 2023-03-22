"""
    *args         Non-Keyword Arguments
    **kwargs      Keyword Arguments
"""
def with_args(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


def with_kwargs(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


with_args('Hello', 'Welcome', 'to', 'GeeksforGeeks')
with_kwargs("Hi", first='Geeks', mid='for', last='Geeks')
