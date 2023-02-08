a = ['spam', 'eggs', 100, 1234]

print(len(a))

# Chỉ mục danh sách bắt đầu từ 0, có thể được cắt lát, gộm, ... giống như chuỗi
print(2 * a)

print(*a)

print(a[:])  # In ra chính nó

# Tuy nhiên danh sách là mutable 
a[0] = 0
print(a)

a[0:2] = [1, 12]  # Thay thế 1 số phần tử
print(a)

a[0:2] = []  # Xóa
print(a)

a[0:0] = ["A"]  # Chèn
print(a)

a[:0] = a  # Chèn danh sách vào danh sách
print(a)

a[:] = []  # Xóa toàn bộ sanh sách
print(a)

# Lệnh DEL
a = [1, 2, 3]
del a[0]  # Xóa dữa vào index
del a[2:4]  # Xóa khoảng
del a[:]  # Xóa tất cả
del a  # Xóa luôn biến sanh sách
# print(a)

# Lồng danh sách vào sanh sách khác
p = [1, 2, 3]
q = [p, 4, 5]
 
print(q)
p.append(6)
 
print(q)
 
x = [1]
print(x + [2])

# Loop
s = ['tic', 'tac', 'toe']
for i, v in enumerate(s):
    print(i, v)
    
# Lặp nhiều sanh sách với zip()
for a, b in zip([0, 1, 2], s):
    print(a, b)

# 
for i in reversed(range(1, 10, 2)):
    print(i)

# 
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)): # basket không bị thay đổi
    print(f)
