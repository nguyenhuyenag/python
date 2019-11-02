import json
import urllib.request as _request
import urllib.parse as _parse
import luu_json

url = "http://dnhoang.laptrinhphp.net/public/api/login"
values = {"email": "dnhoang77@gmail.com", "password": "hoang2019"}
data = _parse.urlencode(values)
data = data.encode("ascii")
req = _request.Request(url, data)

url = _request.urlopen(req)
data = json.loads(url.read().decode())

print(data)
path = "files/token.json"
luu_json.saveJson(path, data)
