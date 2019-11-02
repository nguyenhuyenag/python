class SinhVien():
    def __init__(self, _MaSV, _TenSV, _NgaySinh):
        self.MaSV = _MaSV
        self.TenSV = _TenSV
        self.NgaySinh = _NgaySinh

    def printSV(self):
        print(self.MaSV + ", " + self.TenSV + ", " + self.NgaySinh)

SV1 = SinhVien("SV01", "Nguyen Van A", "10/10")
SV2 = SinhVien("SV02", "Nguyen Van B", "11/11")
SV3 = SinhVien("SV03", "Nguyen Van C", "12/12")

SV1.printSV()
SV2.printSV()
SV3.printSV()