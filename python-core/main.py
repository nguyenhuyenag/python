import base64

import requests
import json
from requests.auth import HTTPBasicAuth

headers = {
    'Content-Type': 'application/json'
}

# Function to convert file to base64
def file_to_base64(file_path):
    with open(file_path, "rb") as file:
        # Read file content and encode it to Base64
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
    return encoded_string

file_path = "C:/Users/huyennv/Desktop/ts24pro_mobile/CauTruc_ContractSigning_Ky_base64.xml"

# byte_array = read_file_to_byte_array(file_path)
# file_to_base64
# encoded_byte_array = base64.b64encode(byte_array).decode('utf-8')

payload = {
    "oDTrinhKy": {
				"maSoThue": "12344",
				"coQuanThue": "",
				"ngayTrinhKy": "2024-10-10",
				"tenfile":"daky.cs",
				"lanGui":0,
				"taiKhoanTrinhKy":"la.le@gmail.com",
				"taiKhoanKyChinh":"la.le@gmail.com",
				"taiKHoanKyDuyet":"",
				"tinhTrang":0,
				"dungLuong":0,
				"noiDung":"",
				"loai":"",
				"tinhTrangXuLy":""
			},
    "fileContentBase64": file_to_base64(file_path),
    "loaiTrinhKy": 1
}

auth = HTTPBasicAuth('ts24one', 'fd40f21f61fb4806587216692c30a1e1')
url = "http://localhost:8080/ts24pro_mobile/HD_MOBILE/addDownloadTrinhKy_HD?sKey=AxNC0xMC0wMyAxNzowODozN35fmZ1dkYyNktEcE15bnFBZUhUTHhZaE1VbzNMTT"

response = requests.post(url, auth=auth, headers=headers, data=json.dumps(payload))

print("Status:", response.status_code)
print(json.dumps(response.json(), indent=4, ensure_ascii=False))
