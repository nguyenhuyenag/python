# For loop
a = ['cat', 'window', 'defenestrate']
for i in a:
    print(i, len(i))
  
# Không nên sửa đổi danh sách khi đang duyệt
for i in a[:]:  # Tạo ra bản sao
    if len(i) > 6:
        a.insert(0, 'mouse')
print(a)
  
# Hàm range(n) # 0 -> n-1
#     range(m, n) # m -> n-1
for i in range(len(a)):  # 0, 1, 2, 3
    print(i, a[i])

# Break & continue
# for-else: Xảy ra khi chạy hết vòng lặp
for n in range(2, 10):
    for i in range(2, n):
        if n % i == 0:
            print(n, ' = ', i, '*', int(n / i))
            break
    else:
        print(n, 'is a prime number')

"""
Các toán tử and, or, not có độ ưu tiên thấp hơn các toán tử so sánh, not có độ ưu tiên cao nhất và or thấp nhất, ví dụ

Ví dụ:    (A and not B or C)  <=>  (A and (not B)) or C

"""