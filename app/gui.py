# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class wxVideoFrame
###########################################################################

class wxVideoFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelVideo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panelVideo, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre(wx.BOTH)
		#self.quote = wx.StaticText(self.m_panelVideo, label="Your quote:")
		# self.result = wx.StaticText(self.m_panelVideo, label="")
		# self.result.SetForegroundColour(wx.RED)
		# self.button = wx.Button(self.m_panelVideo, label="Save",pos=(10, 50))
		# #self.lblname = wx.StaticText(self.m_panelVideo, label="Your name:")
		# self.editname = wx.TextCtrl(self.m_panelVideo,pos=(10, 10) ,size=(140, -1))

        # # Set sizer for the frame, so we can change frame size to match widgets
		# self.windowSizer = wx.BoxSizer(wx.VERTICAL )
		# self.windowSizer.Add(self.m_panelVideo, 1, wx.ALL | wx.EXPAND)

        # # Set sizer for the panel content
		# self.sizer = wx.GridBagSizer(5, 5)
		# #self.sizer.Add(self.quote, (0, 0))
		# self.sizer.Add(self.result, (0, 1))
		# #self.sizer.Add(self.lblname, (1, 0))
		# self.sizer.Add(self.editname, (1, 1))
		# self.sizer.Add(self.button, (2, 0), (1, 2), flag=wx.EXPAND)

        # # Set simple sizer for a nice border
		# #self.border = wx.BoxSizer()
		# #self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # # Use the sizers
		# #self.panel.SetSizerAndFit(self.border)  
		# self.SetSizerAndFit(self.windowSizer)  

        # # Set event handlers
		# self.button.Bind(wx.EVT_BUTTON, self.OnButton)

	def OnButton(self, e):
		self.result.SetLabel(self.editname.GetValue())
	
	def __del__( self ):
		pass
	

