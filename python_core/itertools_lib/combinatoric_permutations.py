from itertools import permutations


def base():
    for v in permutations("ABC"):
        print(v, end=" ")


# base()

print("All the permutations of the given container is:")
print(list(permutations([1, 2, 3], 1)))
print(list(permutations([1, 2, 3], 2)))
print(list(permutations([1, 2, 3], 3)))
