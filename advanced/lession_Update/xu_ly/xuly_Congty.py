from xu_ly.xuly_database import *
class CongTy(Database):
    def __init__(self, file_db):
        Database.__init__(self,file_db)
    def TTCongTy(self):
        chuoiSQL="select Ten, Dia_chi,Ma_so,Dien_thoai,Email from tblCongty"
        cursor=Database.getOne(self,chuoiSQL)
        TT={'Ten': cursor[0], 'Dia_chi':cursor[1], 'Ma_so':cursor[2],'Dien_thoai':cursor[3],'Email':cursor[4]}
        return TT
    def UpdateCTY(self, Ten, Dia_chi,Ma_so,Dien_thoai,Email):
        chuoiSQL="update tblCongty set Ten=?, Dia_chi=?,Ma_so=?,Dien_thoai=?,Email=?  "
        kq=Database.execute(self,chuoiSQL,(Ten, Dia_chi,Ma_so,Dien_thoai,Email))
        return kq
