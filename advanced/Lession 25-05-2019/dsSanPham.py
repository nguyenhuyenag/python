import urllib.request, json

path_url='http://dnhoang.laptrinhphp.net/public/api/san-pham'
url=urllib.request.urlopen(path_url)
data=json.loads(url.read().decode())
for item in data:
    print(item['ten_san_pham'])