# l1 = ['id', 'included_segments', 'excluded_segments', 'filter', 'specific_devices', 'target_parameters', 'contents',
#       'headings', 'data', 'app_id', 'company_id', 'status', 'reason', 'external_id', 'one_signal_notification_id',
#       'recipients_count', 'cron_job', 'send_time', 'x_res_partner_check', 'email_char', 'email_text', 'x_all',
#       'x_link_url', 'x_detail_content', 'create_uid', 'create_date', 'write_uid', 'write_date']
#
# l2 = ['app_id', 'id', 'company_id',
#       'email_text', 'x_all',
#       'email',
#       'contents', 'headings', 'send_time',
#       'x_link_url',
#       'write_date', 'write_uid', 'create_date',
#       'create_uid',
#       'display_name', 'x_detail_content', 'data',
#       'company_id']
#
# print(set(l2) - set(l1))

from itertools import combinations_with_replacement

print("All the combination of List in sorted order(with replacement) is:")
print(list(combinations_with_replacement('ABC', 2)))
