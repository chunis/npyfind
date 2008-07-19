#!/usr/bin/python

import sys, os, time
import wx


class MyListCtrl(wx.ListCtrl):
	def __init__(self, parent, id):
		wx.ListCtrl.__init__(self, parent, id, style=wx.LC_REPORT)

		self.InsertColumn(0, "Name", width=160)
		self.InsertColumn(1, "Size", format=wx.LIST_FORMAT_RIGHT, width=80)
		self.InsertColumn(2, "Date Modified", format=wx.LIST_FORMAT_RIGHT, width=160)
		self.InsertColumn(3, "Directory", width=300)

		self.set_value()


	def set_value(self):
		row = 0
		files = os.listdir('.')
		for file in files:
			self.InsertStringItem(row, os.path.basename(file))
			self.SetStringItem(row, 1, str(os.path.getsize(file)) + ' B')
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
		mainbox.Add(search_argu_box, 0, wx.EXPAND)
		mainbox.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 10)
		mainbox.Add(mylist, 1, wx.EXPAND)

		self.SetSizer(mainbox)
		mainbox.Fit(self)


	
	def config_argu_ui(self):
		find_st = wx.StaticText(self, label='Find Files In')
		name_st = wx.StaticText(self, label='File Specification')
		type_st = wx.StaticText(self, label='File Type')

		dir_tc = wx.TextCtrl(self, -1)
		brws_btn = wx.Button(self, label='Browse')
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(dir_tc, 1)
		hbox.Add(brws_btn)

		name_tc = wx.TextCtrl(self, -1)
		type_tc = wx.TextCtrl(self, -1)

		search_subdir_cb = wx.CheckBox(self, -1, 'Search Sub Dirs')
		case_sensitive_cb = wx.CheckBox(self, -1, 'Case Sensitive')
		find_btn = wx.Button(self, label='Find Now!')

		self.Bind(wx.EVT_BUTTON, self.onBrowse, brws_btn)
		self.Bind(wx.EVT_BUTTON, self.onFind, find_btn)

		argu_ui_box = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
		argu_ui_box.AddGrowableCol(1, 1)

		argu_ui_box.AddMany([
			(find_st), (hbox, 1, wx.EXPAND), (search_subdir_cb),
			(name_st), (name_tc, 1, wx.EXPAND), (case_sensitive_cb),
			(type_st), (type_tc, 1, wx.EXPAND), (find_btn) ])

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
