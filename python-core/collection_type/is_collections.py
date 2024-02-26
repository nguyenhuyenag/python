from collections.abc import Iterable

# is collections
def is_collections():
    print("[] -> ", isinstance([], Iterable))
    print("{} -> ", isinstance({}, Iterable))
    print("None -> ", isinstance(None, Iterable))

is_collections()
