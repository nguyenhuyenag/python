import wx
app=wx.App()
frame= wx.Frame(None,title="frame hello",size=(400,200))
panel= wx.Panel(frame,-1)
label= wx.StaticText(panel,-1,label="Hello word",pos=(100,50))
wx.TextCtrl(panel,-1,"Nhap ho ten ", pos=(50,100),size=(175,30))
frame.Show(True)
app.MainLoop()