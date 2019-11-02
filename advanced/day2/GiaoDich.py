class GiaoDich(object):
    def __init__(self, ma, ngay, dongia, soluong, loai):
        self.ma = ma
        self.ngay = ngay
        self.dongia = dongia
        self.soluong = soluong
        self.loai = loai

    def thanhTien(self):
        return self.dongia * self.soluong

    def inGiaoDich(self):
        return self.ma + " - " + self.ngay+" - "+self.loai + " - " + str(self.soluong) \
            + " - " + str(self.dongia)+" - "+"Thanh tien: " + \
            str(self.thanhTien())


class GiaoDichTienTe(GiaoDich):  # GiaoDichTienTe ke thua GiaoDich
    def __init__(self, ma, ngay, dongia, soluong, loai, mua):
        self.mua = mua
        GiaoDich.__init__(self, ma, ngay, dongia, soluong, loai)

    def thanhTien(self):
        if self.mua:
            return GiaoDich.thanhTien(self)
        else:
            return GiaoDich.thanhTien(self) * 1.05

    def inGiaoDich(self):
        if self.mua:
            return "Giao dich Mua: " + GiaoDich.inGiaoDich(self)
        else:
            return "Giao dich Ban: " + GiaoDich.inGiaoDich(self)


if __name__ == "__main__":
    #c= GiaoDich('AA','01-01-2019',12,6,'A')
    # print(c.inGiaoDich())
    tieptuc = 1
    lst_Vang = []
    lst_Tien = []
    tong_sl = 0
    tongtien = 0
    print('QUAN LY GIAO DICH')
    while tieptuc == 1:
        ma = input('Nhap vao ma gd: ')
        ngay = input('Nhap vao ngay gd: ')
        soluong = int(input('Nhap vao so luong: '))
        i = int(input('Nhap loai giao dich 1: Vang, 2: Tien te: \t'))
        if i == 1:
            dongia = eval(input('Nhap vao don gia: '))
            loai = input("Chon loai vang 18k / 24k / 9999:\t")
            dgv = GiaoDich(ma, ngay, soluong, dongia, loai)
            lst_Vang.append(dgv)
            for item in lst_Vang:
                tong_sl += item.soluong
                tongtien += item.thanhTien()
                print(item.inGiaoDich())
            print('Tong so luong: '+str(tong_sl))
            print('Tong tien vang: '+str(tongtien))
        else:
            tong_sl = tongtien = 0
            loai = input('Chon loai: USD/EUR/AUD: \t')
            dongia = eval(input('Nhap ty gia: \t'))
            mua = True
            mb = int(input('Ban chon mua hay ban: 1: Mua, 2: Ban: \t'))
            if mb != 1:
                mua = False
            dgtt = GiaoDichTienTe(ma, ngay, soluong, dongia, loai, mua)
            lst_Tien.append(dgtt)
            for item in lst_Tien:
                tong_sl += item.soluong
                tongtien += item.thanhTien()
                print(item.inGiaoDich())
            print('Tong so luong: ' + str(tong_sl))
            print('Tong tien vang: ' + str(tongtien))
        tieptuc = int(input('Ban co muon tiep tuc giao dich khong? 1: Co, 0: Khong \t'))
