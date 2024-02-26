from itertools import compress

# compress(iter, selector)
programs = ['C', 'C++', 'Java', 'Python']
comp1 = list(compress(programs, [0, 1, 0, 1]))
comp2 = list(compress(programs, [0, True, 0, False]))
print(comp1)
print(comp2)

