# def create_json1(list_fields, object_name):
#     print("{")
#     for field in list_fields:
#         row = "\t'{}': {}.get('{}')".format(field, object_name, field)
#         if field != list_fields[-1]:
#             print(row + ",")
#         else:
#             print(row)
#     print("}")

def create_json(list_fields, object_name):
    data = ""
    for field in list_fields:
        row = f"\t'{field}': {object_name}.get('{field}')"
        if field != list_fields[-1]:
            data += row + ",\n"
        else:
            data += row
    print("{\n" + data + "\n}")


fields = ['id', 'name', 'currency_id', 'code', 'create_uid', 'create_date', 'write_date']

create_json(fields, "val")
