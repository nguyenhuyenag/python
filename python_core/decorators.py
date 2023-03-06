"""
    Decorators are a way to modify the behavior of a function or a class. They are defined using the @ symbol and can be used to add functionality to a function, such as logging, timing, or authentication
"""


def log_function(func):
    def wrapper(*args, **kwargs):
        print(f'Running {func.__name__} function')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result

    return wrapper


@log_function
def add(x, y):
    return x + y


print(add(5, 7))
