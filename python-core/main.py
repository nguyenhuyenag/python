data_uri = 'data:image/png;base64,Accccassss...'

if data_uri.startswith('data:'):
    _, base64_content = data_uri.split(',', 1)
    print("Base64 Content:", base64_content)
else:
    print("Invalid data URI")
