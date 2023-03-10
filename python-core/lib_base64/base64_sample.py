import base64

from file.file_utils import read_file_to_bytes

"""
    Why do I need 'b' to encode a string with Base64?
    
    -> You need to push a bytes-like object (bytes, bytearray,..) to the base64.b64encode() method, look like
    
    data = base64.b64encode(b'data to be encoded')
    data = base64.b64encode(input.encode())    
"""

if __name__ == '__main__':
    file = "base64_sample.py"
    data = read_file_to_bytes(file)
    print(data)
    base64_str = base64.b64encode(data)
    print(base64_str)
    print(base64.b64decode(base64_str))
