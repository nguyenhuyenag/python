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


# post_json()
# post_file()
post_multiple_file()
