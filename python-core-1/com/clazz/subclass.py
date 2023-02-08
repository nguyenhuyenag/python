from com.clazz.superclass import SuperClass


class SubClass(SuperClass):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call_super_constructor(self):
        super().__init__()
        
    def printInfo(self):
        print("Name: %s, age: %d" % (self.name, self.age))

    def hello(self, name):
        print("Sub class hello %s" % name)

        
def main():
    s = SubClass("Python", 1995)
    s.printInfo()
    s.call_super_constructor()
    s.hello("SubClass")

    
if __name__ == "__main__":
    main()
