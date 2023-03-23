import base64
from path_file.file_utils import read_file_to_bytes

"""
    Why do I need 'b' to encode a string with Base64?
    
    -> You need to push a bytes-like object (bytes, bytearray,..) to the base64.b64encode() method, look like
    
    data = base64.b64encode(b'data to be encoded')
    data = base64.b64encode(input.encode())    
"""


def b64encode(data):
    #   b'SGVsm'.decode()   ->    'SGVsm'
    return base64.b64encode(data).decode()


def b64decode(data):
    return base64.b64decode(data).decode()


if __name__ == '__main__':
    file = "data.txt"
    data = read_file_to_bytes(file)
    # print(data)

    print("Encode")
    encode = b64encode(data)
    print(encode)

    print("Decode")
    decode = b64decode(encode.encode())
    print(decode)
