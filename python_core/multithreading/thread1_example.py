from concurrent.futures import ThreadPoolExecutor
import random, time


def worker(thread_name, a, b):
    print(f"Thread {thread_name}: ---------------------- Start")
    print(f"Thread {thread_name}: Calculator: {a}^{b}={a ** b}")
    time_sleep = random.choice([1, 2, 3, 4])
    print(f"Thread {thread_name}: Sleep {time_sleep} second...")
    time.sleep(time_sleep)
    print(f"Thread {thread_name}: ---------------------- Done")


if __name__ == '__main__':
    # create a thread pool with 2 threads
    # pools = ThreadPoolExecutor(max_workers=2)
    with ThreadPoolExecutor(max_workers=2) as pools:
        # create and submit worker to pool
        for i in range(1, 6):
            v1 = random.choice([1, 2, 3, 4, 5])
            v2 = random.choice([1, 2, 3, 4, 5])
            future = pools.submit(worker, i, v1, v2)
        # pools.shutdown(wait=True)  # wait for all tasks to complete
    print("Main thread continuing to run")
