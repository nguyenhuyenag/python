import requests


def post_json():
    url = "https://httpbin.org/post"
    data = {
        "id": 1001,
        "name": "geek",
        "passion": "coding",
    }
    headers = {"Content-Type": "application/json; charset=utf-8"}
    response = requests.post(url, json=data, headers=headers)
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())


def post_file():
    url = 'https://httpbin.org/post'
    files = {'file': open('method_get.py', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)


def post_multiple_file():
    url = 'https://httpbin.org/post'
    file_list = [
        ('images', ('input.jpg', open('img/input.jpg', 'rb'), 'image/jpg')),
        ('images', ('output.jpg', open('img/output.jpg', 'rb'), 'image/jpg'))
    ]
    r = requests.post(url, files=file_list)
    print(r.text)


def call_api():
    access_token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJodXllbm52Iiwic2NvcGVzIjoiUk9MRV9BRE1JTixST0xFX1VTRVIiLCJpYXQiOjE2Nzk0NzI0ODUsImV4cCI6MTY3OTU1ODg4NX0.6gwNvBE0WICiH9bqWql93dgD9xDkxp6ty6p2o1Ks7DBF25zwQx7gH0moFj6AjQoY559UoauBeegqPQB0obs-pA'
    headers = {
        # "Content-Type": "application/json; charset=utf-8",
        'Authorization': 'Bearer {}'.format(access_token)
    }
    result = requests.get('http://localhost:8082/api/get-all-user', headers=headers)
    print(result.status_code)
    print(result.json())


# post_json()
# post_file()
# post_multiple_file()
call_api()
