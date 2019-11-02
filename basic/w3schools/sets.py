thisset = {"apple", "banana", "cherry"}

# thisset = set(("apple", "banana", "cherry"))

print(thisset)

print("length: ", len(thisset))


# loop
for x in thisset:
  print(x)

print("banana" in thisset)


# Add Items
thisset.add("orange")
print(thisset)


# Add multiple items to a set, using the update() method:
thisset.update(["orange", "mango", "grapes"])
print(thisset)


# remove()
# If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print("after remove 'banana': ", thisset)


# discard()
# If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("banana")
print(thisset)


# pop(): remove the last item
# The return value of the pop() method is the removed item.
x = thisset.pop()
print(x)
print(thisset)


# clear()
# The clear() method empties the set:
thisset.clear()
print(thisset)


# del
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)


# difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
print(z)


# difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) 
print(x)


# intersection
# Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("intersection: ", z)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print("intersection: ", result)

# intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


# Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)


# issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) 
print(z)


# issuperset
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) 
print(z)


# pop()
# Remove a random item from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop() 
print(fruits)


# symmetric_difference
# The returned set contains a mix of items that are not present in both sets.
# (x hợp y) trừ (x giao y)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) 
print(z)


# union
# Return a set that contains all items from both sets, duplicates are excluded
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) 
print("union: ", z)

# update
# Insert the items from set y into set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) 
print("update: ", x)
