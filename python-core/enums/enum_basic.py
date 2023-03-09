import enum
from enum import Enum, auto, IntEnum

Color = Enum('MyColor', [('RED', 3), ('GREEN', 5), ('BLUE', 4)])

class Days(Enum):
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'


def enum_api():
    # print("Name:", Color.__name__)
    print(Days.__members__)
    # print(list(Color))
    # print(Color.RED.name, Color.RED.value)
    # print("Enum check:", Days.Mon in Days)
    # print(Numbers.ONE + Numbers.TWO == 3)
    print([(weekday.name, weekday.value) for weekday in Days])


enum_api()