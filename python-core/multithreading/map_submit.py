from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor, as_completed


def task(name):
    sleep(random())
    return name


def map_method():
    with ThreadPoolExecutor(10) as executor:
        # execute tasks concurrently and process results in order
        for result in executor.map(task, range(10)):
            print(result)


def submit_method():
    with ThreadPoolExecutor(10) as executor:
        # submit tasks and collect futures
        futures = [executor.submit(task, i) for i in range(10)]
        # process task results as they are available
        for future in as_completed(futures):
            print(future.result())
