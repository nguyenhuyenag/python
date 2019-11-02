# thisdict =	dict(brand="Ford", model="Mustang", year=1964)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

x = thisdict["year"]
print(x)

y = thisdict.get("model")
print(y)

# Change Values
thisdict["year"] = 2018
print(thisdict)


# Loop Through a Dictionary
for x in thisdict:
  print(x)


print()


for x in thisdict:
  print(thisdict[x])


print()


for x in thisdict.values():
  print(x)


for x, y in thisdict.items():
  print(x, ":", y)


# Check if Key Exists
if "model" in thisdict:
  print("Yes")


# Adding Items
thisdict["color"] = "red"
print(thisdict)


# Removing Items
thisdict.pop("model")
print(thisdict)


# removes the last inserted item
thisdict.popitem()
print(thisdict)

# del
del thisdict["brand"]
print(thisdict)


# The del keyword can also delete the dictionary completely:
#del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.


# clear
# The clear() keyword empties the dictionary:
thisdict.clear()
print(thisdict)


thisdict =	{ "brand": "Ford", "model": "Mustang", "year": 1964 }
# Copy a Dictionary
mydict = thisdict.copy()
# mydict = dict(thisdict)
print(mydict)


