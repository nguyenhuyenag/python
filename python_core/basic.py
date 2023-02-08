# Print without newline
# print("Enter a number: ", end="")

n = input("Enter a number: ")

print("Type of n: ", type(n))

for i in range(1, int(n)):
    if i % 2 == 0:
        print('%d is event' % i)
    else:
        print('%d is odd' % i)
