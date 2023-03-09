import time, random
from timeit import default_timer as timer


# Đo lường thời gian
def todo():
    time.sleep(random.choice([1, 2, 3]))


def using_time():
    start = time.time()
    todo()
    end = time.time()
    print("Time = ", end - start)


def using_timer():
    start = timer()
    todo()
    end = timer()
    print("Time =", end - start)


# Use a decorator
def timer_func_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = timer()
        result = func(*args, **kwargs)
        t2 = timer()
        print(f'{func.__name__}() executed in {(t2 - t1):.6f}s')
        return result

    return wrapper


@timer_func_decorator
def do_something():
    for i in range(1000000):
        i * i


if __name__ == '__main__':
    # using_time()
    # using_timer()
    do_something()
