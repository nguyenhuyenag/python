# import json
import requests


def login():
    url = "http://localhost:8082/auth/login"
    payload = {
        "username": "huyennv",
        "password": "123456"
    }
    # Adding empty header as parameters are being sent in payload
    headers = {}
    r = requests.post(url, json=payload, headers=headers)
    # r = requests.post(url, data=json.dumps(payload), headers=headers)
    print("status_code:", r.status_code)
    print("Response JSON:", r.json())


def do_post():
    url = "https://httpbin.org/post"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {
        "id": 1001,
        "name": "geek",
        "passion": "coding",
    }
    response = requests.post(url, headers=headers, json=data)
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())


def post_file():
    url = 'https://httpbin.org/post'
    files = {'file': open('get_method.py', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)


# login()
# do_post()
post_file()
