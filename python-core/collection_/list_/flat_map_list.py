from itertools import chain

list_of_lists = [[1, 2, 3], [4, 5, 6]]

print(list(chain(*list_of_lists)))

iterable = chain.from_iterable(list_of_lists)
print(list(iterable))

print(sum(list_of_lists, []))
