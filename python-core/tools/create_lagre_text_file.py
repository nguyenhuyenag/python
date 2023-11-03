import os
import random
import pathlib

import random
import string


# def create_file_with_size(filename, size_in_mb):
#     size_in_bytes = size_in_mb * 1024 * 1024  # MB to bytes
#     with open(filename, 'w') as file:
#         while file.tell() < size_in_bytes:
#             random_char = random.choice(string.ascii_letters + string.digits)
#             file.write(random_char)
#
#
# if __name__ == '__main__':
#     # filename = "random_text_file.txt"  # Tên của file bạn muốn tạo
#     filename = os.path.join(pathlib.Path.home(), 'Desktop', 'test', 'random_text_file.txt')
#     os.makedirs(os.path.dirname(filename), exist_ok=True)
#
#     size_in_mb = 10  # Dung lượng bạn muốn (VD: 10 MB)
#     create_file_with_size(filename, size_in_mb)
#     print(f"File '{filename}' đã được tạo có dung lượng {size_in_mb} MB.")

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

size = input('Please enter a numeric size (MB): ')
while not size.isnumeric():
    size = input('Please enter a numeric size (MB): ')

size = int(size)

my_name = os.path.join(pathlib.Path.home(), 'Desktop', 'test', 'output.txt')
os.makedirs(os.path.dirname(my_name), exist_ok=True)

with open(my_name, 'w') as file:
    for _ in range(size):
        file.write(''.join(random.choices(characters, k=1000000)))
    # file_size = os.path.getsize(my_name)

print('Done!')
