import wx
app=wx.App()
frame= wx.Frame(None,title="Vi du TextCtrl",size=(400,200))
panel= wx.Panel(frame,-1)
strHoten=wx.StaticText(panel,-1,label="Ho Ten", pos=(10,10),size=wx.DefaultSize)
strHoten.SetForegroundColour("#8f3d5e")

txtHoten=wx.TextCtrl(panel,-1,value="ABC", pos=(100,10),size=(250,20))
txtHoten.SetForegroundColour("red")


strLop=wx.StaticText(panel,-1,label="Lop: ", pos=(10,50),size=wx.DefaultSize)
txtLop=wx.TextCtrl(panel,-1,value="ABC", pos=(100,10),size=(250,20))
frame.Show(True)
app.MainLoop()