class MyClass:
    "This is document"
    
    def __init__(self):
        self.data = []
    
    i = 12345

    def f(self):
        return "This is method"

# print(MyClass.__doc__)
# print(MyClass.i)
# print(MyClass.f)

# class intance
x = MyClass()
print(x.i)
print(x.f())