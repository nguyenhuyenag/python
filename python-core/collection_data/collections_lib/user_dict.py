from collections import UserDict


class MyData(UserDict):

    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    def append(self, s=None):
        raise RuntimeError("Append not allowed")


mydict = MyData({'x': 10, 'y': 20})

# print(mydict)

# Deliting From Dict
# mydict.pop()

# Append not allowed
mydict.append({'z': 5})
