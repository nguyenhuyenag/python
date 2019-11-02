# def fib(n):
#     if n >= 0 and n < 2:
#         return n
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#         print(dp)
#     return dp[n]

look_up = {0: 1, 1: 1}
def fib(n):
    if look_up.get(n) is None:
        look_up[n] = fib(n - 1) + fib(n - 2)
        print(look_up)
    return look_up[n]

n = int(input("n = "))
#print(fib(n))
print(fib(n))