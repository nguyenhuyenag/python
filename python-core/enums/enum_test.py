from enum import Enum, auto, IntEnum


# auto() -> Auto assign the integer value to the values of enum class attributes
class Days(Enum):
    Sun = 1
    Mon = 2
    Tue = 3
    Wed = auto()
    Thu = auto()
    Fri = auto()
    Sat = auto()

Color = Enum('MyColor', [('RED', 3), ('GREEN', 5), ('BLUE', 4)])

class Numbers(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


def todo():
    # print("Name:", Color.__name__)
    # print(list(Color))
    # print(Color.RED.name, Color.RED.value)
    print(Numbers.ONE + Numbers.TWO == 3)
    for weekday in Days:
        print(weekday.name, weekday.value)


todo()

