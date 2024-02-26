from oop.person import Person


class NhanVien(Person):
    def __init__(self, name, year):
        Person.__init__(self, name, year)


def check_subclass():
    # Kiểm tra xem lớp Dog có phải là lớp con của lớp Animal không
    result = issubclass(NhanVien, Person)
    print(result)  # Kết quả là True


def sample():
    nv = NhanVien("Mike", 2000)
    print(nv)
    # Static method
    print("isAdult:", Person.isAdult(19))


if __name__ == '__main__':
    # sample()
    check_subclass()
