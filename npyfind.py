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


Name	= 'NPyFind'
Version	= '0.0.1-dev'
Date	= '2008.05.22'


class MyFrame(wx.Frame):
	"Main frame for NPyFind"

	def __init__(self, parent=None, id=-1, title='NPyFind',
			pos=wx.DefaultPosition, size=(450,300)):
		wx.Frame.__init__(self, None, -1, title, pos, size)
		self.panel = wx.Panel(self)
		self.SetBackgroundColour('white')
		self.createMenu()
		self.createStatusBar()
		self.createToolBar()
		self.createWorkArea()
		self.test()
	
	def createMenu(self):
		menuBar = wx.MenuBar()
		self.SetMenuBar(menuBar)

		menuAction = wx.Menu()
		menuAction.Append(10, '&Find')
		menuAction.AppendSeparator()
		menuAction.Append(20, '&Open Dir')
		self.Bind(wx.EVT_MENU, self.onFind, id=10)
		self.Bind(wx.EVT_MENU, self.onOpenDir, id=20)
		menuBar.Append(menuAction, '&Action')

		menuFile = wx.Menu()
		menuFile.Append(1, '&About...')
		menuFile.AppendSeparator()
		menuFile.Append(2, 'E&xit')
		self.Bind(wx.EVT_MENU, self.onAbout, id=1)
		self.Bind(wx.EVT_MENU, self.onExit, id=2)
		menuBar.Append(menuFile, '&About')

	def createStatusBar(self):
		self.CreateStatusBar()
		self.SetStatusText('Welcome to use NPyFind!')

	
	def toolBarData(self):
		pass

	def createToolBar(self):
		pass

	def createWorkArea(self):
		pass

	def test(self):
		button = wx.Button(self.panel, label='close', pos=(125, 20), size=(100, 30))
#		self.Bind(wx.EVT_BUTTON, self.onTest, button)
		self.Bind(wx.EVT_BUTTON, self.onExit, button)
	
	def onTest(self, event):
		self.SetTitle('Hello')

	def onAbout(self, event):
		about = pyfind_core.myabout(Name, Version, Date)
		wx.MessageBox(about, 'About %s' %Name, wx.OK | wx.ICON_INFORMATION, self)

	def onExit(self, event):	
		self.Close()
		
	def onNotImplemented(self, name):	
		wx.MessageBox('Sorry. Not implemented yet...', 
				name, wx.OK | wx.ICON_INFORMATION, self)
		
	def onFind(self, event):	
		self.onNotImplemented('Find')
		
	def onOpenDir(self, event):	
		self.onNotImplemented('Open Dir')
		

class NPyFind(wx.App):
	"Main App for NPyFind"

	def OnInit(self):
		self.frame = MyFrame(self)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

#	thread.start_new(myprint, ())





