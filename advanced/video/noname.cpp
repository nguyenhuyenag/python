///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

pTTCT::pTTCT( wxWindow* parent, wxWindowID id, const wxPoint& pos, const wxSize& size, long style ) : wxPanel( parent, id, pos, size, style )
{
	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );
	
	wxStaticBoxSizer* sbSizer1;
	sbSizer1 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Nhom Ti vi") ), wxHORIZONTAL );
	
	wxGridBagSizer* gbSizer1;
	gbSizer1 = new wxGridBagSizer( 0, 0 );
	gbSizer1->SetFlexibleDirection( wxBOTH );
	gbSizer1->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_staticText2 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Ma"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2->Wrap( -1 );
	gbSizer1->Add( m_staticText2, wxGBPosition( 0, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textTEN = new wxTextCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer1->Add( m_textTEN, wxGBPosition( 0, 1 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText3 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Ten"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3->Wrap( -1 );
	gbSizer1->Add( m_staticText3, wxGBPosition( 0, 2 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textTEN = new wxTextCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 280,-1 ), 0 );
	gbSizer1->Add( m_textTEN, wxGBPosition( 0, 3 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_btnTHEM = new wxButton( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Them"), wxDefaultPosition, wxSize( 100,-1 ), 0 );
	gbSizer1->Add( m_btnTHEM, wxGBPosition( 1, 1 ), wxGBSpan( 4, 3 ), wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	sbSizer1->Add( gbSizer1, 0, 0, 5 );
	
	
	bSizer1->Add( sbSizer1, 0, 0, 5 );
	
	wxStaticBoxSizer* sbSizer2;
	sbSizer2 = new wxStaticBoxSizer( new wxStaticBox( this, wxID_ANY, wxT("Danh sach nhom") ), wxVERTICAL );
	
	m_lstBox = new wxListBox( sbSizer2->GetStaticBox(), wxID_ANY, wxDefaultPosition, wxDefaultSize, 0, NULL, 0 ); 
	sbSizer2->Add( m_lstBox, 1, wxALL|wxEXPAND, 5 );
	
	
	bSizer1->Add( sbSizer2, 1, wxEXPAND, 5 );
	
	
	this->SetSizer( bSizer1 );
	this->Layout();
	
	// Connect Events
	m_btnTHEM->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( pTTCT::m_btnTHEMOnButtonClick ), NULL, this );
}

pTTCT::~pTTCT()
{
	// Disconnect Events
	m_btnTHEM->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( pTTCT::m_btnTHEMOnButtonClick ), NULL, this );
	
}

pTTCTMemu::pTTCTMemu( wxWindow* parent, wxWindowID id, const wxPoint& pos, const wxSize& size, long style ) : wxPanel( parent, id, pos, size, style )
{
	wxGridBagSizer* gbSizer2;
	gbSizer2 = new wxGridBagSizer( 0, 0 );
	gbSizer2->SetFlexibleDirection( wxBOTH );
	gbSizer2->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_staticText7 = new wxStaticText( this, wxID_ANY, wxT("Ma so"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText7->Wrap( -1 );
	gbSizer2->Add( m_staticText7, wxGBPosition( 1, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textMASO = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 200,-1 ), 0 );
	gbSizer2->Add( m_textMASO, wxGBPosition( 1, 1 ), wxGBSpan( 1, 2 ), wxALL|wxEXPAND, 5 );
	
	m_staticText8 = new wxStaticText( this, wxID_ANY, wxT("Ten"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText8->Wrap( -1 );
	gbSizer2->Add( m_staticText8, wxGBPosition( 2, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textTEN = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 120,-1 ), 0 );
	gbSizer2->Add( m_textTEN, wxGBPosition( 2, 1 ), wxGBSpan( 1, 2 ), wxALL|wxEXPAND, 5 );
	
	m_staticText9 = new wxStaticText( this, wxID_ANY, wxT("Ky hieu"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText9->Wrap( -1 );
	gbSizer2->Add( m_staticText9, wxGBPosition( 3, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textKYHIEU = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 200,-1 ), 0 );
	gbSizer2->Add( m_textKYHIEU, wxGBPosition( 3, 1 ), wxGBSpan( 1, 2 ), wxALL|wxEXPAND, 5 );
	
	wxArrayString m_choiceNHOMTIVIChoices;
	m_choiceNHOMTIVI = new wxChoice( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choiceNHOMTIVIChoices, 0 );
	m_choiceNHOMTIVI->SetSelection( 0 );
	gbSizer2->Add( m_choiceNHOMTIVI, wxGBPosition( 5, 4 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );
	
	m_staticText10 = new wxStaticText( this, wxID_ANY, wxT("Don gia Nhap"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText10->Wrap( -1 );
	gbSizer2->Add( m_staticText10, wxGBPosition( 4, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textDONGIANHAP = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( -200,-1 ), 0 );
	gbSizer2->Add( m_textDONGIANHAP, wxGBPosition( 4, 1 ), wxGBSpan( 1, 2 ), wxALL|wxEXPAND, 5 );
	
	m_staticText12 = new wxStaticText( this, wxID_ANY, wxT("Don gia ban"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText12->Wrap( -1 );
	gbSizer2->Add( m_staticText12, wxGBPosition( 4, 3 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textDONGIABAN = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 150,-1 ), 0 );
	gbSizer2->Add( m_textDONGIABAN, wxGBPosition( 4, 4 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText11 = new wxStaticText( this, wxID_ANY, wxT("So Luong Ton"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText11->Wrap( -1 );
	gbSizer2->Add( m_staticText11, wxGBPosition( 5, 0 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_textSOLUONGTON = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gbSizer2->Add( m_textSOLUONGTON, wxGBPosition( 5, 1 ), wxGBSpan( 1, 2 ), wxALL|wxEXPAND, 5 );
	
	m_staticText13 = new wxStaticText( this, wxID_ANY, wxT("Nhom Tivi"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText13->Wrap( -1 );
	gbSizer2->Add( m_staticText13, wxGBPosition( 5, 3 ), wxGBSpan( 1, 1 ), wxALL, 5 );
	
	m_staticText14 = new wxStaticText( this, wxID_ANY, wxT("THONG TIN DON VI"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText14->Wrap( -1 );
	m_staticText14->SetFont( wxFont( 14, 70, 90, 92, false, wxEmptyString ) );
	
	gbSizer2->Add( m_staticText14, wxGBPosition( 0, 1 ), wxGBSpan( 1, 4 ), wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_btnThem = new wxButton( this, wxID_ANY, wxT("Them"), wxDefaultPosition, wxSize( 150,-1 ), 0 );
	gbSizer2->Add( m_btnThem, wxGBPosition( 6, 2 ), wxGBSpan( 1, 1 ), wxALL|wxEXPAND, 5 );
	
	
	this->SetSizer( gbSizer2 );
	this->Layout();
	
	// Connect Events
	m_btnThem->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( pTTCTMemu::m_btnThemOnButtonClick ), NULL, this );
}

pTTCTMemu::~pTTCTMemu()
{
	// Disconnect Events
	m_btnThem->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( pTTCTMemu::m_btnThemOnButtonClick ), NULL, this );
	
}

Main::Main( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	m_menubar1 = new wxMenuBar( 0 );
	m_menu1 = new wxMenu();
	m_menu11 = new wxMenu();
	wxMenuItem* m_menu11Item = new wxMenuItem( m_menu1, wxID_ANY, wxT("MyMenu"), wxEmptyString, wxITEM_NORMAL, m_menu11 );
	m_menu1->Append( m_menu11Item );
	
	m_menu21 = new wxMenu();
	wxMenuItem* m_menu21Item = new wxMenuItem( m_menu1, wxID_ANY, wxT("MyMenu"), wxEmptyString, wxITEM_NORMAL, m_menu21 );
	m_menu1->Append( m_menu21Item );
	
	m_menu31 = new wxMenu();
	wxMenuItem* m_menu31Item = new wxMenuItem( m_menu1, wxID_ANY, wxT("MyMenu"), wxEmptyString, wxITEM_NORMAL, m_menu31 );
	m_menu1->Append( m_menu31Item );
	
	m_menubar1->Append( m_menu1, wxT("MyMenu") ); 
	
	m_menu2 = new wxMenu();
	m_menubar1->Append( m_menu2, wxT("MyMenu") ); 
	
	m_menu3 = new wxMenu();
	m_menubar1->Append( m_menu3, wxT("MyMenu") ); 
	
	this->SetMenuBar( m_menubar1 );
	
	
	this->Centre( wxBOTH );
}

Main::~Main()
{
}
