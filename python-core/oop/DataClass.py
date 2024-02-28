from dataclasses import dataclass, astuple, asdict


class Student:
    def __init__(self, id, name):
        # Instance variables
        self.id = id
        self.name = name

    def __str__(self):
        return "Student: id={}, name={}".format(self.id, self.name)


@dataclass
class StudentWithDataClass:
    id: int
    name: str = "John"


if __name__ == '__main__':
    std = Student(22, "Paul")
    print(std)

    student = StudentWithDataClass(22, "Paul")
    print(student)

    # Conversion to a tuple or a dictionary
    print("Tuple:", astuple(student))
    print("Dictionary:", asdict(student))

    # Get value
    value = getattr(student, "name", None)
    print("Get by getattr", value)

    # getattr() với giá trị mặc định cho thuộc tính không tồn tại
    value = getattr(student, "my_name", None)
    print("Get by getattr:", value)

    setattr(student, "id", 2024)
    print("New value: ", student.id)
