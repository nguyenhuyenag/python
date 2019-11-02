from giao_dien.ThongTinNhanVien import *
from xu_ly.xuly_Congty import *
import wx

app = wx.App()
frame= wx.Frame(None,title='Thong tin nhan vien',size=(500,400))
frmTTNV=pTTNV(frame)
# get cty from database
path_DB= 'du_lieu\dbTTCY.db'
cty= CongTy(path_DB)
TT= cty.TTCongTy()
#end getcty
frmTTNV.m_textTEN.SetValue(TT['Ten'])
frmTTNV.m_textDIACHI.SetValue(TT['Dia_chi'])
frmTTNV.m_textMASO.SetValue(TT['Ma_so'])
frmTTNV.m_textDIENTHOAI.SetValue(TT['Dien_thoai'])
frmTTNV.m_textEMAIL.SetValue(TT['Email'])
frame.Show()
app.MainLoop()