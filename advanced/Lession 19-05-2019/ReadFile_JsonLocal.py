import urllib.request, json

file= open('D:\\Son\\Lession 19-05-2019\\files\\QLCT_1.json', encoding='utf-8')
noidung = json.load(file)
print(noidung)
CONG_TY=noidung['CONG_TY'][0]
DON_VI=noidung['DON_VI']
tongsonv=0
for nv in DON_VI:
    tongsonv+=int(nv['So_Nhan_vien'])

print ("Thong tin cong ty===========")
print (CONG_TY['Ten'])
print (CONG_TY['Dien_thoai'])
print (CONG_TY['Mail'])
print (CONG_TY['Dia_chi'])
print("Tong so nhan vien: "+ str(tongsonv))
print("===================")
for nv in DON_VI:
    print (nv['Ten'])