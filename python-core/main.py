# def gcd(a,b):


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def reduce_fraction(f):
    a, b = f
    _gcd = gcd(a, b)
    if _gcd == 0:
        return f
    return (a / _gcd, b / _gcd)
