def myfunc(anotherfunc, extraArgs):
    print(callable(anotherfunc))
    anotherfunc(*extraArgs)

def cal_pow(a, b):
    return a ** b

def cal_sum(a, b):
    return a + b

def calculator(caltype, args):
    print(caltype.__name__)     # get function name
    return caltype(*args)

if __name__ == '__main__':
    print(calculator(cal_sum, [2, 3]))
    print(calculator(cal_pow, [2, 3]))
