n = int(input("n = "))

# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

# for i in range(n):
#     for j in range(n):
#         if i <= j:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

# for i in range(n):
#     for j in range(n):
#         if i + j <= n - 1:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

# for i in range(n):
#     for j in range(n):
#         if i + j >= n - 1:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

for i in range(n):

    for j in range(n):
        if i >= j:
            print("*", end=' ')
        else:
            print(" ", end=' ')

    print(end=' ')

    for j in range(n):
        if i <= j:
            print("*", end=' ')
        else:
            print(" ", end=' ')

    print(end=' ')

    for j in range(n):
        if i + j <= n - 1:
            print("*", end=' ')
        else:
            print(" ", end=' ')

    print(end=' ')

    for j in range(n):
        if i + j >= n - 1:
            print("*", end=' ')
        else:
            print(" ", end=' ')

    print()
