"""
    r means raw
    b means bytes
    u means unicode
    f means format

    r'\"'           =    \"
    '\"'            =    "

    r'Test\new'     =    Test\new
    "Test\new"      =    Test
                         ew
"""
print(r'Test\new')
print('Test\new')
print('\"')
