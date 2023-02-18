# # database
# list1 = ['id', 'message_main_attachment_id', 'access_token', 'name', 'company_id', 'done_stage_boolean',
#          'cancel_stage_boolean', 'reopen_stage_boolean', 'closed_stage_boolean', 'open_boolean', 'state', 'active',
#          'ticket_from_website', 'ticket_from_portal', 'cancel_reason', 'priority', 'stage_id', 'ticket_type', 'team_id',
#          'team_head', 'user_id', 'subject_id', 'category_id', 'sub_category_id', 'partner_id', 'person_name', 'email',
#          'close_date', 'close_by', 'cancel_date', 'cancel_by', 'replied_date', 'comment', 'description', 'color',
#          'priority_new', 'customer_comment', 'category_bool', 'sub_category_bool', 'rating_bool', 'ticket_allocated',
#          'sh_status', 'sh_sla_deadline', 'sh_days_to_reach', 'sh_days_to_late', 'sh_due_date', 'report_token',
#          'mobile_no', 'email_subject', 'create_uid', 'create_date', 'write_uid', 'write_date', 'start_time', 'end_time',
#          'total_time', 'ticket_running', 'x_property_id', 'x_attribute_type', 'state_field']
#
# # project
# list2 = ['id', 'name', 'message_main_attachment_id', 'access_token',
#          'company_id',
#          'done_stage_boolean',
#          'cancel_stage_boolean', 'reopen_stage_boolean',
#          'closed_stage_boolean',
#          'open_boolean', 'state', 'active',
#          'ticket_from_website', 'ticket_from_portal',
#          'cancel_reason', 'priority', 'stage_id', 'ticket_type',
#          'team_id', 'team_head',
#          'user_id', 'subject_id', 'category_id', 'sub_category_id',
#          'partner_id', 'person_name', 'email', 'close_date',
#          'close_by',
#          'cancel_date', 'cancel_by', 'replied_date', 'comment',
#          'description', 'color', 'priority_new', 'customer_comment',
#          'category_bool', 'sub_category_bool', 'rating_bool',
#          'ticket_allocated', 'sh_status', 'sh_sla_deadline',
#          'sh_days_to_reach',
#          'sh_days_to_late', 'sh_due_date', 'report_token',
#          'mobile_no', 'email_subject', 'create_uid', 'create_date',
#          'write_uid',
#          'write_date', 'start_time', 'end_time', 'total_time',
#          'ticket_running', 'date_system', 'x_property_id',
#          'x_attribute_type', 'state_field', 'check_list_ids',
#          'custom_checklist', 'custom_checklist_ids']
#
# diff = list(set(list2) - set(list1))
# print(diff)

# from itertools import groupby
#
# some_list = [("Animal", "cat"),
#              ("Animal", "dog"),
#              ("Animal", "lion"),
#              ("Plant", "dandellion"),
#              ("Plant", "blumen")]
#
# for key, group in groupby(some_list, lambda x: x[0]):
#     key_and_group = {key: list(group)}
#     print(key_and_group)

from itertools import pairwise

# def pairwise(iterable):
#     "s -> (s0,s1), (s2,s3), (s4, s5), ..."
#     a = iter(iterable)
#     return zip(a, a)

l = [1, 2, 3, 4, 5, 6, 7]
print(())
for x, y in pairwise(l):
   print("{} + {} = {}".format(x, y, x + y))
   # print(v)
#
# # 1 + 2 = 3
# # 3 + 4 = 7
# # 5 + 6 = 11
# #izip() does almost same thing as zip() but it returns a iterlist.izip object which is iterable using next() or using loops
# print x
# #cant print contents of iterable object directly
# print "\nUSING LOOP TO PRINT CONTENTS OF izip OBJECT"
# for i in x:
#     print i