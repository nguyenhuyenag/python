from collections import OrderedDict

# Dictionary theo thứ tự chèn
ordered = OrderedDict()
ordered['z'] = 1
ordered['r'] = 3
ordered['f'] = 0
ordered['a'] = 5
ordered['m'] = 9

print(ordered)
ordered.pop('a')
print(ordered)
