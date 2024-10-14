import base64
import json

import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080/HD_MOBILE/"

headers = {
    'Content-Type': 'application/json'
}


# Function to read the file to a byte array
def read_file_to_byte_array(fpath):
    with open(fpath, 'rb') as file:
        barray = file.read()
    return barray


file_path = "C:/Users/huyennv/Desktop/file/CauTruc_ContractSigning_CHUAKY.xml"
byte_array = read_file_to_byte_array(file_path)

# Encode the byte array to Base64 (needed to send binary data as JSON)
encoded_byte_array = base64.b64encode(byte_array).decode('utf-8')

payload = {
    "oDTrinhKy": None,
    "fileContent": encoded_byte_array,  # Base64 encoded fileContent
    "loaiTrinhKy": 1
}

auth = HTTPBasicAuth('username', 'password')
response = requests.post(url, auth=auth, headers=headers, data=json.dumps(payload))

print(response.status_code)
print(response.json())
