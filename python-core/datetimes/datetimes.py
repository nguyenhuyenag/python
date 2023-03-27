import time
from datetime import date, datetime


def datetime_api():
    dt = datetime.now()
    print("Now: ", dt.strftime("%Y-%m-%d %H:%M:%S"))
    print("Year = {}, month = {}, day = {},".format(dt.year, dt.month, dt.day))

    # Date object to represent the date
    dt = date(2022, 2, 24)
    print("Init date:", dt)

    # Date object of today's date
    today = date.today()
    # Get current date
    print("Current date:", today)
    # Get day, month, and year of the week
    print("Current year:", today.year)
    print("Current month:", today.month)
    print("Current day:", today.day)


def to_millisecond():
    milli_sec = int(round(time.time() * 1000))
    print("Millisecond = ", milli_sec)


# to_millisecond()
datetime_api()
