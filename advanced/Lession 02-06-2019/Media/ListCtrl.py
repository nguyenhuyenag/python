import sys
import wx

player=[('','',''),('','',''),('','',''),('','','')]

app= wx
frame=wx.Frame(None,title="Vi du choice",size=(450,200))
panel=wx.Panel(frame,-1)
list=wx.ListCtrl(panel,-1,style=wx.LC_REPORT,size=(450,200))
list.InsertColumn(0,'Ma so')
