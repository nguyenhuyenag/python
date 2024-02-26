# A Pandas Series is like a column in a table
import pandas as pd

a = [1, 7, 2]


def series():
    myvar = pd.Series(a)
    print(myvar)


def series_index():
    myvar = pd.Series(a, index=["x", "y", "z"])
    print(myvar)


def series_json():
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(calories)
    print(myvar)


# filter index
def series_filter():
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pd.Series(calories, index=["day1", "day2"])
    print(myvar)


# series()
# series_index()
series_json()
# series_filter()
