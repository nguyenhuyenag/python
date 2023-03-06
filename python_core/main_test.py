def minimalKSum(nums, k):
    missing = []
    i, count = 1, 0
    while count != k:
        if i not in nums:
            missing.append(i)
            count = count + 1;
        i = i + 1
    return sum(missing)


if __name__ == '__main__':
    # result = minimalKSum([1, 4, 25, 10, 25], 2)
    result = minimalKSum([5, 6], 6)
    print(result)
