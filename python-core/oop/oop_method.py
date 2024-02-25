class MyClass:
    class_variable = 10

    def __init__(self):
        self.attribute1 = 42
        self.attribute2 = "Hello"

    """
        cls: Tham chiếu đến class chứa phương thức đó (dùng để truy cập các biến,...)
        self: Tham chiếu đến instance của class
    """
    @classmethod
    def print_class_variable(cls):
        print("I'm a classmethod & class_variable = ", cls.class_variable)


"""
    @classmethod: Dùng để truy cập trực tiếp một phương thức mà không cần thông qua instance
"""
def print_class_variable():
    MyClass.print_class_variable()  # Gọi trực tiếp từ lớp


"""
    delattr(): Dùng để xóa thuộc tính của class
"""
def del_attr():
    obj = MyClass()
    print("Before deletion:", obj.__dict__)
    # Xóa thuộc tính 'attribute1' của đối tượng 'obj'
    delattr(obj, 'attribute1')
    print("After deletion:", obj.__dict__)


if __name__ == '__main__':
    # print_class_variable()
    del_attr()