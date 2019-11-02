from giao_dien.ThongTinDonVi import *
from xu_ly.xuly_Congty import *
import wx

app = wx.App()
frame= wx.Frame(None,title='Thong tin don vi',size=(600,300))
TTNV=pTTDV(frame)
# get cty from database
# path_DB= 'du_lieu\dbTTCY.db'
# cty= CongTy(path_DB)
# TT= cty.TTCongTy()
# #end getcty
# TTNV.m_textTEN.SetValue(TT['Ten'])
# TTNV.m_textDIACHI.SetValue(TT['Dia_chi'])
# TTNV.m_textMASO.SetValue(TT['Ma_so'])
# TTNV.m_textDIENTHOAI.SetValue(TT['Dien_thoai'])
# TTNV.m_textEMAIL.SetValue(TT['Email'])
frame.Show()
app.MainLoop()