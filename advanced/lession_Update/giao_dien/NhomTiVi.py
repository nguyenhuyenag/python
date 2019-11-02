# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from xu_ly.xuly_NhomTivi import *
###########################################################################
## Class pTTCT
###########################################################################

class pNhomTiVi ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nhom Ti vi" ), wx.HORIZONTAL )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Ma", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        gbSizer1.Add( self.m_staticText2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textMA = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_textMA, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Ten", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        gbSizer1.Add( self.m_staticText3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textTEN = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), 0 )
        gbSizer1.Add( self.m_textTEN, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_btnTHEM = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Them", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        gbSizer1.Add( self.m_btnTHEM, wx.GBPosition( 1, 1 ), wx.GBSpan( 4, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        sbSizer1.Add( gbSizer1, 0, 0, 5 )


        bSizer1.Add( sbSizer1, 0, 0, 5 )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Danh sach nhom" ), wx.VERTICAL )

        m_lstBoxChoices = []
        self.m_lstBox = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstBoxChoices, 0 )
        sbSizer2.Add( self.m_lstBox, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

         # Connect Events
        self.m_btnTHEM.Bind( wx.EVT_BUTTON, self.m_btnTHEMOnButtonClick )

    def __del__( self ):
        pass


# Virtual event handlers, overide them in your derived class
    def m_btnTHEMOnButtonClick( self, event ):
        Ma=self.m_textMA.GetValue()
        Ten=self.m_textTEN.GetValue()
        path_DB= 'du_lieu\dbTTCY.db'
        xl_Nhomtivi= NhomTivi(path_DB)
        kq= xl_Nhomtivi.ThemNhomTivi(Ma,Ten)
        if kq>0:
            wx.MessageBox("Thanh cong","Thong bao",wx.OK|wx.ICON_INFORMATION )
            self.LoadNhomCty()
        else:
            wx.MessageBox("Thất bại","Thong bao",wx.OK|wx.ICON_INFORMATION )


    def LoadNhomCty(self):
        path_DB= 'du_lieu\dbTTCY.db'
        xl_Nhomtivi= NhomTivi(path_DB)
        dsNhom= xl_Nhomtivi.DanhSachNhomTivi()
        if dsNhom!=None:
            lstNhomTV=[]
            for row in dsNhom:
                lstNhomTV.append(row['Ten'])
            self.m_lstBox.Clear()
            self.m_lstBox.AppendItems(lstNhomTV)

        