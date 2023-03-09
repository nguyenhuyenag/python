import enum
from enum import Enum, auto, IntEnum


# auto() -> Auto assign the integer value to the values of enum class attributes
class Days(Enum):
    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'

Color = Enum('MyColor', [('RED', 3), ('GREEN', 5), ('BLUE', 4)])

# @enum.unique -> Đánh dấu class chỉ chứa nững giá trị duy nhất
class ResponseStatus(Enum):
    # in progress
    IN_PROGRESS = 1
    REQUESTING = 1
    PENDING = 1

    # success
    SUCCESS = 2
    OK = 2
    FULFILLED = 2

    # error
    ERROR = 3
    NOT_OK = 3
    REJECTED = 3


def todo():
    # print("Name:", Color.__name__)
    print(Days.__members__)
    # print(list(Color))
    # print(Color.RED.name, Color.RED.value)
    # print("Enum check:", Days.Mon in Days)
    # print(Numbers.ONE + Numbers.TWO == 3)
    print([(weekday.name, weekday.value) for weekday in Days])

def how_to_use():
    code = 'OK'
    if ResponseStatus[code] is ResponseStatus.SUCCESS:
        print('The request completed successfully')


# todo()
how_to_use()
