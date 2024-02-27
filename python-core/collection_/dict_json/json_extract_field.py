my_json = {
    "id": 1,
    "city": False,
    "create_uid": False,
    "display_name": "False",
    "coordinates_calc": "by_addr",
}

key_values = []
for key, value in my_json.items():
    key_values.append(key)

print(key_values)
