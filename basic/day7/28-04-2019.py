'''
list =[7.5,6,9,8,5,8.5]
n =len(list)
rank=[0]*n # tao mang phan tu N 
print (rank)

for i in range(n):
    for j in range(n):
        if list[j]>=list[i]:
            rank[i]+=1
print (rank)


#############Do nuoc day binh
bX=5
bY=3
z=4
x=0
y=0

while x!=z and y!=z:
    if x==0:
         print("Đo day binh %d lit"%bX)
         x=bX
    if y==bY:
        print ("Do het nuoc tu binh %d lit" %bY)
        y=0
    t=bY-y
    if t>x:
        t=x 
     
    x=x-t
    y=y+t
    print("Do %d lit tu bình %d qua bình %d" %(t,bX, bY))
**********************
import random

com =random.randint(0,2)
print ('0: Bao')
print ('1: Bua')
print ('2: Kéo')
hum = int(input("Moi ban nhap vao "))
if com==0:
    print ('May chon Bao')
elif com==1:
    print ('May chon Bua')
else :
    print ('May chon Keo')
if hum==0:
    print ('Ban chon Bao')
elif hum=1:
    print('Ban chon Bua')
else:
    print ('Ban chon Keo')
 if(com==hum):
     print ('Hoa roi')
     elif (hum==0 and com=2)
'''
import random
a = ["Bao", "Bua", "Keo"]
kq = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
c = ["Hoa", "Ban Thang", "Ban Thua"]


com = random.randint(0, 2)
n = len(a)
for i in range(n):
    print("%d: %s" % (i, a[i]))

hum = int(input("Moi Ban Nhap"))
print("May chon", a[com])
print("Nguoi chon", a[hum])

tk = kq[int(hum)][int(com)]

print(c[kq[int(hum)][com]])
