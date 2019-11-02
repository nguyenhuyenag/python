import json
import urllib.request as request

path = "http://dnhoang.laptrinhphp.net/public/api/san-pham"
url = request.urlopen(path)
data = json.loads(url.read().decode())

# print(data)

for entry in data:
    print(entry["ten_san_pham"])
