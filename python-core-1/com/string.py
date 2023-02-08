s = 'Help' + 'A'

print("Length:", len(s))

print(5 * s)  # Nhân 5 lần chuỗi s

print('a' 'b')  # Hai chuỗi đặt kế tiếp nhau sẽ tự động nối lại
print("a""b")  # Hai chuỗi đặt kế tiếp nhau sẽ tự động nối lại

print(s[4])
print(s[0:])
print(s[:1])
print(s[0:5])

# immutable
# s[0] = 'x' => error

print(s[:2] + s[2:])  # In ra chuỗi s

print(s[0:12])

print(s[1:0])  # Trả về chuỗi rỗng

# Các chỉ mục có thể là số âm
print(s[-1])  # The last character

print(s[-2])  # The last-but-one character

#  +---+---+---+---+---+ 
#  | H | e | l | p | A |
#  +---+---+---+---+---+ 
#  0   1   2   3   4   5 
# -5  -4  -3  -2  -1
