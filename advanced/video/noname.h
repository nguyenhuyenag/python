///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/gbsizer.h>
#include <wx/sizer.h>
#include <wx/statbox.h>
#include <wx/listbox.h>
#include <wx/panel.h>
#include <wx/choice.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/menu.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class pTTCT
///////////////////////////////////////////////////////////////////////////////
class pTTCT : public wxPanel 
{
	private:
	
	protected:
		wxStaticText* m_staticText2;
		wxTextCtrl* m_textTEN;
		wxStaticText* m_staticText3;
		wxTextCtrl* m_textTEN;
		wxButton* m_btnTHEM;
		wxListBox* m_lstBox;
		
		// Virtual event handlers, overide them in your derived class
		virtual void m_btnTHEMOnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		pTTCT( wxWindow* parent, wxWindowID id = wxID_ANY, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 500,300 ), long style = wxTAB_TRAVERSAL ); 
		~pTTCT();
	
};

///////////////////////////////////////////////////////////////////////////////
/// Class pTTCTMemu
///////////////////////////////////////////////////////////////////////////////
class pTTCTMemu : public wxPanel 
{
	private:
	
	protected:
		wxStaticText* m_staticText7;
		wxTextCtrl* m_textMASO;
		wxStaticText* m_staticText8;
		wxTextCtrl* m_textTEN;
		wxStaticText* m_staticText9;
		wxTextCtrl* m_textKYHIEU;
		wxChoice* m_choiceNHOMTIVI;
		wxStaticText* m_staticText10;
		wxTextCtrl* m_textDONGIANHAP;
		wxStaticText* m_staticText12;
		wxTextCtrl* m_textDONGIABAN;
		wxStaticText* m_staticText11;
		wxTextCtrl* m_textSOLUONGTON;
		wxStaticText* m_staticText13;
		wxStaticText* m_staticText14;
		wxButton* m_btnThem;
		
		// Virtual event handlers, overide them in your derived class
		virtual void m_btnThemOnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		pTTCTMemu( wxWindow* parent, wxWindowID id = wxID_ANY, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 617,257 ), long style = wxTAB_TRAVERSAL ); 
		~pTTCTMemu();
	
};

///////////////////////////////////////////////////////////////////////////////
/// Class Main
///////////////////////////////////////////////////////////////////////////////
class Main : public wxFrame 
{
	private:
	
	protected:
		wxMenuBar* m_menubar1;
		wxMenu* m_menu1;
		wxMenu* m_menu11;
		wxMenu* m_menu21;
		wxMenu* m_menu31;
		wxMenu* m_menu2;
		wxMenu* m_menu3;
	
	public:
		
		Main( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 500,300 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~Main();
	
};

#endif //__NONAME_H__
