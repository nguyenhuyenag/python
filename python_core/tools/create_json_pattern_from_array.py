def create_json(list_fields, object_name):
    print("{")
    for field in list_fields:
        row = "\t'" + field + "': " + object_name + "[" + "'" + field + "'" + "]"
        if field != list_fields[-1]:
            print(row + ",")
        else:
            print(row)
    print("}")


fields = ['id', 'name', 'company_id',
          'display_name', 'date', 'title', 'parent_id',
          'lang', 'tz', 'user_id', 'vat', 'website', 'comment',
          'credit_limit', 'active', 'customer_rank',
          'employee', 'supplier_rank', 'function', 'type',
          'street', 'street2', 'zip', 'city', 'state_id',
          'country_id', 'email', 'phone',
          'mobile', 'is_company', 'color',
          'commercial_partner_id', 'commercial_company_name',
          'company_name', 'write_uid', 'create_uid',
          'calendar_last_notif_ack', 'create_date', 'write_date']

# 'id': partner['id']
create_json(fields, "partner")
