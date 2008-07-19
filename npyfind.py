#!/usr/bin/python
# -*- coding: gb2312 -*-

# Name:   NPyFind
# Author: Deng Chunhui
# Email:  chunchengfh@gmail.com'

"Another PyFind implemented by WxPython"

import wx
#import os, sys
#import glob, shutil, thread
import pyfind_core
from pyMainPanel import pyMainPanel
from pySketch import pySketch


Name	= 'NPyFind'
Version	= '0.0.1-dev'
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
		#box.Fit(self)


	def menu_data(self):
		return [ ("&File", (
				("&Save Result", "Save Search Result", self.mypass),
				("", "", ""),
				("&Configure...", "Configure Search Options", self.mypass),
				("", "", ""),
				("&Close", "Close this tool", self.onExit))),
			 ("&Action", (
				("&Find", "Find", self.mypass),
				("&Open", "Open", self.mypass),
				("&Open Dir", "Open Dir", self.mypass),
				("&Copy To", "Copy Selected Files to Another Place", self.mypass),
				("&Delete", "Delete Selected Files", self.mypass),
				("", "", ""),
				("&Clear Result", "Clear Search Result", self.mypass))),
			 ("&Help", (
				("&About", "About this tool", self.onAbout),
				("&Close", "Close this tool", self.onExit))) ]


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
		toolbar.Realize()

	def createStatusBar(self):
		self.CreateStatusBar()
		self.SetStatusText('Welcome to use NPyFind!')

	
	def toolBarData(self):
		pass

	
	def onAbout(self, event):
		about = pyfind_core.myabout(Name, Version, Date)
		wx.MessageBox(about, 'About %s' %Name, wx.OK | wx.ICON_INFORMATION, self)

	def onExit(self, event):	
		self.Close()
		
		

class NPyFind(wx.App):
	"Main App for NPyFind"

	def OnInit(self):
		self.frame = MyFrame(self, size=(700, 500))
		self.frame.Center()
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

#	thread.start_new(myprint, ())

if __name__ == '__main__':
	nPyFind = NPyFind(False)
	nPyFind.MainLoop()
