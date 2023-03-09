from typing import Final

MAX_VALUE: Final[int] = 99

# This executes fine, but mypy will report an error if mypy is applied:
MAX_VALUE = 100
