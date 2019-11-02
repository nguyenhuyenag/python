
# install request
#import requests
#response = requests.post(url_path, data=value)
#print(response.json())
print('--------------------------login get Token----------------------------------------')
import urllib.request, urllib.parse, json
url_path='http://dnhoang.laptrinhphp.net/public/api/login'
value={'email':'dnhoang77@gmail.com','password':'hoang2019'}
data=urllib.parse.urlencode(value)
data=data.encode('ascii')

req=urllib.request.Request(url_path,data)

url=urllib.request.urlopen(req)
data =json.loads(url.read().decode())
token= data['access_token']
type =data['token_type']

print ('----------------------Get User------------------------------')
url_path='http://dnhoang.laptrinhphp.net/public/api/user'
headers = {
    'Authorization': type+' '+token,
    'Content-Type': 'application/x-www-form-urlencode',
    'Accept':'application/json'
}
req=urllib.request.Request(url_path, data=None, headers=headers)
url=urllib.request.urlopen(req)
data= json.loads(url.read().decode())
print (data)