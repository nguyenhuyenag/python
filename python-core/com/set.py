basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(basket)

fruit = set(basket)
print(fruit)
print('orange' in fruit)

a = set("abxyz")
b = set('abd')
print("a = ", a)
print("b = ", b)
print("a - b: ", a - b)  # Hiệu 2 tập hợp
print("a | b: ", a | b)  # Phép hợp
print("a & b: ", a & b)  # Phép giao
print("a ^ b: ", a ^ b)  # Thuộc a hoặc thuộc b nhưng không thuộc cả 2
print("a ^ b: ", (a | b) - (a & b))

