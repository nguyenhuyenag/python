def example_function(x):
    y = x * 2
    breakpoint()  # Điểm chấm dừng ở đây
    z = y + 3
    return z


result = example_function(5)
print(result)
