from dataclasses import dataclass, astuple, asdict


class Student:
    def __init__(self, id, name):
        # Instance variables
        self.id = id
        self.name = name

    def __repr__(self):
        return "Student Info: id={}, name={}".format(self.id, self.name)


@dataclass
class StudentWithDataClass:
    id: int
    name: str = "John"


std = Student(22, "Paul")
print(std)

student = StudentWithDataClass(22, "Paul")
print(student)

# Conversion to a tuple or a dictionary
print("Tuple:", astuple(student))
print("Dictionary:", asdict(student))
