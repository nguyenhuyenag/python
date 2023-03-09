# import enum and IntEnum
from enum import Enum, auto

class Language(Enum):
    Python = 1
    Java = 2
    C = 3
    HTML = auto()
    JavaScript = 4

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])


for v in Language:
    print(v.name, v.value)
