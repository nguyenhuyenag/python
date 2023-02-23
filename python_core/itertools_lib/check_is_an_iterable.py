from collections.abc import Iterable

print("[] -> ", isinstance([], Iterable))
print("{} -> ", isinstance({}, Iterable))
print("None -> ", isinstance(None, Iterable))
