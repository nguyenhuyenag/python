# Megre dict
x = {"age": 22}
y = {"name": 'Green'}

y.update(x)
print(y)

z = {**x, **y}
print(z)

z = dict(x, **y)
print(z)
