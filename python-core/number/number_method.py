""""
    Number methods
"""

"""
    min, max: Tìm min, max của một tập hợp
"""


def min_max():
    print("min(3,5): ", min(3, 5))
    numbers = [3, 1, 4, 1, 5]
    print(f"min({numbers}): ", min(numbers))  # Kết quả là 1

    strings = ["apple", "banana", "kiwi", "orange", "Orange", "pear"]
    # So sánh theo nhiều tiêu chí: key=lambda x: (len(x), x)
    max_by_length = max(strings, key=lambda x: (len(x), x))
    print("max by length: ", max_by_length)


if __name__ == '__main__':
    min_max()
