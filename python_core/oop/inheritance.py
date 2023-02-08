from oop.person import Person


class NV(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)


if __name__ == "__main__":
    nv = NV("Python", 1995)
    print(nv)
