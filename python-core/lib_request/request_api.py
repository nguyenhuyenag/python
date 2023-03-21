import requests
from requests.exceptions import HTTPError


def show_req_info():
    payload = {'key1': 'value1', 'key2': 'value2'}
    res = requests.get('https://httpbin.org/get', params=payload)
    # req = requests.post('https://httpbin.org/post', data={'key': 'value'})

    print(f"Status Code: {res.status_code}, Reason: {res.reason}")
    # print("Header:", res.headers)
    # print("Encoding", res.encoding)
    # print("Response Content:", res.text)
    # print("Binary Response Content:", res.content)      # = bytyes(res.text)
    # print("JSON Response Content:", res.json())         # = json(res.text)
    # print("Raw Response Content:", res.raw)
    # print("url:", res.url)
    print(res.iter_lines())


def response_with_try_catch():
    urls = ['https://api.github.com', 'https://api.github.com/invalid']
    for url in urls:
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Success!')


# response_with_try_catch()
show_req_info()
