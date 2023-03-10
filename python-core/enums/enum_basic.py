from enum import Enum, auto

Color = Enum('MyColor', [('RED', 3), ('GREEN', 5), ('BLUE', 4)])


class IntDays(Enum):
    SUN = 1
    MON = 2
    TUE = 3
    WED = 4
    THU = 5
    FRI = 6
    SAT = auto()  # 7, Automatically assign the integer value


class Days(Enum):
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'


def enum_api():
    # Check contains & compare
    print("Compare (1):", Days['MON'] == Days.MON)
    print("Compare (2):", Days['MON'] is Days.MON)

    print("Check contains (1):", Days.MON in Days)
    print("Check contains (2):", Days['MON'] in Days)

    # DeprecationWarning
    # print("Check Enum contains:", Days.MON.name in Days)
    # print("Check Enum contains:", Days.MON.value in Days)

    print([(weekday.name, weekday.value) for weekday in Days])


enum_api()
