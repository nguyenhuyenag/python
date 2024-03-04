from typing import Self # Python 3.11+

class MethodChainingExample:
    def __init__(self) -> None:
        self.value = 0

    def add(self, num: int) -> Self:
        self.value += num
        return self

    def multiply(self, num: int) -> Self:
        self.value *= num
        return self

    def subtract(self, num: int) -> Self:
        self.value -= num
        return self

# Creating an instance of MethodChainingExample
method_chaining_example = MethodChainingExample()

# Method chaining example
result = method_chaining_example.add(5).multiply(3).subtract(2)

print(result.value)  # Output: 13
