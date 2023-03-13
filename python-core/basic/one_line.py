def swap_value():
    a, b = 5, 10
    a, b = b, a
    print(a, b)


def list_comprehension():
    a1 = []
    for i in range(10):
        a1.append(i * i)
    print(a1)

    a2 = [i * i for i in range(10)]
    print(a2)

    a3 = [i * i for i in range(10) if i % 2 != 0]
    print(a3)


def print_without_newline():
    arr = [1, 2, 3, 4, 5]
    print(*arr)


def reverse_string_or_list():
    s = "python"
    print(s[::-1])

    arr = [1, 2, 3, 4, 5]
    print(arr[::-1])


def string_to_integer():
    user_input = "1 2 3 4 5"
    arr = list(map(int, user_input.split(" ")))
    print(arr)


# def read_file_into_list():
#     file_content = [line.strip() for line in open("path_file/data-path_file.txt", "r")]
#     print(file_content)


# swap_value()
# list_comprehension()
# print_without_newline()
reverse_string_or_list()
# string_to_integer()
# read_file_into_list()
