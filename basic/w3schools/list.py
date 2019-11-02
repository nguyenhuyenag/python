
thislist = ["apple", "banana", "cherry"]

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

# Loop Through a List
for x in thislist:
  print(x)

# Check if Item Exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Add Items
thislist.append("orange")
print(thislist)

# List Length
print(len(thislist))

#Insert an item as the second position:
thislist.insert(1, "watermelon")
print(thislist)

# Remove Item
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)

# The del keyword removes the specified index:
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely:
del thislist
#print(thislist) # name 'thislist' is not defined

#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)

#count()
x = thislist.count("cherry")
print(x)

#extend()
cars = ['Ford', 'BMW', 'Volvo']
thislist.extend(cars)
print(thislist)

# index()
x = thislist.index("banana")
print(x)

# reverse()
thislist.reverse()
print(thislist)

# sort()
thislist.sort()
print(thislist)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)
cars.sort(reverse=False)
print(cars)

# Sort the list by the length of the values:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)


def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)
