import requests


def query_string_parameters():
    url = 'https://httpbin.org/post'
    # params = b'q=requests+language:python'
    # params = {'q': 'requests+language:python'}
    params = {'key1': ['value1', 'value2']}
    # params = [('q', 'requests+language:python')]
    # params = [('key1', 'value1'), ('key1', 'value2')]

    response = requests.get(url, params=params)

    print(response.url)


query_string_parameters()
