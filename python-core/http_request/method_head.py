import requests

url = 'https://api.github.com/users/kennethreitz/repos?page=1&per_page=10'

r = requests.head(url=url)
print("link:", r.headers['link'])
print("next:", r.links["next"])

print("last:", r.links["last"])
