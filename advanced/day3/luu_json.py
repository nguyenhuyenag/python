import json

def saveJson(filePath, data):
    f = open(filePath, "w", encoding="utf-8")
    json.dump(data, f, indent=4)
    f.close()


noi_dung = {"MaSV": "SV001", "HoSV": "Nguyen Van", "TenSV": "A"}
path = "files/ttsv.json"
saveJson(path, noi_dung)

# f = open("files/ttsv.json", "w", encoding="utf-8")
# json.dump(noi_dung, f, indent=4)
# f.close()
