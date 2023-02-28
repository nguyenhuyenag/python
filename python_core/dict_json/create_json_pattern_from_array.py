def create_json(list_fields, object_name):
    print("{")
    for field in list_fields:
        row = "\t'{}': {}.get('{}')".format(field, object_name, field)
        if field != list_fields[-1]:
            print(row + ",")
        else:
            print(row)
    print("}")


fields = ['id', 'name', 'sequence', 'write_uid', 'display_name', 'description',
          'create_uid', 'company_id', 'create_date', 'write_date']

create_json(fields, "val")
