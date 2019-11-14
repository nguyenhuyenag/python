import time


def f(n):
    if n < 2:
        return n
    return f(n-1)+f(n-2)


print(f(5))

start = time.process_time()
# code here
print(f(10))
# end code
end = time.process_time()
print(end - start)

a = True
print(type(a))
