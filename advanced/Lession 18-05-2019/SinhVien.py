class SinhVien(object):
    def __init__(self,_MaSV,_TenSV,_NgaySinh):
        self.MaSV=_MaSV
        self.TenSV=_TenSV
        self.NgaySinh=_NgaySinh
    def PrintSV(self):
        print(self.MaSV +' ' +self.TenSV +' '+ self.NgaySinh)

sv1=SinhVien('SV1','Nguyen Van A','01-02-2018')
sv2=SinhVien('SV2','Nguyen Van B','01-02-2018')
sv3=SinhVien('SV3','Nguyen Van C','01-02-2018')
sv4=SinhVien('SV4','Nguyen Van D','01-02-2018')

sv1.PrintSV()
sv2.PrintSV()
sv3.PrintSV()