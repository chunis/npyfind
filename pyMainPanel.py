#!/usr/bin/python

import sys, os, time
import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
from wx.lib.mixins.listctrl import ColumnSorterMixin
import glob


def recu_find(path, file, recu):
	tmp = [ ]
	result = [ ]

	old_dir = os.getcwd()
	new_dir = os.path.join(old_dir, path)
	os.chdir(new_dir)
	
	books=glob.glob(file)
	for book in books:
		result.append(os.path.join(new_dir, book))
#		print book

	if recu == 1:
		for filepath in os.listdir('.'):
			if os.path.isdir(filepath):
				tmp = recu_find(filepath, file, recu)

	# if there are search result from sub dirs, add them
	if tmp: result.extend(tmp)

	os.chdir(old_dir)
	return result


class MyListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin, ColumnSorterMixin):
	def __init__(self, parent, id):
		wx.ListCtrl.__init__(self, parent, id, style=wx.LC_REPORT)
		ListCtrlAutoWidthMixin.__init__(self)
		ColumnSorterMixin.__init__(self, 6)
		self.itemDataMap = {}

		self.InsertColumn(0, "Name", width=160)
		self.InsertColumn(1, "Size", format=wx.LIST_FORMAT_RIGHT, width=80)
		self.InsertColumn(2, "Date Modified", format=wx.LIST_FORMAT_RIGHT, width=160)
		self.InsertColumn(3, "Directory", width=300)

	def GetListCtrl(self):
		return self

	def set_value(self, files):
		for file in files:
			name = os.path.basename(file)
			size = str(os.path.getsize(file)) + ' B'
			ctime = time.ctime(os.path.getmtime(file))
			dir = os.path.dirname(file)

			item = (name, size, ctime, dir)
			index = self.InsertStringItem(sys.maxint, item[0])
			for col, text in enumerate(item[1:]):
				self.SetStringItem(index, col+1, text)
			self.SetItemData(index, index)
			self.itemDataMap[index] = item


class pyMainPanel(wx.Panel):
	def __init__(self, parent=None, id=-1):
		wx.Panel.__init__(self, parent, id)
		#self.SetBackgroundColour('White')
		self.create_widgets()

	
	def create_widgets(self):
		search_argu_box = self.config_argu_ui()
		self.mylist = MyListCtrl(self, -1)

		self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onOpenItem, self.mylist)

		mainbox = wx.BoxSizer(wx.VERTICAL)
		mainbox.Add(search_argu_box, 0, wx.EXPAND)
		mainbox.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 10)
		mainbox.Add(self.mylist, 1, wx.EXPAND)

		self.SetSizer(mainbox)
		mainbox.Fit(self)


	
	def config_argu_ui(self):
		find_st = wx.StaticText(self, label='Find Files In')

		#self.dir_tc = wx.TextCtrl(self, -1)
		self.dir_tc = wx.TextCtrl(self, -1, value='/home/denny/sunny/books')
		brws_btn = wx.Button(self, label='Browse')
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		hbox.Add(self.dir_tc, 1)
		hbox.Add(brws_btn)

		self.search_subdir_cb = wx.CheckBox(self, -1, 'Search Sub Dirs')
		self.search_subdir_cb.SetValue(True)

		name_st = wx.StaticText(self, label='File Specification')
		#self.name_tc = wx.TextCtrl(self, -1)
		self.name_tc = wx.TextCtrl(self, -1, value='ython')
		self.case_sensitive_cb = wx.CheckBox(self, -1, 'Case Sensitive')
		self.case_sensitive_cb.Disable()

		type_st = wx.StaticText(self, label='File Type')
		#self.type_tc = wx.TextCtrl(self, -1)
		self.type_tc = wx.TextCtrl(self, -1, value='*')
		find_btn = wx.Button(self, label='Find Now!')


		self.Bind(wx.EVT_BUTTON, self.onBrowse, brws_btn)
		self.Bind(wx.EVT_BUTTON, self.onFind, find_btn)
		#self.Bind(wx.EVT_CHECKBOX, self.onSubdir, search_subdir_cb)
		#self.Bind(wx.EVT_CHECKBOX, self.onCaseSen, case_sensitive_cb)

		argu_ui_box = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
		argu_ui_box.AddGrowableCol(1, 1)

		argu_ui_box.AddMany([
			(find_st, 0, wx.ALIGN_RIGHT),
			(hbox, 1, wx.EXPAND),
			(self.search_subdir_cb),

			(name_st, 0, wx.ALIGN_RIGHT),
			(self.name_tc, 1, wx.EXPAND),
			(self.case_sensitive_cb),

			(type_st, 0, wx.ALIGN_RIGHT),
			(self.type_tc, 1, wx.EXPAND),
			(find_btn) ])

		return argu_ui_box


	def onOpenItem(self, event):
		item = event.GetItem()
		print 'Selected %s' %item.GetText()


	def mytest(self, parent):
		#sbox = wx.StaticBox(self, -1, "Auto Search")
		#main_box = wx.StaticBoxSizer(sbox, wx.VERTICAL)
		pass

	def mypass(self, event): pass


	def onNotImplemented(self, name):	
		wx.MessageBox('Sorry. Not implemented yet...', 
				name, wx.OK | wx.ICON_INFORMATION, self)
		
	def onBrowse(self, event):	
		dir = wx.DirDialog(None, "Choose a Directory:")
		if dir.ShowModal() == wx.ID_OK:
			self.searchdir = dir.GetPath()
			self.dir_tc.SetValue(self.searchdir)
			print self.searchdir
		dir.Destroy()

	def onFind(self, event):	
		subdir_flag = self.search_subdir_cb.GetValue()
		case_flag = self.case_sensitive_cb.GetValue()
		tmpdir = self.dir_tc.GetValue()
		tmp_name_spec = self.name_tc.GetValue()
		tmp_file_type = self.type_tc.GetValue()

		if not os.path.isdir(tmpdir):
			wx.MessageBox('The Search Directory doesn\'t exist!\n'
					'Please correct it first',
					'Wrong Path', wx.OK | wx.ICON_INFORMATION, self)

		if tmp_name_spec == '':
			wx.MessageBox('Is the Name Specification Empty?',
					'No Name Specification', wx.OK | wx.ICON_INFORMATION, self)

		print subdir_flag, case_flag
		print tmpdir, tmp_name_spec, tmp_file_type
		
		file_pattern = '*' + tmp_name_spec + '*.' + tmp_file_type
		print file_pattern

		search_result = recu_find(tmpdir, file_pattern, subdir_flag)
		#for file in search_result: print file
		self.mylist.set_value(search_result)


	def onSubdir(self, event):	
		self.onNotImplemented('Search Sub Dir')

	def onCaseSen(self, event):	
		self.onNotImplemented('Case Sensitive')

	def onFilesType(self, event):	
		self.onNotImplemented('Files Type')

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
