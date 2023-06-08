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


# fields = read_file_into_list(r'table_data.txt')
fields = ['name', 'id', 'message_main_attachment_id',
                                                                    'state', 'partner_id', 'request_date',
                                                                    'appointment_date', 'appointment_stop_date',
                                                                    'slot_id',
                                                                    'technician_id', 'client_note',
                                                                    'job_desc', 'currency_id', 'company_id', 'street',
                                                                    'street2', 'zip', 'city',
                                                                    'state_id', 'country_id', 'email', 'mobile',
                                                                    'phone', 'search_locatiion',
                                                                    'website', 'display_name',
                                                                    'partner_latitude', 'partner_longitude',
                                                                    'create_uid', 'create_date',
                                                                    'write_uid',
                                                                    'write_date', 'x_property_id']
# fields.sort()
# print(fields)
create_json(fields, "template")
