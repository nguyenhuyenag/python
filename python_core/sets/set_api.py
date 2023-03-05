def immutable_set():
    vowels = {'a', 'e', 'i', 'o', 'u'}
    fSet = frozenset(vowels)
    fSet.add('v')


def set_api():
    A = {1, 3, 5, 7, 9, 8}
    B = {2, 3, 5, 7, 11}
#
    A.discard(8)                    # Remove item

    A.pop()                         # Get and remove a random item, if set empty -> throws an error

    A.isdisjoint(B)                 # True if don't any common items, else False

    A.issubset(B)                   # True B contains A, else False
    A.issuperset(B)                 # True A contains B, else False

    # CÁC PHÉP TOÁN TRONG TẬP HỢP

    # Phép giao (hội)
    C = A.intersection(B)           # Find common items 2 set (Shorthand A & B)
    # A.intersection_update(B)      # A &= B
    print(C)

    # Phép hợp
    A.union(B)                      # A | B
    A.update(B)                     # A |= B

    # Phép trừ
    C = A.difference(B)             # A - B
    print("A - B = ", C)

    C = A.symmetric_difference(B)   # A ∪ B - (A ∩ B) Những phần tử không chung của 2 tập hợp
    print(C)

    # A.difference_update(B)          # Gán A = A - B
    # print(A)


# immutable_set()
set_api()
