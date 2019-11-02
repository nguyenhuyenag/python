'''
Override lai nhung ham nay 
+ __add__
* __mul__
- __sub__
% __mod__
/ __truediv__
< __lt__
<=__le__
==__eq__
!=__ne__
> __gt__
>= __ge__
[index] __getitem__(self,index)
in __contains__(self,value)
len __len__
str __str__#in Object
'''

from abc import ABC, abstractmethod  # import khai bao lop ao


class VectorAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __add__(self):
        pass


class Vector(VectorAbstract):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "{a: %d, b: %d}" % (self.a, self.b)

    def __add__(self, object):
        return Vector(self.a+object.a, self.b+object.b)

    def __mul__(self, object):
        return Vector(self.a*object.a, self.b*object.b)

    def __sub__(self, object):
        return Vector(self.a-object.a, self.b-object.b)


vector1 = Vector(2, 4)
vector2 = Vector(5, 2)
#print (vector1)
print(vector1-vector2)
