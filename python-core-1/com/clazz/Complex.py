class Complex:

    def __init__(self, realpart, imagpart):  #
        self.r = realpart  # 
        self.i = imagpart


z = Complex(2, 3)
print(z.i)


class Bag:

    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
