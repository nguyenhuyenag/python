from itertools import permutations


# p[collection, r]: r-length tuples, all possible orderings, no repeated elements
def base():
    for v in permutations("ABC"):
        print(v, end=" ")


# base()

print("All the permutations of the given container is:")
arr = [1,2,3]
for i in range(1, len(arr) + 1):
    print(list(permutations(arr, i)))
