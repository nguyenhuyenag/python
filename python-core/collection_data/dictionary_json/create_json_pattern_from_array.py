def create_json(list_fields, object_name):
    data = ""
    for field in list_fields:
        row = f"\t'{field}': {object_name}.get('{field}')"
        if field != list_fields[-1]:
            data += row + ",\n"
        else:
            data += row
    print("{\n" + data + "\n}")

if __name__ == '__main__':
    fields = ['id', 'name', 'currency_id', 'code', 'create_uid', 'create_date', 'write_date']
    create_json(fields, "template")
