a, b = 0, 1
count = 0;
while count < 20:
    print(b, end = " ")
    count += 1
    a, b = b, a + b
