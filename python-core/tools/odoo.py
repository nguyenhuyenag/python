def read_file_into_list(_file):
    return [line.strip() for line in open(_file, "r")]


def create_json(list_fields, object_name):
    data = ""
    for field in list_fields:
        row = f"\t'{field}': {object_name}.get('{field}')"
        if field != list_fields[-1]:
            data += row + ",\n"
        else:
            data += row
    print("{\n" + data + "\n}")

pfile = r'table_data.txt'
fields = read_file_into_list(pfile)
# fields.sort()
# print(fields)
create_json(fields, "template")
