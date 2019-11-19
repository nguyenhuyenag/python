# Gộp danh sách
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

a = [x.strip() for x in freshfruit]
print(a)

vec = [2, 4, 6]
b = [2*x for x in vec if x > 3]
print(b)