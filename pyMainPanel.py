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
		#search_result_box = self.config_search_result()
		mylist = MyListCtrl(self, -1)

		mainbox = wx.BoxSizer(wx.VERTICAL)
		mainbox.Add(search_argu_box, 0)
		mainbox.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 10)
		#mainbox.Add(search_result_box, 1, wx.EXPAND)
		mainbox.Add(mylist, 1, wx.EXPAND)

		self.SetSizer(mainbox)
		mainbox.Fit(self)


	
	def config_argu_ui(self):
		'''
		service_lb = wx.StaticText(self, -1, 'Total Service Found: ')
		self.service_found = wx.TextCtrl(self, -1, '')
		self.service_found.Enable(False)

		service_box = wx.BoxSizer(wx.HORIZONTAL)
		service_box.Add(service_lb, 0)
		service_box.Add(self.service_found, 0)

		auto_box = self.create_auto_widgets(self)

		box = wx.BoxSizer(wx.HORIZONTAL)
		#box.Add(auto_box, wx.ALL, 10)
		box.Add(auto_box, 0)

		mainbox = wx.BoxSizer(wx.VERTICAL)
		mainbox.Add(box, 0)
		mainbox.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 10)
		mainbox.Add(service_box, 0)

		self.SetSizer(mainbox)
		mainbox.Fit(self)
		'''

		set_co_b = wx.Button(self, label='Find Files In')
		set_sti_b = wx.Button(self, label='Browse')
		auto_search_b = wx.Button(self, label='Files Type')

		argu_ui_box = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
		argu_ui_box.Add(set_co_b)
		argu_ui_box.Add(set_sti_b)
		argu_ui_box.Add(auto_search_b)

		return argu_ui_box


	def config_search_result(self):
		'''
		set_co_b = wx.Button(self, label='Set Country')
		set_sti_b = wx.Button(self, label='Set STI')
		auto_search_b = wx.Button(self, label='Auto Search')

		argu_ui_box = wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
		argu_ui_box.Add(set_co_b)
		argu_ui_box.Add(set_sti_b)
		argu_ui_box.Add(auto_search_b)
		'''

		panel = wx.Panel(self)
		mylist = MyListCtrl(panel, -1)
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(panel, 1, wx.EXPAND) #|wx.TOP)
		#box.Fit(self)
		return box


	def create_auto_widgets(self, parent):
		set_co_b = wx.Button(parent, label='Set Country')
		set_sti_b = wx.Button(parent, label='Set STI')
		auto_search_b = wx.Button(parent, label='Auto Search')

		search_pro_lb = wx.StaticText(parent, -1, 'Search Progress: ')
		self.process_gauge = wx.Gauge(parent, -1, 100)
		#self.gauge.SetBezelFace(3)
		#self.gauge.SetShadowWidth(3)

		self.Bind(wx.EVT_BUTTON, self.onSetCountry, set_co_b)
		self.Bind(wx.EVT_BUTTON, self.onSetFTI, set_sti_b)
		self.Bind(wx.EVT_BUTTON, self.onAutoSearch, auto_search_b)

		#co_sti_box = wx.BoxSizer(wx.HORIZONTAL)
		#co_sti_box.Add(set_co_b, 0)
		#co_sti_box.Add(set_sti_b, 0)

		search_box = wx.BoxSizer(wx.VERTICAL)
		#search_box.Add(co_sti_box, 0)
		search_box.Add(set_co_b, 0)
		search_box.Add(set_sti_b, 0)
		search_box.Add(auto_search_b, 0)

		process_box = wx.BoxSizer(wx.HORIZONTAL)
		process_box.Add(search_pro_lb, 0)
		process_box.Add(self.process_gauge, 0)

		#main_box = wx.BoxSizer(wx.VERTICAL)
		sbox = wx.StaticBox(self, -1, "Auto Search")
		main_box = wx.StaticBoxSizer(sbox, wx.VERTICAL)

		#main_box.Add(search_box, wx.ALL, 20)
		#main_box.Add(process_box, wx.ALL, 20)
		main_box.Add(search_box, 0)
		main_box.Add(process_box, 0)

		return main_box


	def mypass(self, event): pass

	def key_send(self, data):
		s = chr(0x55) + str(data) + chr(0xAA)
		print 'the length of send str is: ',
		print len(s)
		print_str(s)


	def onSetCountry(self, event):
		pass


	def onSetFTI(self, event):
		FTI_str = chr(0x11) + chr(0x03)
		self.key_send(FTI_str)


	def onAutoSearch(self, event):
		auto_search_str = chr(0x11) + chr(0x01) + chr(self.auto_search_flag)
		self.key_send(auto_search_str)
		self.auto_search_flag = not self.auto_search_flag


	def onSetChannelNum(self, event):
		channel = wx.GetNumberFromUser("Enter a number (between 21~68):", "", 
				caption="Input Channel Number", value=21, min=21, max=68, parent=None)
		if channel != -1:
			print "you set channel as %d" %channel
			channel_str = chr(0x12) + chr(0x01) + chr(channel)
			self.key_send(channel_str)



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
