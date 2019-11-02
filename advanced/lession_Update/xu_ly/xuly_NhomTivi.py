from xu_ly.xuly_database import *

class NhomTivi(Database):
    def __init__(self, file_db):
        Database.__init__(self,file_db)
    def DanhSachNhomTivi(self):
        chuoiSQL="select Id, Ma,Ten from tblNhomTivi"
        cursor=Database.getALL(self,chuoiSQL)
        if cursor != None:    
            lstNhom=[]
            for row in cursor:
                TT={'Id':row[0], 'Ma': row[1], 'Ten':row[2]}
                lstNhom.append(TT)
        return lstNhom
    def ThemNhomTivi(self, Ma,Ten):
        chuoiSQL="insert into tblNhomTivi (Ma,Ten) values(?,?)"
        kq=Database.execute(self,chuoiSQL,(Ma,Ten))
        return kq
    def UpdateNhomTivi(self, Ma,Ten):
        chuoiSQL="update tblNhomTivi set Ma=?, Ten=? "
        kq=Database.execute(self,chuoiSQL,(Ma,Ten))
        return kq
