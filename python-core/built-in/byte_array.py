"""
    Built-in Functions
"""

"""
    bytearray(): Returns a bytearray object which is an array of given bytes. 
"""

my_str = "Python is fun"


# Immutable
def _bytes():
    byte_message = my_str.encode('utf-8')
    # byte_message[0] = 1                   # -> TypeError 'bytes' object does not support item assignment
    print(list(byte_message))


# Mutable
def _bytearray():
    arr = bytearray(my_str)
    # arr = bytearray(msg, 'utf-8')
    # arr[0] = 1                            # Pass
    print(list(arr))


_bytes()
# _bytearray()
