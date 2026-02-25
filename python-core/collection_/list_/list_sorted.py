"""
    Có 2 cách để sắp xếp:

        - arr.sort() -> Sắp xếp trực tiếp trên mảng, không có giá trị trả về.

        - sort_result = sorted(arr) -> Trả về bản sao của mảng đã được sắp xếp, mảng gốc không thay đôi.

        => sort() nhanh hơn sorted()

    Sort by length: list_.sort(key=len) = sorted(list_, key=len)
"""
from typing import List


def sort_in_place():
    the_list = [0, 4, 1, 3, 2]
    the_list.sort()
    # the_list.sort(reverse=True)
    print(the_list)


def sorted_test():
    the_list = [0, 4, 1, 3, 2]

    # Sort và trả về kết quả
    the_list_sorted = sorted(the_list)

    # Thay đổi giá trị mảng gốc
    the_list[0] = 9999

    # In ra kết quả
    print(the_list)
    print(the_list_sorted)

def sort_by_bits(arr: List[int]) -> List[int]:
    arr.sort(key=lambda x: (x.bit_count(), x))
    return arr

def sort_complex():
    the_list = [
        {"name": "Java", "year": 1991, "author": "James Gosling"},
        {"name": "Python", "year": 1991, "author": "Guido van Rossum"},
        {"name": "C", "year": 1972, "author": "Dennis Ritchie"},
        {"name": "C++", "year": 1985, "author": "Bjarne Stroustrup"},
    ]
    """
        Đảo ngược điều kiện so sánh:
            result.sort(key=lambda w: (-counter[w], w)) // Đảo ngược 1 tiêu chí
            result.sort(key=lambda w: (counter[w], w), reverse=True) // Đảo ngược toàn bộ
    """
    sorted_data = sorted(the_list, key=lambda x: (x['year'], x['name']))
    print(sorted_data)


# sort_in_place()
# sort_complex()
# sorted(student_objects, key=lambda student: student.age)   # sort by age
sorted_test()
