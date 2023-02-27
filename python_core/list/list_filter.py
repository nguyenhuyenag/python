def filter_by_loop():
    scores = [200, 105, 18, 80, 150, 140]
    print([s for s in scores if s >= 150])


# Filter
def filter_height(height):
    return True if height < 150 else False


def filter_by_function():
    heights = [140, 180, 165, 162, 145]
    filtered_heights = filter(filter_height, heights)
    print(list(filtered_heights))


def filter_by_lambda():
    # Filter by lambda
    ages = [20, 33, 44, 66, 78, 92]
    filtered_ages = filter(lambda a: a > 50, ages)
    print(list(filtered_ages))


"""
    When None is used as the first argument to the filter() function, all elements that are truthy
    values (gives True if converted to boolean) are extracted
"""


def filter_by_none():
    random_list = [1, 'a', 0, False, True, '0']
    filtered_iterator = filter(None, random_list)
    filtered_list = list(filtered_iterator)
    print(filtered_list)


# filter_by_loop()
# filter_by_function()
# filter_by_lambda()
filter_by_none()
