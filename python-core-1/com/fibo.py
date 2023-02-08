def fib(n):
    "Print a Fibonacci series up to n"
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()


print(fib)

# Gán 1 hàm
f = fib
f(100)


def fiboDynamic(n):
    a, b = 0, 1
    arr = []
    while b < n:
        arr.append(b)  # arr = arr + [b] 
        a, b = b, a + b
    return arr


f100 = fiboDynamic(100)
print(f100)


def ask_ok():
    while True:
        print('Do you really want to quit? ', end="")
        ok = input()
        if ok in ('y', 'ye', 'yes'):
            print("Yes")
            return
        if ok in ('n', 'no', 'nop', 'nope'):
            print("No")
            return

# ask_ok()


# def f(func, L=[]):
#     if L is None:
#         L = []
#     L.append(a)
#     return L


def fNone(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# print(f(func))
# print(f(func))
# print(f(func))


print(fNone(1))
print(fNone(2))
print(fNone(3))


def my_method():
    """
    this is python docs
    """


print(my_method.__doc__)
