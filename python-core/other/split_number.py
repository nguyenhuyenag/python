def chia_so(number, set_of_numbers):
    if number == 0:
        return []
    for num in set_of_numbers:
        if num <= number:
            result = chia_so(number - num, set_of_numbers)
            if result is not None:
                return [num] + result
    return None


number = 9
set_of_numbers = [7,5,3]

result = chia_so(number, set_of_numbers)

if result is not None:
    print(f"{number} = {' + '.join(map(str, result))}")
else:
    print(f"{number} không thể chia thành tổng các số nhỏ hơn trong {set_of_numbers}")
