"""
open(filename, mode)
    'r' chỉ được đọc,
    'w' chỉ được ghi (tập tin cùng tên đang có sẽ bị xóa),
    'a' mở tập tin để thêm vào cuối; mọi dữ liệu ghi vào tập tin sẽ được tự động thêm vào cuối
    'r+' mở tập tin để đọc và ghi.
    Mode mặc định là r
"""
f = open("data.txt", "r")
print(f)
for x in f:
    print(x.rst)