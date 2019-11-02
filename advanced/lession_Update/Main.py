
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from giao_dien.NhomTiVi import *
from giao_dien.ThongTinDonVi import *
from giao_dien.ThongTinNhanVien import *
###########################################################################
## Class Main
###########################################################################

class Main ( wx.MDIParentFrame ):#wx.Frame
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menuCONGTY = wx.Menu()
		self.m_mItTTCTY = wx.MenuItem( self.m_menuCONGTY, wx.ID_ANY, u"Thong tin cong ty", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCONGTY.AppendItem( self.m_mItTTCTY )
		
		self.m_mItNHOMTIVI = wx.MenuItem( self.m_menuCONGTY, wx.ID_ANY, u"Nhom tivi", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCONGTY.AppendItem( self.m_mItNHOMTIVI )
		
		self.m_mItTHEMNV = wx.MenuItem( self.m_menuCONGTY, wx.ID_ANY, u"Them nhan vien", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCONGTY.AppendItem( self.m_mItTHEMNV )
		
		self.m_mItTHONGKENV = wx.MenuItem( self.m_menuCONGTY, wx.ID_ANY, u"Thong ke nhan vien", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuCONGTY.AppendItem( self.m_mItTHONGKENV )
		
		self.m_menubar1.Append( self.m_menuCONGTY, u"Cong ty" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_mItTHEMTIVI = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Them Tivi", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_mItTHEMTIVI )
		
		self.m_menubar1.Append( self.m_menu2, u"Tivi" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_mItTTCTYOnMenuSelection, id = self.m_mItTTCTY.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mItNHOMTIVIOnMenuSelection, id = self.m_mItNHOMTIVI.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mItTHEMNVOnMenuSelection, id = self.m_mItTHEMNV.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mItTHONGKENVOnMenuSelection, id = self.m_mItTHONGKENV.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mItTHEMTIVIOnMenuSelection, id = self.m_mItTHEMTIVI.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_mItTTCTYOnMenuSelection( self, event ):
		#frmNhomTiVi= w
	
	def m_mItNHOMTIVIOnMenuSelection( self, event ):
		event.Skip()
	
	def m_mItTHEMNVOnMenuSelection( self, event ):
		event.Skip()
	
	def m_mItTHONGKENVOnMenuSelection( self, event ):
		event.Skip()
	
	def m_mItTHEMTIVIOnMenuSelection( self, event ):
		event.Skip()
	
if __name__=='__main__':
    app= wx.App()
    frame=Main()
    frame.Maximize(True)
    frame.Show(True)
    app.MainLoop()
