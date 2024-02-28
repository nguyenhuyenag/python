from datetime import datetime

"""
Class method và Static method

    – Class method nhận vào cls làm tham số đầu tiên, trong khi static method không cần tới tham số đặc biệt nào.

    – Class method có thể truy cập hoặc sửa đổi trạng thái của class, trong khi static method không thể truy cập tới
    hay sửa đổi nó.

    – Nói chung, static method không biết gì về trạng thái của class. Chúng là những method – phương thức thuộc kiểu
    tiện ích, nhận vào một số tham số và làm việc trên các tham số đó. Mặt khác, class method phải có được một class
    làm tham số truyền vào cho nó.

    – Chúng ta sử dụng các decorator @classmethod trong Python để tạo ra một class method (phương thức/hàm thuộc về lớp)
    và sử dụng decorator @staticmethod để tạo ra một static method (phương thức/hàm tĩnh) trong Python.
"""
class Person:
    # The __init__() function is called automatically every time the class is being used to create a new object
    # Có thể đổi tên `self` thành tên bất kỳ nhưng phải là tham số đầu tiên của hàm
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def show(self):
        print(locals())

    # ~ toString() method
    def __str__(self):
        return f"[name={self.name}, year={self.year}]"

    # A class method to create a Person object by birth year
    @classmethod
    def fromYear(cls, name, year):
        return cls(name, datetime.today().year - year)

    # A static method to check if a Person is adult or not
    @staticmethod
    def isAdult(age):
        return age > 18


if __name__ == '__main__':
    p1 = Person("Python", 1995)
    print(p1)
    # Modify object properties
    p1.name = "Java"
    print(p1)
