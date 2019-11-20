# from com.module import fibo
# fibo.fib(1000)
# print(fibo.fib2(100))
# print(fibo.__name__)
# 
# fb = fibo.fib
# fb(100)

"Câu lệnh này nhập tất cả mọi tên trừ những tên bắt đầu bằng dấu gạch chân (_)."
# from com.module.fibo import *

from com.module.fibo import fib, fib2

# fib(100)
# print(fib2(100))

print(dir(fib))
print(dir(fib2))