from requests.utils import requote_uri
from urllib.parse import urlencode, quote_plus, quote, unquote


def using_quote():
    url = 'https://api.com/search/repositories?q='
    key_search = 'requests+language:python'

    encode = url + quote(key_search.encode('utf8'))
    decode = unquote(encode)

    print("Encode:", encode)
    print("Decode:", decode)


def use_urlencode():
    payload = {'username': 'admin', 'password': '123456'}
    result = urlencode(payload, quote_via=quote_plus)
    print(result)


def use_requote():
    encode = requote_uri("https://www.sample.com/?id=123 abc")
    print(encode)


def safe_encode():
    print("Not safe:", quote('/'))
    print("Safe:", quote('/', safe=''))


# using_quote()
# use_urlencode()
# use_requote()
safe_encode()
