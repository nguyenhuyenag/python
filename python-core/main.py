
def chia_so(number, set_of_numbers):
    result = []
    set_of_numbers = sorted(set_of_numbers, reverse=True) # Sắp xếp tập hợp theo thứ tự giảm dần
    for num in set_of_numbers:
        while number >= num:
            result.append(num)
            number -= num
    if number == 0:
        print(f"{sum(result)} = {' + '.join(map(str, result))}")
    else:
        print('No solution!')


if __name__ == '__main__':
    number = 58
    set_of_numbers = [14, 16, 18, 19, 1]
    chia_so(number, set_of_numbers)
