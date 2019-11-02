import urllib.request, json

def read_json_from_internet_unicode(url1):
    DEFAULT_ENCODING = 'utf-8'   
    
    urlResponse = urllib.request.urlopen(url1)
    
    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
    noi_dung = json.loads(urlResponse.read().decode(encoding))
    #pprint(output)
    return noi_dung

path ='https://api.github.com/users/mralexgray/repos'
noidung=read_json_from_internet_unicode(path)
#print(noidung)
for item in noidung:
    print(item['id'])
    print(item['full_name'])


# Vi du truyen them cookies, password, token.