import random
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def worker(thread_name, a, b, flag: bool):
    if flag:
        print(f"Thread {thread_name}: Start")
    cal = a ** b
    if flag:
        print(f"Thread {thread_name}: Calculator {a}^{b}={cal}")
    time_sleep = random.choice([1, 2, 3, 4])
    if flag:
        print(f"Thread {thread_name}: Sleep {time_sleep} second...")
    time.sleep(time_sleep)
    if flag:
        print(f"Thread {thread_name}: ----------------------> Done")
    return cal

def thread1_test():
    with ThreadPoolExecutor(max_workers=2) as pools:
        # create and submit worker to pool
        for i in range(1, 5):
            v1 = random.choice([1, 2, 3, 4, 5])
            v2 = random.choice([1, 2, 3, 4, 5])
            future = pools.submit(worker, i, v1, v2, True)
            print(future.result())

        pools.shutdown(wait=True)  # wait for all tasks to complete

def thread2_test():
    with ThreadPoolExecutor(max_workers=2) as pools:
        list_futures = []
        for i in range(1, 6):
            v1 = random.choice([i for i in range(50)])
            v2 = random.choice([i for i in range(50)])
            list_futures.append(pools.submit(worker, i, v1, v2, True))

        # Đóng/mở để thấy kết quả khác
        pools.shutdown(wait=True)

        for f in as_completed(list_futures):
            print(f.result())


if __name__ == '__main__':
    # thread1_test()
    thread2_test()
    print("Main thread continuing to run")
