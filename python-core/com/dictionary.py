dic = {'jack': 4098, 'sape': 4139}
# hoặc
dic = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# hoặc 
dic = dict(sape=4139, guido=4127, jack=4098)

dic['guido'] = 4127

print(dic.get('jack'))

# Xóa 1 phần tử
del dic['sape']

# Kiểm tra 1 khóa có tồn tại trong dictionary
print(dic.__contains__("jack"))
# hoặc
print('jack' in dic)

print(dict([(v, v ** 2) for v in (2, 4, 6)]))

# Loop for dictionary
thisdict = {'a': 'the', 'b': 'brave', 'c': 'new'}

# For by key
for k in thisdict:
    print("key: %s, value: %s" % (k, thisdict[k]))

print()

# For by key & value
for k, v in thisdict.items():
    # print("key:", k, ", value:", v)
    print("key: %s, value: %s" % (k, v))

print()

# For by value
for v in thisdict.values():
    print(v)
