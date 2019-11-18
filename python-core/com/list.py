a = ['spam', 'eggs', 100, 1234]

print(len(a))

# Chỉ mục danh sách bắt đầu từ 0, có thể được cắt lát, gộm, ... giống như chuỗi
print(2 * a)

# Tuy nhiên danh sách là mutable 
a[0] = 0
print(a)

a[0:2] = [1, 12]  # Thay thế 1 số phần tử
print(a)

a[0:2] = []  # Xóa
print(a)

a[0:0] = ["A"]  # Chèn
print(a)

a[:0] = a  # Chèn sanh sách vào danh sách
print(a)

a[:] = []  # Xóa toàn bộ sanh sách
print(a)

# Lồng danh sách vào sanh sách khác
p = [1, 2, 3]
q = [p, 4, 5]

print(q)
p.append(6)

print(q)
