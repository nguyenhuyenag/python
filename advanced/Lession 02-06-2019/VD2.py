import wx
app=wx.App()
frame= wx.Frame(None,title="Vi du TextCtrl",size=(400,200))
panel= wx.Panel(frame,-1)
str="Thong Tin Cong Ty"
text= wx.StaticText(panel,-1,label=str,pos=(20,0))
font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
text.SetFont(font)
wx.StaticText(panel,-1,label="cong ty trach nhiem huu han",pos=(20,50))
frame.Show(True)
app.MainLoop()