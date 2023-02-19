from itertools import  zip_longest

# zip() iterates up to the length of the shortest iterator
for v in zip("ABCD", "xy"):
    print(v, end=" ")

print()
# zip_longest() iterates up to the length of the longest iterator
# zip_longest() will go through all entries, and if one of the iterators runs out early, it gets replaced with None
for v in zip_longest("ABCD", "xy", fillvalue="-"):
    print(v, end=" ")

