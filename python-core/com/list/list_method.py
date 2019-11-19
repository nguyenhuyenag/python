a = [5, 7, 0, 5, 4, 3, 7]

# append(x) = a[len(a):] = [x]
a.append(3)

# extend(L) =  a[len(a):] = L
a.extend([4, 5])  

# insert(): Thêm phần tử vào vị trí chỉ định
a.insert(len(a), 6)

# Xóa phần tử, xóa phần tử đầu tiên nếu có các phần tử giống nhau
a.remove(5)

# pop(x): Xóa bỏ x khỏi danh sách, a.pop() sẽ xóa phần tử cuối cùng. Hàm trả về phần tử bị xóa
a.pop(0)

# index(): Trả về vị trí đầu tiên của phần tử
idx = a.index(5)

# count(x): Đếm số lần xuất hiện trong danh sách
count = a.count(0)

# sort()
a.sort()
print(a)

a.reverse()
print(a)
