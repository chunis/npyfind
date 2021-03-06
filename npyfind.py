#!/usr/bin/python
# -*- coding: utf-8 -*-

"Another PyFind implemented by WxPython"

import wx
#import os, sys
#import glob, shutil, thread
from pyMainPanel import pyMainPanel, save_config, restore_config
from pySketch import pySketch


Name	= 'NPyFind'
Version	= '0.0.1-dev'
Author	= 'Deng Chunhui'
Email	= 'chunchengfh@gmail.com'
Date	= '2008.05.22'


class MyFrame(wx.Frame):
	"Main frame for NPyFind"

	def __init__(self, parent=None, id=-1, title='NPyFind',
			pos=wx.DefaultPosition, size=wx.DefaultSize):
		wx.Frame.__init__(self, None, -1, title, pos, size)
		self.panel = wx.Panel(self)
		#self.panel.SetBackgroundColour('white')
		self.nb = wx.Notebook(self.panel)

		self.createMenuBar()
		self.createStatusBar()
		self.createToolBar()
	
		self.main_panel_frame = pyMainPanel(self.nb)
		self.filter_frame = pySketch(self.nb)
		self.more_options_frame = pySketch(self.nb)
		self.link_tools_frame = pySketch(self.nb)

		self.nb.AddPage(self.main_panel_frame, "Main")
		self.nb.AddPage(self.filter_frame, "Filter Result")
		self.nb.AddPage(self.more_options_frame, "More Options")
		self.nb.AddPage(self.link_tools_frame, "Link Tools")

		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(self.nb, 1, wx.EXPAND)
		self.panel.SetSizer(box)
		box.Fit(self)


	def menu_data(self):
		return [ ("&File", (
				("&Save Result", "Save Search Result", self.mypass),
				("", "", ""),
				("C&onfigure...", "Configure Search Options", self.mypass),
				("", "", ""),
				("&Close", "Close this tool", self.onExit))),
			 ("&Action", (
				("&Find", "Find", self.mypass),
				("&Open", "Open", self.mypass),
				("&Open Dir", "Open Dir", self.mypass),
				("&Copy To", "Copy Selected Files to Another Place", self.mypass),
				("&Delete", "Delete Selected Files", self.mypass),
				("", "", ""),
				("&Clear Result\tCTRL-Q", "Clear Search Result", self.onClearResult))),
			 ("&Help", (
				("&Help Contents\tF1", "Help of this tool", self.onHelp),
				("&About", "About this tool", self.onAbout))) ]


	def createMenuBar(self):
		menuBar = wx.MenuBar()
		for eachMenuData in self.menu_data():
			menuLabel = eachMenuData[0]
			menuItems = eachMenuData[1]
			menuBar.Append(self.createMenu(menuItems), menuLabel)
		self.SetMenuBar(menuBar)
	
	
	def createMenu(self, menuitems):
		menu = wx.Menu()
		for each_menu in menuitems:
			if each_menu[0] == '':
				menu.AppendSeparator()
			else:
				tmpmenu = menu.Append(wx.NewId(), each_menu[0], each_menu[1])
				self.Bind(wx.EVT_MENU, each_menu[2], tmpmenu)

		return menu


	def mypass(self, event):
		pass

	def createToolBar(self):
		toolbar = self.CreateToolBar()
		#toolbar.AddLabelTool(-1, '', wx.Bitmap('images/tux.png'))
		toolbar.AddLabelTool(-1, '', wx.Bitmap('images/find.png'))
		#toolbar.AddLabelTool(-1, '', wx.Bitmap('images/configure.png'))
		toolbar.Realize()

	def createStatusBar(self):
		self.CreateStatusBar()
		self.SetStatusText('Welcome to use NPyFind!')

	
	def toolBarData(self):
		pass

	
	def onClearResult(self, event):
		self.main_panel_frame.onClearResult(event)


	def onHelp(self, event):
		wx.MessageBox('Sorry, No help yet', 'Help', wx.OK | wx.ICON_INFORMATION, self)

	def onAbout(self, event):
		about = (Name 	+ '\nThis is another PyFind implemented by WxPython'
				+ '\n\nVersion: ' + Version
				+ '\n Author: ' + Author 
				+ '\n Email: ' + Email 
				+ '\n Date:\t' + Date)
		wx.MessageBox(about, 'About %s' %Name, wx.OK | wx.ICON_INFORMATION, self)

	def onExit(self, event):	
		save_config()
		self.Close()
		
		

class NPyFind(wx.App):
	"Main App for NPyFind"

	def OnInit(self):
		restore_config()
		self.frame = MyFrame(self, size=(700, 500))
		self.frame.Center()
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

#	thread.start_new(myprint, ())

if __name__ == '__main__':
	nPyFind = NPyFind(False)
	nPyFind.MainLoop()
