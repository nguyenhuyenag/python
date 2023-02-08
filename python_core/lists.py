import this


thislist = ["a", "b", "c"]

thislist.insert(1, "1")

thislist.append("a")

print(thislist)

# Extend list
tropical = ["mango", "pineapple", "papaya"]

print(thislist + tropical)
thislist.extend(tropical)

print(thislist)

# Remove list item
thislist.remove("mango")
print(thislist)

# Remove specified index: the pop() method removes the last item
thislist.pop(2)
print(thislist)

thislist.reverse()

print("Count:", thislist.count("a"))

# Clear the list
thislist.clear()
print(thislist)