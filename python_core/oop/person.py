class Person:
    # The __init__() function is called automatically every time the class is being used to create a new object
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # ~ toString() method
    def __str__(self):
        return f"{self.name}({self.age})"

    # Có thể thay đổi tên của `self` thành tên bất kỳ nhưng phải là tham số đầu tiên của hàm
    def sayHello(this):
        return f"Hello {this.name}"

p1 = Person("Python", 1995)

print(p1)

# Modify object properties
p1.name = "Java"

print(p1.sayHello())