'''

class myScrolledList(ScrolledList):
	def runCommand(self, selection):
		for dir in dirnames:
#			print 'dir:', dir
			tmp_file = os.path.join(dir, selection)
#			print 'tmp_file:', tmp_file
			if os.path.exists(tmp_file):
				os.startfile(tmp_file)
				break


def myquit():
	try:
		cfg_file = open(CFG_FILE, 'w')
	except IOError, msg:
		pass
	else:
		cfg_file.write('dir=%s\n' %epath.get())
		cfg_file.write('type=%s\n' %etype.get())
		cfg_file.write('recu=%s\n' %var.get())
		cfg_file.close()

	root.quit()

def brws():
	global tmp_dir
	tmp_dir = askdirectory(initialdir = dirname)
#	print dirname
	if tmp_dir != '':
		epath.delete(0, END)
		epath.insert(0, tmp_dir)

def myclear():
	scroll.listbox.delete(0, END)

def myopen():
	file = scroll.listbox.get('active')
#	print dirnames
	for dir in dirnames:
#		print dir, 'good'
		tmp_file = os.path.join(dir, file)
#		print 'tmp_file:', tmp_file
		if os.path.exists(tmp_file):
			os.startfile(tmp_file)
			break

def myopen_dir():
	file = scroll.listbox.get('active')
	for dir in dirnames:
		tmp_file = os.path.join(dir, file)
		if os.path.exists(tmp_file):
#			print tmp_file
			file_dir = os.path.dirname(tmp_file)
			tmp_dir = os.getcwd()
			os.chdir(file_dir)
			os.startfile('.')
			os.chdir(tmp_dir)

def mycopy():
	file = scroll.listbox.get('active')
	for dir in dirnames:
		tmp_file = os.path.join(dir, file)
		if os.path.exists(tmp_file):
			tmp_dir = askdirectory()
#			print 'copy to: ' + tmp_dir
			shutil.copy(tmp_file, tmp_dir)


def recufind(path, allpath, file):
	if find_flag == False:
		lstatus.config(text='Find is canceled')
		return

	root_width = root.geometry().split('x')[0]
	lstatus.config(width=int(root_width), text='Find files in subdir: ' + allpath + '...')
	os.chdir(path)
	books=glob.glob(file)
	for book in books:
		result.append(allpath + '/' + book)
		scroll.listbox.insert('end', allpath.decode('gbk') + '/' + book.decode('gbk'))
#		print path + '/' + book
	for filepath in os.listdir('.'):
		if os.path.isdir(filepath):
			recufind(filepath, allpath+'/'+filepath, file)
	os.chdir('..')

def myFind():
	global find_flag
	if find_flag == True:
		find_flag = not find_flag
	else:
		prepare_find()

def prepare_find():
#	print dirname
	global dirname

	bfind.config(text='Cancel')

	dirname = epath.get()
	if not os.path.isdir(dirname):
		showerror('Wrong Path', 'The folder doesn\'t exist. Please correct it first')
		bfind.config(text='Find')
		return

	thread.start_new(real_find, ())


def real_find():
	global dirname
	global find_flag
	find_flag = True

	if dirname not in dirnames:
#		dirnames.append(dirname)
		dirnames[:0] = [ dirname ]
	os.chdir(dirname)
	type = etype.get()
	keywords = (ekeyword.get()).encode('gbk')
	recu = var.get()
	file = '*' + keywords + '*.' + type

	root_width = root.geometry().split('x')[0]
#	print 'root_width: '  + root_width
	lstatus.config(width=root_width, text='Find files in dir: ' + dirname + '...')

	global result
	result = [ ]
	books=glob.glob(file)
	for book in books:
		result.append(book)
		scroll.listbox.insert('end', book.decode('gbk'))
#		print book

	if recu == 1:
		for filepath in os.listdir('.'):
			if os.path.isdir(filepath):
				recufind(filepath, filepath, file)
	
	bfind.config(text='Find')
	if find_flag == True:
		lstatus.config(text='Find finished')
		find_flag = False
	

root = Tk()
root.title('PyFind-' + Version)
root.geometry('440x360+250+250')
root.config()
win1 = Frame(root)
win2 = Frame(root)
win3 = Frame(root)
win4 = Frame(root)
win5 = Frame(root)
win6 = Frame(root)	# status bar
#win1.config(width=60)
win1.pack(side=TOP, fill=X)
win2.pack(side=BOTTOM, fill=X)
win6.pack(side=BOTTOM, fill=X)
win3.pack(side=TOP, fill=X)
win4.pack(side=TOP, fill=X)
win5.pack(side=TOP, expand=YES, fill=BOTH)

CFG_FILE = os.path.join(os.getcwd(), 'pyfind.cfg')

# get last time's choices
try:
	cfg_file = open(CFG_FILE, 'r')
except IOError, msg:
	tmp_dir = dirname = ''
	type = '*'
	recu = 0
else:
	cfg = {}
	line = cfg_file.readline().rstrip()
	while line:
		options = line.split('=')
		try:
			cfg[options[0]] = options[1]
		except IndexError:
			pass
		line = cfg_file.readline().rstrip()
	cfg_file.close()
	tmp_dir = dirname = cfg.get('dir', '')
	type = cfg.get('type', '*')
	recu = int(cfg.get('recu', 0))

result = [ ]  # used for store result 
dirnames = [ ] # used for store old dirs
find_flag = False	# when in find process: true; else: false

font1 = ('times', 11, 'bold')
font2 = ('times', 13, 'bold')
font3 = ('times', 11, 'normal')

help_button = Button(win1, text='Help', command=myhelp)
help_button.config(bd=2, relief=GROOVE)
help_button.config(font=font1)

about_button = Button(win1, text='About', command=myabout)
about_button.config(bd=2, relief=GROOVE)
about_button.config(font=font1)

labelfont = ('times', 20, 'bold')
lname = Label(win1, text='PyFind', fg='blue')
lname.config(font=labelfont)

help_button.pack(side=LEFT, anchor='n')
about_button.pack(side=RIGHT, anchor='n')
lname.pack(fill=X, pady=20, anchor='s')

Label(win3, text='Find file in:', font=font3).pack(side=LEFT)

browse = Button(win3, text='Browse', command=brws)
browse.config(font=font3, anchor='e')
browse.pack(side=RIGHT, padx=6, pady=6) 
browse.focus()
browse.bind('<Return>', lambda event: brws())

epath = Entry(win3, width=40)
epath.pack(padx=5, side=LEFT, expand=YES, fill=X)
epath.delete(0, END)
epath.insert(0, dirname)

Label(win4, text='key word:', font=font3).pack(side=LEFT) #, anchor='e')
ekeyword = Entry(win4, width=20)
ekeyword.pack(padx=5, side=LEFT)
ekeyword.bind('<Return>', lambda event: myFind())

Label(win4, text='type:', font=font3).pack(side=LEFT) #, anchor='e')
etype = Entry(win4, width=6)
etype.insert(0, type)
etype.pack(padx=5, side=LEFT)
etype.bind('<Return>', lambda event: myFind())

var = IntVar()
#Checkbutton(win4, text='recursive', font=font3, variable=var).pack(padx=5, side=LEFT)
crecu=Checkbutton(win4, text='recursive', font=font3, variable=var)
crecu.pack(padx=5, side=LEFT)
crecu.bind('<Return>', lambda event: myFind())
var.set(recu)

scroll = myScrolledList('', win5)

lstatus = Label(win6, font=font3)
lstatus.config(relief=SUNKEN, padx=2, pady=2)
lstatus.pack(side=LEFT, expand=YES, fill=X)

bquit = Button(win2, text='Quit', command=myquit)
bquit.config(font=font2, padx=1)

bfind = Button(win2, text='Find', command=myFind)
bfind.config(font=font2, padx=1)
bclear = Button(win2, text='Clean', command=myclear)
bclear.config(font=font2, padx=1)
bopen = Button(win2, text='Open', command=myopen)
bopen.config(font=font2, padx=1)
bopen_dir = Button(win2, text='Open Dir', command=myopen_dir)
bopen_dir.config(font=font2, padx=1)
bcopy = Button(win2, text='Copy to', command=mycopy)
bcopy.config(font=font2, padx=1)

bfind.pack(side=RIGHT, padx=5, pady=3, anchor='s')
bquit.pack(side=LEFT, padx=5, pady=3, anchor='s')
bclear.pack(side=RIGHT, padx=5, pady=3, anchor='s')
bopen.pack(side=RIGHT, padx=5, pady=3, anchor='s')
bopen_dir.pack(side=RIGHT, padx=5, pady=3, anchor='s')
bcopy.pack(side=RIGHT, padx=5, pady=3, anchor='s')

root.mainloop()
'''


if __name__ == '__main__':
	nPyFind = NPyFind(False)
	nPyFind.MainLoop()
