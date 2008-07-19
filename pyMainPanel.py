#!/usr/bin/python

import sys, os, time
import wx


class MyListCtrl(wx.ListCtrl):
	def __init__(self, parent, id):
		wx.ListCtrl.__init__(self, parent, id, style=wx.LC_REPORT)

		self.InsertColumn(0, "Name")
		self.InsertColumn(1, "Size")
		self.InsertColumn(2, "Date Modified")
		self.InsertColumn(3, "Directory")

		self.SetColumnWidth(0, 160)
		self.SetColumnWidth(1, 80)
		self.SetColumnWidth(2, 160)
		#self.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)
		self.SetColumnWidth(3, 300)

		self.set_value()


	def set_value(self):
		row = 0
		files = os.listdir('.')
		for file in files:
			self.InsertStringItem(row, os.path.basename(file))
			self.SetStringItem(row, 1, str(os.path.getsize(file)))
			self.SetStringItem(row, 2, time.ctime(os.path.getmtime(file)))
			self.SetStringItem(row, 3, os.getcwd() + os.path.dirname(file))
			row += 1



class pyMainPanel(wx.Panel):
	def __init__(self, parent=None, id=-1):
		wx.Panel.__init__(self, parent, id)
		#self.SetBackgroundColour('White')
		self.create_widgets()

	
	def create_widgets(self):
		search_argu_box = self.config_argu_ui()
		mylist = MyListCtrl(self, -1)

		mainbox = wx.BoxSizer(wx.VERTICAL)
		mainbox.Add(search_argu_box, 0)
		mainbox.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 10)
		mainbox.Add(mylist, 1, wx.EXPAND)

		self.SetSizer(mainbox)
		mainbox.Fit(self)


	
	def config_argu_ui(self):
		set_co_b = wx.Button(self, label='Find Files In')
		set_sti_b = wx.Button(self, label='Browse')
		auto_search_b = wx.Button(self, label='Files Type')

		self.Bind(wx.EVT_BUTTON, self.onFind, set_co_b)
		self.Bind(wx.EVT_BUTTON, self.onBrowse, set_sti_b)
		self.Bind(wx.EVT_BUTTON, self.onFilesType, auto_search_b)

		argu_ui_box = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
		argu_ui_box.Add(set_co_b)
		argu_ui_box.Add(set_sti_b)
		argu_ui_box.Add(auto_search_b)

		return argu_ui_box


	def mytest(self, parent):
		#sbox = wx.StaticBox(self, -1, "Auto Search")
		#main_box = wx.StaticBoxSizer(sbox, wx.VERTICAL)
		pass

	def mypass(self, event): pass


	def onNotImplemented(self, name):	
		wx.MessageBox('Sorry. Not implemented yet...', 
				name, wx.OK | wx.ICON_INFORMATION, self)
		
	def onFind(self, event):	
		self.onNotImplemented('Find')
		
	def onBrowse(self, event):	
		self.onNotImplemented('Find')
		
	def onFilesType(self, event):	
		self.onNotImplemented('Open Dir')

	def onOpenDir(self, event):	
		self.onNotImplemented('Open Dir')


class testFrame(wx.Frame):
	def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition, size=wx.DefaultSize):
		wx.Frame.__init__(self, parent, -1, pos=pos, size=size)
		self.panel = pyMainPanel(self)

class MyApp(wx.App):
	def OnInit(self):
		self.frame = testFrame(pos=(300,120), size=(600, 400))
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True


if __name__ == '__main__':
	myapp = MyApp()
	myapp.MainLoop()
