import time
import concurrent.futures


def worker(alist, name):
    print(f"Thread {name}")
    return sum([i ** i for i in alist])

def split(alist, sub_list):
    splitted = []
    for i in reversed(range(1, sub_list + 1)):
        split_point = len(alist) // i
        splitted.append(alist[:split_point])
        alist = alist[split_point:]

    return splitted

def thread_test():
    arr = [i for i in range(100)]
    arr = split(arr, 5)
    # print(arr)
    # return
    threaded_start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i, v in enumerate(arr):
            futures.append(executor.submit(worker, v, i))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("Threaded time:", time.time() - threaded_start)


if __name__ == '__main__':
    thread_test()

