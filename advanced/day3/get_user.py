import json
import JsonUtils
import urllib.parse as _parse
import urllib.request as _request

token = JsonUtils.loadJson("files/token.json")
# print(token)

url = "http://dnhoang.laptrinhphp.net/public/api/user"
headers = {
    "Authorization": "Bearer " + token["access_token"],
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

req = _request.Request(url, data=None, headers=headers)
url = _request.urlopen(req)
data = json.loads(url.read().decode())

print(data)
