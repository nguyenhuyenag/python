from collections import Counter

arr = ['d', 'a', 'c', 'a', 'e', 'b', 'c', 'c', 'b', 'd']
counter = Counter(arr)
print(counter)
print(counter.most_common(1))
print(counter.most_common(2))
