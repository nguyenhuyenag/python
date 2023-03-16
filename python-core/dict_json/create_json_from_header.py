header = ['name', 'id', 'age', 'department', 'likes_pizza']

data = [
    ['Jess', '006', '32', 'accounting', True],
    ['Lisa', '007', '21', 'engineering', False],
    ['Jack', '008', '20', 'sales', True],
    ['Wendy', '009', '22', 'accounting', True],
]

for row in data:
    pairs = zip(header, row)
    print(dict(pairs))
