from itertools import permutations

"""
    Tạo ra tất cả các hoán vị (permutations) có độ dài r từ một iterable cho trước.
    Mỗi một kết qủa là một tupple
"""

# p[collection, r]: r-length tuples, all possible orderings, no repeated elements
def base():
    for v in permutations("ABC", 2):
        print(v, end=" ")

def print_all():
    print("All the permutations of the given container is:")
    arr = [1, 2, 3]
    for i in range(1, len(arr) + 1):
        print(list(permutations(arr, i)))

base()
# print_all()


