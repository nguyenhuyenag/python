import math
import abc
from abc import abstractmethod
# metaclass=abc.ABCMeta):


class Shape(abc.ABC):
    @abstractmethod
    def find_Area(self):
        pass

    @abstractmethod
    def find_P(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def find_Area(self):
        print('Area= ', math.pi*math.pow(self.r, 2))

    def find_P(self):
        print('Area=', math.pi*math.pow(self.r, 2))


if __name__ == "__main__":
    c = Circle(5)
    c.find_Area()
