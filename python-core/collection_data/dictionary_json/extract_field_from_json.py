my_json = {
        "city": False,
        "coordinates_calc": "by_addr",
        "country": False,
        "create_date": False,
        "create_uid": False,
        "display_name": "False",
        "id": 1,
        "name": False,
        "store_email": False,
        "store_lat": False,
        "store_long": False,
        "store_mob": False,
        "store_phone": False,
        "store_state": False,
        "street": False,
        "write_date": False,
        "write_uid": False,
        "x_company_id": False,
        "zipcode": False
    }

key_values = []
for key, value in my_json.items():
    key_values.append(key)

print(key_values)
