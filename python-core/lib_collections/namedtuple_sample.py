"""
    - Là một phiên bản nâng cao của tuple cho phép nhanh chóng để tạo một class.

    - Một điểm khác biệt là tuple cho phép truy cập dữ liệu thông qua các chỉ mục, còn namedtuple là bằng tên của chúng.
"""
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
