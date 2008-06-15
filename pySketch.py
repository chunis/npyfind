#!/usr/bin/python

import sys
import wx


class pySketch(wx.Panel):
	def __init__(self, parent=None, id=-1, tty=sys.stdout):
		wx.Panel.__init__(self, parent, id)
		#self.SetBackgroundColour('White')
		self.create_widgets()

	
	def create_widgets(self):
		pass
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


	def create_auto_widgets(self, parent):
		pass

	def mypass(self, event): pass

	def key_send(self, data):
		s = chr(0x55) + str(data) + chr(0xAA)
		print 'the length of send str is: ',
		print len(s)
		print_str(s)

		self.tty.tty_write(str(s))


	def onSetCountry(self, event):
		pass


	def onSetFTI(self, event):
		FTI_str = chr(0x11) + chr(0x03)
		self.key_send(FTI_str)


	def onAutoSearch(self, event):
		auto_search_str = chr(0x11) + chr(0x01) + chr(self.auto_search_flag)
		self.key_send(auto_search_str)
		self.auto_search_flag = not self.auto_search_flag


class testFrame(wx.Frame):
	def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition, size=wx.DefaultSize):
		wx.Frame.__init__(self, parent, -1, pos=pos, size=size)
		self.panel = pySketch(self)

class MyApp(wx.App):
	def OnInit(self):
		self.frame = testFrame(pos=(300,120), size=(320, 200))
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True


if __name__ == '__main__':
	myapp = MyApp()
	myapp.MainLoop()
