"""
    - Là một phiên bản nâng cao của tuple. Hoặc như một cách nhanh chóng để tạo một lớp python với các thuộc tính được đặt tên nhất định.

Một điểm khác biệt chính giữa tuple và tuple có tên là: trong khi tuple cho phép bạn truy cập dữ liệu thông qua các chỉ mục, thì với tuple có tên, bạn có thể truy cập các phần tử bằng tên của chúng.

Bạn thực sự có thể xác định tất cả các thuộc tính mà một bộ có tên có thể chứa và tạo nhiều phiên bản của nó. Cũng giống như cách bạn sẽ làm với các lớp học.

Vì vậy, về mặt chức năng, nó giống với một lớp hơn, mặc dù nó có bộ trong tên của nó.
"""
# Creating a namedtuple.

from collections import namedtuple

movie = namedtuple('movie', 'genre rating lead_actor')

# Create instances of movie
ironman = movie(genre='action', rating=8.5, lead_actor='robert downey junior')
titanic = movie(genre='romance', rating=8, lead_actor='leonardo dicaprio')
seven = movie(genre='crime', rating=9, lead_actor='Brad Pitt')

# Access the fields
print(titanic.genre)
print(seven.lead_actor)
print(ironman.rating)