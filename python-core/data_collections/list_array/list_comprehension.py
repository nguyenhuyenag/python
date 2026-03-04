"""
    - Cú pháp
        the_list = [
            expression
            for item1 in iterable1
            for item2 in iterable2
        ]
"""


def list_comprehension_1():
    pairs = [
        (i, j)
        for i in range(2)
        for j in range(3)
    ]
    print(pairs)

def numSpecial() -> int:
    # Xem special_positions_in_binary_matrix.py
    mat = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    row_sum = [sum(row) for row in mat]
    col_sum = [sum(col) for col in zip(*mat)]

    return sum(
        mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1
        for i in range(len(mat))
        for j in range(len(mat[0]))
    )

# list_comprehension_1()
numSpecial()
