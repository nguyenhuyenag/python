import threading
import time


def print_cube(thread_name, num):
    time.sleep(2)
    print("{} -> Cube: {}".format(thread_name, num ** 3))


def print_square(thread_name, num):
    time.sleep(3)
    print("{} -> Square: {}".format(thread_name, num * num))


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=["Thread_1", 2])
    t2 = threading.Thread(target=print_cube, args=["Thread_2", 2])

    # starting thread 1
    t1.start()

    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()

    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
