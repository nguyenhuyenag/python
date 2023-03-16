from collections import OrderedDict

# Dictionary theo thứ tự chèn
_ordered = OrderedDict()
_ordered['z'] = 1
_ordered['r'] = 3
_ordered['f'] = 0
_ordered['a'] = 5
_ordered['m'] = 9

print(_ordered)
_ordered.pop('a')
print(_ordered)
