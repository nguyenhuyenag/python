def find_sum(arr):
    return sum(arr)


"""
    enumerate(): Liệt kê các phần tử của một iterable cùng với chỉ số của chúng.
                 Hàm trả về một đối tượng enumerate, mỗi phần tử của nó là một tuple 
                 chứa một chỉ số và giá trị tương ứng từ iterable.
"""
def loop_by_enumerate(arr):
    for (i, v) in enumerate(arr, start=1):  # start default is 0
        print(i, v)


def loop_by_zip():
    a1 = [1, 2, 3, 4]
    a2 = ["a", "b", "c"]
    # for (v1,v2) in zip(a1, a2, strict=True): # -> ValueError
    for (v1, v2) in zip(a1, a2):
        print(v1, v2)


nums = [11, 52, 73, 94, 50]
# print("Sum:", findSum(nums))
loop_by_enumerate(nums)
# loop_by_zip()
