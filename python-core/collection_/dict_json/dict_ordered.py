from collections import OrderedDict

# Dictionary theo thứ tự chèn = LinkedHashMap
ordered = OrderedDict()
ordered['z'] = 1
ordered['z'] += 10
ordered['r'] = 3
ordered['f'] = 0
ordered['a'] = 5
ordered["abc"] = 9

print(ordered)
ordered.pop('a')
print(ordered)
