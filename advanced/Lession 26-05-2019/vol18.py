import sqlite3
con = sqlite3.connect('data/ql_ban_may_tinh.sqlite')
text = 'insert into khach_hang(ten_khach_hang,phai,ngay_sinh,dia_chi,dien_thoai,email) values(?,?,?,?,?,?)'
ten_khach_hang = input('nhap ten khach hang : ')
phai =input('nhap gioi tinh cua khach hang (1)Nam (2)Nu :')
ngay_sinh =input("nhap ngay sinh cua khach hang : ")
dien_thoai = input('nhapso dien thoai cua khach hang : ')
dia_chi = input('nhap dia chi cua khach hang : ')
email = input('nhap email cua khach hang : ')
con.execute(text,(ten_khach_hang,phai,ngay_sinh,dia_chi,dien_thoai,email))
con.commit()
con.close()