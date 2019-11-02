from giao_dien.NhomTiVi import *
from xu_ly.xuly_NhomTivi import *
import wx

app = wx.App()
frame= wx.Frame(None,title='Nhom TiVi',size=(500,400))
frmNhom=pNhomTiVi(frame)
# get cty from database
frmNhom.LoadNhomCty()

# path_DB= 'du_lieu\dbTTCY.db'
# xl_Nhomtivi= NhomTivi(path_DB)
# dsNhom= xl_Nhomtivi.DanhSachNhomTivi()
# lstNhomTV=[]
# for row in dsNhom:
#     lstNhomTV.append(row['Ten'])
# frmNhom.m_lstBox.Clear()
# frmNhom.m_lstBox.AppendItems(lstNhomTV)

#end getcty
frame.Show()
app.MainLoop()