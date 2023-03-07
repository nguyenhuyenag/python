import concurrent.futures
import random
import time


def worker(thread_name, a, b):
    print(f"Thread {thread_name}: Start")
    print(f"Thread {thread_name}: Calculator: {a}^{b}={a ** b}")
    print(f"Thread {thread_name}: Sleep {thread_name} second...")
    time.sleep(thread_name)
    print(f"Thread {thread_name}: Done")


if __name__ == '__main__':
    # create a thread pool with 2 threads
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

    for i in range(1, 6):
        v1 = random.choice([1, 2, 3, 4, 5])
        v2 = random.choice([1, 2, 3, 4, 5])
        pool.submit(worker, i, v1, v2)

    pool.shutdown(wait=True)  # wait for all tasks to complete

    print("Main thread continuing to run")
