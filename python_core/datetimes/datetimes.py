import time
from datetime import datetime


def method_name():
    d = datetime.now()
    print(d)
    print(d.year)
    print(d.strftime("%Y-%m-%d %H:%M:%S"))


# method_name()


ms = time.time_ns()
print(ms)

# import time
milli_sec = int(round(time.time() * 1000))
print(milli_sec)


