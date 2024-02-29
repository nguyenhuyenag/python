import time
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


# def current_milli_time():
#     return round(time.time() * 1000)


def base64_decode_type(base64_string: str, file_path: str):
    try:
        # Decode the Base64 string
        decoded_data = base64.b64decode(base64_string)

        # Write the decoded data to a file
        with open(file_path, 'wb') as output_file:
            output_file.write(decoded_data)

        print(f"File successfully decoded and saved as {file_path}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    # file = r"output/data.txt"
    file_image = r"output/logo.png"
    file_output = r"output/decoded_image_2024.png"
    byte_array = read_file_to_bytes(file_image)
    encode = b64encode(byte_array)
    # print(encode)
    base64_decode_type(encode, file_output)

    # encode = b64encode(data)
    # print("Encode: ", encode)

    # decode = b64decode(encode.encode())
    # print("Decode: ", decode)
