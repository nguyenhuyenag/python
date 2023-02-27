def findSum(arr):
    return sum(arr)


# Enumerate
def loop_by_enumerate(arr):
    for (i, v) in enumerate(arr, start=1):  # start default is 0
        print(i, v)


def loop_by_zip():
    a1 = [1, 2, 3, 4]
    a2 = ["a", "b", "c"]
    # for (v1,v2) in zip(a1,a2, strict=True): # -> ValueError
    for (v1, v2) in zip(a1, a2):
        print(v1, v2)


nums = [11, 52, 73, 94, 50]
# print("Sum:", findSum(nums))
loop_by_enumerate(nums)
# loop_by_zip()
