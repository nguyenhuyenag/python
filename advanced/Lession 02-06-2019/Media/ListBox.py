import wx
def OnListBox(seft):
    dlg= wx.MessageDialog(None,lst.GetStringSelection(),'A Message',wx.OK)
    dlg.ShowModal()
app=wx.App()
frame=wx.Frame(None,title="Vi du ListBox",size=(300,150))
panel= wx.Panel(frame,-1)
lstLanguages=['C','C++','JAVA','Python','Perl']
lst=wx.Lixtbox(panel,size)