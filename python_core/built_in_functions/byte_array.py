def char_and_byte():
    print("Char to int: {} -> {}".format('a', ord('a')))
    print("Int to char: {} -> {}".format(97, chr(97)))


def sting_bytes():
    message = 'Python is fun'
    byte_message = bytes(message, 'utf-8')  # an immutable bytes
    # byte_message[0] = 1                   # TypeError: 'bytes' object does not support item assignment
    print(list(byte_message))


def string_bytearray():
    msg = "Python is interesting"
    arr = bytearray(msg, 'utf-8')
    # arr[0] = 1                            # pass
    print(list(arr))


char_and_byte()
# sting_bytes()
# string_bytearray()
