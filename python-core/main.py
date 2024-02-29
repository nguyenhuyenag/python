# def get_permutations(s):
#     if len(s) == 0:
#         return ['']
#
#     first_char = s[0]
#     rest_chars = s[1:]
#
#     rest_permutations = get_permutations(rest_chars)
#
#     all_permutations = []
#
#     for perm in rest_permutations:
#         for i in range(len(perm) + 1):
#             new_permutation = perm[:i] + first_char + perm[i:]
#             all_permutations.append(new_permutation)
#
#     return sorted(all_permutations)
#
# # Example usage:
# input_string = "abcd"
# result = get_permutations(input_string)
# print(result)

from itertools import permutations

def get_all_permutations(input_string):
    # Get all permutations of the input string
    permuted_strings = [''.join(p) for p in permutations(input_string)]

    return permuted_strings

# Example usage
input_str = "abc"
result = get_all_permutations(input_str)
print(result)
