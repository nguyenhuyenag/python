import json
# noi_dung= {"MaSV":"SV001", "HoSV":"MAI", "TenSV":"SON"}
# f=open('ttsc.json','w',encoding='utf-8')
# json.dump(noi_dung,f,indent=4)
# f.closed()

f=open('ttsc.json', encoding='utf-8')
noi_dung=json.load(f)
f.close()
noi_dung['dia_chi']='Nguyen Chi Thanh'
f=open('ttsc.json', 'w', encoding='utf-8')
json.dump(noi_dung, f, indent=4)
f.close()