import base64
from file.file_utils import read_file_to_bytes, read_file_to_string

"""
    Why do I need 'b' to encode a string with Base64?
    
    -> You need to push a bytes-like object (bytes, bytearray,..) to the base64.b64encode() method, look like
    
    data = base64.b64encode(b'data to be encoded')
    data = base64.b64encode(input.encode())    
"""


def b64e(s):
    # decode(): b'SGVs...'      ->      'SGVs...'
    return base64.b64encode(s).decode()


def b64d(s):
    return base64.b64decode(s).decode()


if __name__ == '__main__':
    file = r"D:\Dev\Projects\Github\python\python-core\file\data.txt"
    data = read_file_to_bytes(file)
    # print(data)

    encode = b64e(data)
    print(encode)

    decode = b64d(encode.encode())
    print(decode)
