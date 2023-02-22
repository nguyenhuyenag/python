# l1 = ['id', 'name', 'company_id', 'create_date', 'display_name', 'date', 'title', 'parent_id', 'ref', 'lang', 'tz', 'user_id', 'vat', 'website', 'comment', 'credit_limit', 'active', 'employee', 'function', 'type', 'street', 'street2', 'zip', 'city', 'state_id', 'country_id', 'partner_latitude', 'partner_longitude', 'email', 'phone', 'mobile', 'is_company', 'industry_id', 'color', 'partner_share', 'commercial_partner_id', 'commercial_company_name', 'company_name', 'create_uid', 'write_uid', 'write_date', 'message_main_attachment_id', 'email_normalized', 'message_bounce', 'signup_token', 'signup_type', 'signup_expiration', 'team_id', 'debit_limit', 'last_time_entries_checked', 'invoice_warn', 'invoice_warn_msg', 'supplier_rank', 'customer_rank', 'sale_warn', 'sale_warn_msg', 'user_is', 'calendar_last_notif_ack', 'website_id', 'is_published', 'purchase_warn', 'purchase_warn_msg', 'partner_ref_id', 'black_list', 'fax', 'picking_warn', 'picking_warn_msg', 'website_meta_title', 'website_meta_description', 'website_meta_keywords', 'website_meta_og_img', 'seo_name', 'website_description', 'website_short_description', 'x_select_property', 'x_is_tenants', 'x_pro4u_dob', 'x_pro4u_cmnd', 'is_property', 'x_qr_code']
#
# l2 = ['id', 'name', 'company_id', 'create_date',
#                       'display_name', 'date', 'title', 'parent_id',
#                       'lang', 'tz', 'user_id', 'vat', 'website', 'comment',
#                       'credit_limit', 'active', 'customer_rank',
#                       'employee', 'supplier_rank', 'function', 'type',
#                       'street', 'street2', 'zip', 'city', 'state_id',
#                       'country_id', 'email', 'phone',
#                       'mobile', 'is_company', 'color',
#                       'commercial_partner_id', 'commercial_company_name',
#                       'company_name', 'write_uid', 'create_uid',
#                       'write_date', 'calendar_last_notif_ack'
#                       ]
#
# print(set(l2) - set(l1))

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

# print(2 ^ 2 ^ 3)
arr = [1, 1, 2 , 2, 3, 3, 4]

x = 0

for v in arr:
    x = x ^ v

print(x)