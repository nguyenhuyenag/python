"""
    *args           Non-Keyword Arguments
    **kwargs        Keyword Arguments
"""


def with_args(args, *argv):
    print("First argument :", args)
    for arg in argv:
        print("Next argument through *argv:", arg)


def with_kwargs(args, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# with_args('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# with_kwargs("Hi", first='Geeks', mid='for', last='Geeks')
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
