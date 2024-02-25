"""
    r -> raw            Python sẽ giữ nguyên
    b -> bytes
    u -> unicode
    f -> format

    r'\"'          =    \"
    '\"'           =    "

    r'Test\new'    =    Test\new
    "Test\new"     =    Test
                         ew
"""
print(r'Test\new')
print(r'Test\\new')
print('Test\new')
print('\"')
