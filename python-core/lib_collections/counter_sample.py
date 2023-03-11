from collections import Counter

arr = 'lalalalandismagic'
# arr = ['d', 'a', 'c', 'a', 'e', 'b', 'c', 'c', 'b', 'd']

string_count = Counter(arr)
# Tính toán tần suất xuất hiện của các phần tử
print(sorted(string_count.elements()))

print(string_count)
print("Xuất hiện nhiều nhất: ", string_count.most_common(1))
print("Xuất hiện nhiều hai: ", string_count.most_common(2))
# print(string_count.most_common(2))


# counter with strings
# string_count = Counter(string)
# print(string_count)
