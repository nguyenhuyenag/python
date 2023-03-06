"""
    :type arr: List[int]
    :type k: int
    :rtype: int
    """


def findKthPositive(arr, k):
    i = 1
    count = 0;
    missing = []
    while count != k:
        if i not in arr:
            count = count + 1;
            missing.append(i)
        i = i + 1
    return missing[k - 1]


result = findKthPositive([2, 3, 4, 7, 11], 5)
result = findKthPositive([1, 2, 3, 4], 2)
result = findKthPositive([1], 1)
print(result)
