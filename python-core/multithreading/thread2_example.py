from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


# mock task that will sleep for a moment
def work(sleep_time):
    sleep(sleep_time)


# create a thread pool
with ThreadPoolExecutor(1) as executor:
    # start a long running task
    _ = executor.submit(work, 1)
    # start a second task
    future = executor.submit(work, 0.1)
    print(f'running={future.running()}, cancelled={future.cancelled()}, done={future.done()}')
    # cancel the second task
    was_cancelled = future.cancel()
    print(f'Cancelled: {was_cancelled}')
    # wait for the second task to complete
    wait([future])
    print(f'running={future.running()}, cancelled={future.cancelled()}, done={future.done()}')
