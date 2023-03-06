"""
    Câu lệnh yield sẽ đình chỉ việc thực thi của hàm và trả về một giá trị cho caller – đối tượng gọi hàm,
    nhưng vẫn giữ lại đầy đủ trạng thái của hàm để ngay sau khi thực thi xong câu lệnh yield, hàm vẫn có
    thể quay lại thực thi tiếp được tại câu lệnh tiếp theo nằm ngay sau câu lệnh yield vừa chạy xong.
    Điều này cho phép một hàm có thể trả về một loạt các giá trị theo thời gian, thay vì phải tính toán
    cùng một lúc ra nhiều outputs rồi đưa tất cả chúng vào trong một list (danh sách) và trả về duy nhất list đó
"""


def simple_generator():
    yield 1
    yield 2
    yield 3

# # Driver code to check above generator function
# for value in simple_generator():
#     print(value)

### Generators created using yield keyword
def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

# Driver code to check above generator function
for number in fibonacci_series(10):
    print(number)




