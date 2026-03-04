"""
    Khởi tạo nhanh ma trận  n x n
"""


# Duyệt ma trận

def matrix():
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

def matrix_2():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Row")
    for row in matrix:
        print(row)

    print("Column")
    # > zip(*mat)  = Transposed matrix.
    # > *mat -> Unpacking list thành các phần tử riêng biệt.
    # > zip(*matrix) = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
    # > zip() nhận vào nhiều danh sách và bắt đầu ghép các phần
    #   tử có cùng vị trí với nhau thành từng nhóm (tuple)
    for col in zip(*matrix):
        print(col)


# matrix()
matrix_2()


