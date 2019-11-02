import json
f = open("files/ttsv.json", encoding="utf-8")
noi_dung = json.load(f)
f.close()
print(noi_dung)

noi_dung["DiaChi"] = "Quan 4"

f = open("files/ttsv.json", "w", encoding="utf-8")
json.dump(noi_dung, f, indent=4)
f.close()

