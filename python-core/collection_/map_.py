from itertools import zip_longest

"""
    map(function, iterable, ...): Ánh xạ lên từng phần tử của 1 hay nhiều iterables
"""

"""
    Ví dụ 1: Ánh xạ một hàm lên từng phần tử của danh sách
"""
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print("Map 1: ", list(squared))  # Kết quả là [1, 4, 9, 16, 25]

"""
    Ví dụ 2: Ánh xạ hai hàm lên từng phần tử của hai danh sách
             Các phần tử thừa của đối tượng dài hơn sẽ được bỏ qua.
"""
list1 = [1, 2, 3]
list2 = [10, 20, 30, -1]
result = map(lambda x, y: x + y, list1, list2)
print("Map 2: ", list(result))  # Kết quả là [11, 22, 33]

"""
    Map theo list có độ dài lớn nhất, phần tử thiếu sẽ nhận giá trị mặc định 
"""
# print(list(zip_longest(list1, list2, fillvalue=0)))
result = map(lambda pair: pair[0] + pair[1], zip_longest(list1, list2, fillvalue=0))
print("Map 3: ", list(result))  # Kết quả là [11, 22, 33, 40]
