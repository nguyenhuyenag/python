import requests
from requests.exceptions import HTTPError


def show_req_info():
    payload = {'key1': 'value1', 'key2': 'value2'}
    res = requests.get('https://httpbin.org/get', params=payload)
    # req = requests.post('https://httpbin.org/post', data={'key': 'value'})

    # print("status_code:", res.status_code)

    print("header:", res.headers)

    # print("encoding", res.encoding)

    # print("text:", res.text)
    # print("content:", res.content)        # = bytyes(res.text)
    # print(res.json())                     # = json(res.text)

    # print("url:", res.url)


def todo():
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


def query_string_parameters():
    # Search GitHub's repositories for requests

    # params = b'q=requests+language:python'
    params = {'q': 'requests+language:python'}
    # params = [('q', 'requests+language:python')]

    headers = {'Accept': 'application/vnd.github.v3.text-match+json'}

    response = requests.get('https://api.github.com/search/repositories', params=params, headers=headers)

    # Inspect some attributes of the `requests` repository
    res = response.json()
    print("total_count:", res.get('total_count'))
    repository = res.get('items')[0]
    print(f'Repository name: {repository.get("name")}')
    print(f'Repository description: {repository.get("description")}')


# todo()
# show_req_info()
query_string_parameters()
