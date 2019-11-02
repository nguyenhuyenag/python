import json


def saveJson(filePath, data):
    f = open(filePath, "w", encoding="utf-8")
    json.dump(data, f, indent = 4)
    f.close()


def loadJson(path):
    f = open(path, encoding = "utf-8")
    data = json.load(f)
    f.close()
    return data
