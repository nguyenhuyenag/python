import wx


def OnClick(self):
    button.SetLabel("Chon")


app = wx.App()
frame = wx.Frame(None, title="Vi du TextCtrl", size=(400, 200))
panel = wx.Panel(frame, -1)
button = wx.Button(panel, -1, "Hello", pos=(50, 20))
frame.Bind(wx.EVT_BUTTON, OnClick, button)
button.SetDefault()
frame.Show(True)
app.MainLoop()
