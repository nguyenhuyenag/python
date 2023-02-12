import itertools


def cycle_array():
    arr = [1, 10, 100]
    count_cycle = 0;
    for v in itertools.cycle(arr):
        print(v)
        if v == 100:
            count_cycle += 1
            print("Cycle {}".format(count_cycle))
        if count_cycle == 4:
            break


def cyc_string():
    str = "ABCD"
    count_cycle = 0;
    for v in itertools.cycle(str):
        print(v)
        if v == "D":
            count_cycle += 1
            print("Cycle {}".format(count_cycle))
        if count_cycle == 4:
            break


# cycle_array()
cyc_string()
# list = [1,2,3,4,5]
# iterator = iter(list)
#
# print(iterator)
