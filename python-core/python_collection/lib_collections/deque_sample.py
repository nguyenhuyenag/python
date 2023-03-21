from collections import deque


# Hàng đợi 2 đầu
def method_name():
    d = deque(['Black', 'White', 'Red', 'Green'])
    print(d)

    # Add elements to the right side
    d.append('Blue')

    # Add elements to the left side
    d.appendleft('Yellow')

    # Remove elements from the right side
    d.pop()

    # Remove elements from the left side
    d.popleft()

    # Get the size of the deque
    len(d)


method_name()
