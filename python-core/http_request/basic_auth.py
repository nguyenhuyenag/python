import base64

import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080/HD_MOBILE/"

payload = json.dumps({
    "oDTrinhKy": None,
    "fileContent": None,
    "loaiTrinhKy": 1
})

username = 'username'
password = 'password'


def basic_auth_1():
    headers = {
        'Content-Type': 'application/json'
    }
    auth = HTTPBasicAuth(username, password)
    return requests.post(url, auth=auth, headers=headers, data=payload)


def basic_auth(u, p):
    token = base64.b64encode(f"{u}:{p}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'


def basic_auth_2():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': basic_auth(username, password)
    }
    return requests.post(url, headers=headers, data=payload)


# response = basic_auth_1()
response = basic_auth_2()

print(response.status_code)
print(response.json())
