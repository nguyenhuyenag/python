"""
    r"\""           =    \"
    "\""            =    "

    r"Test\new"     =    'Test\new'
    "Test\new"      =    'Test'
                         'ew'
"""
print(r"Test\new")
print("Test\new")
print("\"")