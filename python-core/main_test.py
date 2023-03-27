import os

# print all environment variables as a dictionary
print(os.environ)

# get LANG variable without KeyError
print(os.environ.get("LANG"))
