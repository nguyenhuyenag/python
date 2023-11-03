import random

size = ''

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

while not size.isnumeric():
    size = input('How big would you like your file to be (mb)? ')

size = int(size)

my_name = r'C:\Users\huyennv\Desktop\test\output.txt'

open(my_name, 'w').write('')

for mb in range(size):
    open(my_name, 'a').write(''.join(random.choices(characters, k=1000000)))

print('Done!')
