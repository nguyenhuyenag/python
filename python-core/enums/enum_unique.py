import enum
from enum import Enum


# @verify(UNIQUE)     # python 3.11+
@enum.unique          # -> Đánh dấu class chỉ chứa những giá trị duy nhất
class IntDays(Enum):
    SUN = 1
    MON = 1  # Duplicate values found
    TUE = 3
    WED = 4
    THU = 5
    FRI = 6
    SAT = 7
