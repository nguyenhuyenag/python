from oop.person import Person


class NhanVien(Person):
    def __init__(self, name, year):
        Person.__init__(self, name, year)

    """
        super(): Dùng để gọi đến các thuộc tính của lớp cha
    """
    def show(self):
        return super().show()


def check_subclass():
    # Kiểm tra xem lớp Dog có phải là lớp con của lớp Animal không
    result = issubclass(NhanVien, Person)
    print(result)  # Kết quả là True


def sample():
    nv = NhanVien("Mike", 2000)
    print(nv)
    # Static method
    print("isAdult:", Person.isAdult(19))


def _super():
    nv = NhanVien("Mike", 2000)
    nv.show()

"""
    vars(): Tạo dictionary từ một đối tượng
"""
def _vars():
    nv = NhanVien("Mike", 2000)
    v = vars(nv)
    print(v)


if __name__ == '__main__':
    # sample()
    # check_subclass()
    # _super()
    _vars()
