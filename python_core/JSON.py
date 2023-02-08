import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# Parse JSON
y = json.loads(x)

print(y["age"])

# Convert to JSON
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# Sort the result alphabetically by keys
print(json.dumps(x, indent=4, sort_keys=True))
