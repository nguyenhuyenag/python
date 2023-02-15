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

# Filter
scores = [200, 105, 18, 80, 150, 140]
filtered_scores = [s for s in scores if s >= 150]
print(filtered_scores)


# Filter
def filter_height(height):
    if height < 150:
        return True
    else:
        return False


heights = [140, 180, 165, 162, 145]
filtered_heights = filter(filter_height, heights)
print(list(filtered_heights))

# Filter by lambda
ages = [20, 33, 44, 66, 78, 92]
filtered_ages = filter(lambda a: a > 50, ages)
print(list(filtered_ages))

# Clear the list
thelist.clear()
print("Clear list:", thelist)
