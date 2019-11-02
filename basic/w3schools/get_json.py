# import json
# import urllib

# url = 'https://api.github.com/users?since=100'
# output = json.load(urllib.urlopen(url))
# print(output)

import json
result = json.loads('https://api.github.com/users?since=100')  # result is now a dict
print(result)

