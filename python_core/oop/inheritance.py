from oop.person import Person


class NV(Person):
    def __init__(self, name, year):
        Person.__init__(self, name, year)


if __name__ == "__main__":
    nv = NV("Nike", 2000)
    print(nv)
    # Static method
    print("isAdult:", Person.isAdult(19))
