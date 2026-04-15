import requests

url = ('http://192.168.11.69:8080/ts24id_ws_v1/IDTS24.rest/loginAuthentication?userAgent=ts24pro&passAgent=d1663225d1689433cb6943621635189a'
       '&userAccount=huyennv@gmail.com'
       '&passAccount=e10adc3949ba59abbe56e057f20f883e_1')

for i in range(4):
    response = requests.post(url)
    print(response.text)
