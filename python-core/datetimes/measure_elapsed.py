import random
import time
from timeit import default_timer as timer


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


if __name__ == '__main__':
    # using_time()
    using_timer()
