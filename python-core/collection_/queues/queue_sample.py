from queue import PriorityQueue

"""
    PriorityQueue(): Sử dụng class PriorityQueue để tạo queue
"""

def _queue():
    queue = PriorityQueue()

    for i in range(1, 5):
        queue.put(i)

    print("Size: ", queue.qsize())

    print("Queue -> List: ", queue.queue)

    """
        Không dùng `while queue:` vì sẽ bị loop infinity
    """
    while not queue.empty():
        print(queue.get(), end=" ")


def queue_object():
    queue = PriorityQueue()
    queue.put((2, "Harry"))
    queue.put((3, "Charles"))
    queue.put((1, "Riya"))
    queue.put((4, "Stacy"))

    while not queue.empty():
        print(queue.get())


if __name__ == '__main__':
    _queue()
    # queue_object()
