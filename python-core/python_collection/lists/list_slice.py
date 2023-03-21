"""
                +----+----+----+----+----+----+
                | P  | y  | t  | h  | o  | n  |
                +----+----+----+----+----+----+
Slice position: 0    1    2    3    4    5    6
Index position:    0   1   2   3   4   5
                  -6  -5   -4   -3   -2   -1

    A[:]                      A copy of the whole array
    A[start:]                 A[start], A[start+1], ...
    A[:stop]                  A[0], A[1],          ..., A[stop-1]
    A[start:stop]             A[start], A[start+1],      ..., A[stop-1]
    A[::step]                 A[0], A[step],     ..., A[-1]
    A[start::step]            A[start], A[start+step], ..., A[-1]
    A[:stop:step]             A[0],   A[step],     ..., A[stop-1]
    A[start:stop:step]        A[start], A[start+step], ..., A[stop-1]
    A[::-step]                A[-1],   A[-1-step],   ..., A[0]
    A[stop::-step]            A[stop], A[stop-step], ..., A[0]
    A[:start:-step]           A[-1],   A[-1-step],   ..., A[start+1]
    A[stop:start:-step]       A[stop], A[stop-step], ..., A[start+1]

    slice(stop)
    slice(start, stop, step)

    A[start:stop:step] = A[slice(start, stop, step)]
"""
A = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(len(A))
print(A[2:8:-1])
