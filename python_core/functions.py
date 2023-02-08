def func1(*args):  # -> tuple
    print("Hello", args[2])


def func2(**kid):  # -> dict
    print("His last name is " + kid["lname"])


def func3(country="Norway"):
    print("I am from " + country)


func1("a", "b", "c")
func2(fname="Tobias", lname="Refsnes")
func3()
