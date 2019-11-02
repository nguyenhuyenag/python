import math


class PTB2():
    def __init__(self, _a, _b, _c):
        self.a = _a
        self.b = _b
        self.c = _c

    def GiaiPT(self):
        delta = math.pow(self.b, 2) - 4 * self.a * self.c
        if delta < 0:
            print("PT vo nghiem")
        elif delta == 0:
            print("PT co nghiem kep: x1 = x2 = ", -self.b / (2*self.a))
        else:
            print("PT co 2 nghiem phan biet")
            print("x1 = ", (-self.b - math.sqrt(delta)) / (2*self.a))
            print("x2 = ", (-self.b + math.sqrt(delta)) / (2*self.a))

pt = PTB2(3, 5, 2)
#print(pt.GiaiPT())

if hasattr(pt, "b"):
    print(getattr(pt, "b"))
    setattr(pt, "b", 100)
    print(getattr(pt, "b"))