from path_file import file_utils
from collection_data.dictionary_json import create_json_pattern_from_array

fields = file_utils.read_file_into_list(r'table_data.txt')
# fields = ['name', 'id', 'message_main_attachment_id', 'write_date', 'x_property_id']

# fields.sort()
print(fields)
create_json_pattern_from_array.create_json(fields, "partner")
