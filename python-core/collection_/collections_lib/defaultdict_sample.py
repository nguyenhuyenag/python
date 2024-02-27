import collections
from collections import defaultdict

"""
- Default dictionary: Khi truy cập một khóa chưa tồn tại, nó sẽ tự động thêm khóa đó vào từ điển 
và thiết lập giá trị mặc định là 0 (hoặc giá trị được chỉ định khi bạn tạo defaultdict):

    my_dict = defaultdict(int)
    
    my_dict['a'] += 1
    my_dict['b'] += 2
    
    # Không cần kiểm tra khóa tồn tại trước khi thay đổi giá trị
    my_dict['c']  # Giá trị mặc định là 0, không cần phải thêm 'c' vào trước đó
    
    print(my_dict)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 0})
"""


def normal():
    arr = 'abdacvcdcscbcbgnmnnb'
    counts = {}
    for key in list(arr):
        if key not in counts:
            counts[key] = 1
        else:
            counts[key] += 1

    print(counts)


def using_defaultdict():
    arr = 'abdacvcdcscbcbgnmnnb'
    counts = collections.defaultdict(lambda: 0)
    for key in arr:
        counts[key] += 1

    print(counts.items())


normal()
using_defaultdict()
