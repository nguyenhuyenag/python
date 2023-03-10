from enum import Enum
from collections import namedtuple

Color = namedtuple('Color', ['value', 'displayString'])


class Colors(Enum):

    @property
    def displayString(self):
        return self.value.displayString

    yellow = Color(1, 'Yellow')
    green = Color(2, 'Green')


print(Colors.yellow.displayString)
