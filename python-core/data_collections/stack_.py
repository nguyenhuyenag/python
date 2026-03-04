from queue import LifoQueue


# Sử dụng mảng như stack
def stack_as_list():
    stack = []

    # push
    stack.append(12)

    # peek()
    print(stack[-1])

    # pop()
    print(stack.pop())


def stack2():
    # Initializing a stack
    stack = LifoQueue()

    # qsize() show the number of elements
    # in the stack
    print(stack.qsize())

    # put() function to push
    # element in the stack
    stack.put('a')
    stack.put('b')
    stack.put('c')

    print("Full: ", stack.full())
    print("Size: ", stack.qsize())

    # get() function to pop
    # element from stack in
    # LIFO order
    print('\nElements popped from the stack')
    print(stack.get())
    print(stack.get())
    print(stack.get())

    print("\nEmpty: ", stack.empty())


if __name__ == '__main__':
    # stack_as_list()
    stack2()
