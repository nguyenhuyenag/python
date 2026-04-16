import random
import time

import requests
import requests
import random
import time

url = ('/todolist/v1/user/login')

domain = [
    'http://localhost:8080',
    'http://192.168.11.69:8080'
]

data = {
    "uid": "abc@yahoo.com",
    "tokenSocial": "xxx"
}

while True:
    base = random.choice(domain)
    full_url = base + url

    response = requests.post(full_url, json=data)

    print(full_url)
    print(response.text)

    time.sleep(2)
    break
