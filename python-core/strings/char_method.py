"""
    Character method
"""

"""
    chr() & ord : Số nguyên <-> char (ASCII unicode)
"""
char_value = 'A'
ascii_value = 65
print(f"ord('{char_value}') = chr({ascii_value})")

"""
   isalpha(): Kiểm tra một ký tự có phải là chữ cái hay không 
"""
print(f"isalpha('{char_value}') = {char_value.isalpha()}")

"""
    isdigit(): Kiểm tra một ký tự có phải là số hay không
"""
char = '5'
print(f"isdigit('{char}') = {char.isdigit()}")

"""
   isalnum(): Kiểm tra một ký tự có phải là chữ và số hay không 
"""
char = 'A5'
print(f"isalnum('{char}') = {char.isalnum()}")
