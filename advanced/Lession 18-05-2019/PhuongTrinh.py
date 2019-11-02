import math as m
class PTB2():
    def __init__(self, _a, _b,_c):
        self.a=_a
        self.b=_b
        self.c=_c
    def TinhPhuongTrinhB2(self):
        #Cong thuc:f= b^2-a*c
        delta=pow(self.b,2) -4*self.a*self.c
        if delta<0:
            print ('Phuong trinh vo nghiem')
        elif delta==0:
            print ('Phuong trinh co 1 nghiem x1=x2='+ str(-self.b/2*self.a))# -b/2a
        else:
            x1=(-self.b+m.sqrt(delta))/(2*self.a)
            x2=(-self.b-m.sqrt(delta))/(2*self.a)
            print ('Phuong trinh co 2 nghiem x1= %f, x2= %f'%(x1,x2))

pt= PTB2(1,-2,1)
print(pt.TinhPhuongTrinhB2())
# print('-------------------------')
# b= PTB2(3,5,2)
# print(b.TinhPhuongTrinhB2())


if hasattr(pt,'b'):
    print(getattr(pt,'b'))
    setattr(pt,'b',10)
    print(getattr(pt,'b'))