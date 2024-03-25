def basic():
    # Create set
    my_set = set()
    # my_set.add(123)

    # Create set like dictionary
    data = {}  # Nếu data đang rỗng -> AttributeError: 'dict' object has no attribute 'add'
    # data = {'a'}
    data.add('v')
    print(data)


def immutable_set():
    vowels = {'a', 'e', 'i', 'o', 'u'}
    fSet = frozenset(vowels)
    fSet.add('v')


def set_api():
    A = {1, 3, 5, 7, 9, 8}
    B = {2, 3, 5, 7, 11}

    A.discard(8)  # Remove item

    A.pop()  # Get and remove a random item, if set empty -> throws an error

    A.isdisjoint(B)  # Kiểm tra 2 set có phần tử chung không?

    A.issubset(B)  # True B contains A, else False
    A.issuperset(B)  # True A contains B, else False


"""
    Các phép toán trên tập hợp
"""


def set_operator():
    A = {1, 3, 5, 9, 8}
    B = {2, 3, 5, 11}
    print(f"A = {A}")
    print(f"B = {B}")

    # Phép hợp (gộp 2 set)
    C = A | B
    # A.union(B)  # A | B
    # A.update(B)  # A |= B
    print("Phép hợp: ", C)

    # Phép giao (tìm phần tử chung)
    C = A & B
    # C = A.intersection(B)  # Tạo ra set mới
    # A.intersection_update(B) # Tương đương với A &= B (thao tác trên set hiện tại)
    print("Phép giao: ", C)

    # Phép trừ
    # C = A.difference(B)  # A - B
    print(f"Phép trừ: A - B = {A - B}, B - A = {B - A}")
    # print("Phép trừ (B - A): ", B - A)

    # Những phần tử không chung của 2 tập hợp
    C = A.symmetric_difference(B)  # = A ∪ B - (A ∩ B)
    print(C)

    # A.difference_update(B)          # Gán A = A - B
    # print(A)


if __name__ == '__main__':
    basic()
    # immutable_set()
    # set_api()
    # set_operator()
