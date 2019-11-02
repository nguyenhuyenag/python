# A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets
thistuple = ("apple", "banana", "cherry")
print(thistuple)

for x in thistuple:
  print(x)

# Once a tuple is created, you cannot change its values, cannot add items to it
#thistuple[1] = "blackcurrant"

# The values will remain the same:
#print(thistuple)

#Once a tuple is created, you cannot add items to it
#thistuple[3] = "orange" # This will raise an error
#print(thistuple)

# Remove Items
#del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# count()
arr = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = arr.count(5)

print(x)

x = arr.index(8)

print(x)
