import requests


def show_req_info(req):
    # print("status_code:", req.status_code)
    # print("header:", req.headers['content-type'])
    # print("encoding", req.encoding)
    # print("text:", req.text)
    print("url:", req.url)
    # print(r.json())


# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
# r = requests.get('https://api.github.com/events')
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

show_req_info(r)
