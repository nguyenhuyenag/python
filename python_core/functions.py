def func1(*args):  # -> tuple
    print("Hello", args[2])


def func2(**kid):  # -> dict
    print("His last name is " + kid["name"])


def func3(country="Norway"):
    print("I am from " + country)


func1("a", "b", "c")
func2(name="Tobias", age=25)
func3()
