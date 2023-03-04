import json


def string_to_json():
    jstr = '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(jstr)
    print(y["age"])


def format_json():
    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "children": ("Ann", "Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5}
        ]
    }
    # print(json.dumps(x))
    # print(json.dumps(x, indent=4))
    # print(json.dumps(x, indent=4, separators=(". ", " = ")))
    # Sort the result alphabetically by keys
    print(json.dumps(x, indent=4, sort_keys=True))


# is merged dictionary
def merge_json():
    x = {"age": 22, "gender": "Male"}
    y = {"name": 'Green'}
    x.update(y)
    print(x)


# string_to_json()
# format_json()
merge_json()
