"""
                +----+----+----+----+----+----+
                | P  | y  | t  | h  | o  | n  |
                +----+----+----+----+----+----+
Slice position: 0    1    2    3    4    5    6
Index position:    0   1   2   3   4   5
                  -6  -5   -4   -3   -2   -1

    A[:]                      A copy of the whole array
    A[start:]                 A[start], A[start+1], ...
    A[:stop]                  A[0], A[1],               ..., A[stop-1]
    A[start:stop]             A[start], A[start+1],     ..., A[stop-1]
    A[::step]                 A[0], A[step],            ..., A[-1]
    A[start::step]            A[start], A[start+step],  ..., A[-1]
    A[:stop:step]             A[0], A[step],            ..., A[stop-1]
    A[start:stop:step]        A[start], A[start+step],  ..., A[stop-1]
    A[::-step]                A[-1], A[-1-step],        ..., A[0]
    A[stop::-step]            A[stop], A[stop-step],    ..., A[0]
    A[:start:-step]           A[-1], A[-1-step],        ..., A[start+1]
    A[stop:start:-step]       A[stop], A[stop-step],    ..., A[start+1]

    slice(stop)
    slice(start, stop, step)

    Trong đó:

        start: Chỉ mục (index) bắt đầu của phần được cắt (không bắt buộc).
        stop: Chỉ mục kết thúc của phần được cắt.
        step: Bước (step) giữa các chỉ mục của phần được cắt (không bắt buộc).

    A[start:stop:step] = A[slice(start, stop, step)]
"""
A = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(len(A))
print(A[2:8:-1])


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Tạo một đối tượng slice
my_slice = slice(2, 8, 2)
# Sử dụng đối tượng slice để lấy một phần của list
result = my_list[my_slice]
print(result)  # Output: [2, 4, 6]
