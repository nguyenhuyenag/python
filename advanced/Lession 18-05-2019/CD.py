class CD():
    tongtien=0
    def __init__(self, ten, casy,sobaihat, giathanh):
        self.ten=ten
        self.casy=casy
        self.sobaihat=sobaihat
        self.giathanh=giathanh
        CD.tongtien+= giathanh
    def thongTin_CD(self):
        return print('Ten %s - %s- %s - %s'%(self.ten,self.casy,self.sobaihat,self.giathanh))

if __name__ == "__main__":
    run=True
    lstCD=[]
    while run==True:
        ten= input('Nhap ten CD: ')
        casy=input('Nhap ten ca sy:')
        sobai=int(input('Nhap so bai hat:'))
        giathanh=eval(input('Gia thanh:'))
        cd1=CD(ten,casy,sobai,giathanh)
        lstCD.append(cd1)
        nex=eval(input('Ban co tiep tuc khong. 0: No, 1: Yes?'))
        print ('----------------------')
        if(nex!=1):
            run =False
 
    if(len(lstCD)>0):
        print ('Danh sach CD:')
        tongtien=0
        for cd in lstCD:
            tongtien+=cd.giathanh
            cd.thongTin_CD()
        print('Tong gia thanh',tongtien)
        

