"""
    bytearray() -> returns a bytearray object which is an array of given bytes. It gives a mutable sequence of integers
    in the range 0 <= x < 256
"""


# Mutable
def string_bytearray():
    msg = "Python is interesting"
    arr = bytearray(msg, 'utf-8')
    # arr[0] = 1                            # pass
    print(list(arr))


# Immutable
def sting_bytes():
    message = 'Python is fun'
    # byte_message = bytes(message, 'utf-8')  # an immutable bytes
    byte_message = message.encode('utf-8')
    # byte_message[0] = 1                   # -> TypeError 'bytes' object does not support item assignment
    print(list(byte_message))


sting_bytes()
# string_bytearray()
