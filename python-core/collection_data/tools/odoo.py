import json

data = {}
with open("table_data.json", "r") as read_file:
    data = json.load(read_file)

print(data)

# keys = data.keys()
# print(keys)