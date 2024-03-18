def tower(n, a, b, c):
    if n == 1:
        print(f"{a} -----> {c}")
        return
    else:
        # Dùng c làm trung gian, di chuyển n - 1 đĩa từ a -> b
        tower(n - 1, a, c, b)
        # Cho đến khi chỉ còn 1 đĩa ở a, thì dời nó sang c
        tower(1, a, b, c)
        # Dùng a làm trung gian, dời n - 1 đĩa từ b sang c
        tower(n - 1, b, a, c)


if __name__ == '__main__':
    n = 3
    tower(n, 'A', 'B', 'C')
