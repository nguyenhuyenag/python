from itertools import groupby

"""
    groups = []
    uniquekeys = []
    for k, g in groupby(data, keyfunc):
        groups.append(lists(g))  # Store group iterator as a lists
        uniquekeys.append(k)

    [k for k, g in groupby('AAAABBBCCDAABBB')]  --> A B C D A B
    [lists(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
"""

def group1(things):
    for key, group in groupby(things, lambda x: x[0]):
        for thing in group:
            print("A %s is a %s." % (thing[1], key))
        print("")


def group2(things):
    for key, group in groupby(things, lambda x: x[0]):
        listOfThings = " and ".join([thing[1] for thing in group])
        print(key + "s:  " + listOfThings + ".")


def print_groupby(iterable, keyfunc=None):
        for k, g in groupby(iterable, keyfunc):
            print("key: '{}'--> group: {}".format(k, list(g)))

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"),
          ("vehicle", "school bus")]

# group1(things)
# group2(things)

# Feature A: group consecutive occurrences
# print_groupby("BCAACACAADBBB")

# Feature B: group all occurrences
# print_groupby(sorted("BCAACACAADBBB"))

print_groupby(sorted("bCAaCacAADBbB"), lambda s: s.islower())
