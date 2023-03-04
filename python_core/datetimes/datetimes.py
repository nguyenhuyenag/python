import time
from datetime import datetime


def datetime_api():
    d = datetime.now()
    print("Now: ", d.strftime("%Y-%m-%d %H:%M:%S"))
    print("Year = {}, month = {}, day = {},".format(d.year, d.month, d.day))


def to_millisecond():
    milli_sec = int(round(time.time() * 1000))
    print("Millisecond = ", milli_sec)


datetime_api()
to_millisecond()
# method_name()


# ms = time.time_ns()
# print(ms)



