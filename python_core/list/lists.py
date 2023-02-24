# import this

thelist = ["a", "b", "c"]
thelist.insert(1, "1")
thelist.append("a")
print(thelist)

# Extend list
tropical = ["mango", "pineapple", "papaya"]

print(thelist + tropical)
thelist.extend(tropical)

print(thelist)

# Remove list item
thelist.remove("mango")
print(thelist)

# Remove specified index: the pop() method removes the last item
thelist.pop(2)
print(thelist)

thelist.reverse()

print("Count:", thelist.count("a"))

# Sort list
print("Before sort: ", thelist)
print("Sorted: ", sorted(thelist))
thelist.reverse()
print("Reverse: ", thelist)
# print("Reverse: ", sorted(thelist, reverse=True))

# Clear the list
thelist.clear()
print("Clear list:", thelist)
