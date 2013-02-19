# !/usr/bin/env python
# coding:utf-8

import os
import wx

"""
	Simple Command Launcher.

	create 2013/01/22
	auther H.Murashige
	version 0.1.0
	
"""
class CmdLauncher(wx.Frame):


	"""
		build a command-line window.
	"""
	def __init__(self, parent, title):
		self.List = []
		Frm = wx.Frame(None, -1, "CmdLauncher", size=(400,50),pos=(400,400))
		self.TxtCtr = wx.TextCtrl(Frm, -1)
		self.TxtCtr.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
		self.lbFrame = wx.Frame(None, 0, "wxPython", size=(420,200),pos=(400,448),style=wx.DOUBLE_BORDER)
        	self.LBox = wx.ListBox(self.lbFrame, -1, choices = self.List, size=(415,200))
		Frm.Show()
		self.TxtCtr.SetFocus()

	"""
		handling the key.
	"""
	def OnKeyDown(self,event):
		key = event.GetKeyCode()
		input = self.TxtCtr.GetValue()
		input = os.path.normpath(os.path.normcase(input))
		select = self.LBox.GetStringSelection()
		if key ==  wx.WXK_ESCAPE:
			wx.Exit()
		elif key == wx.WXK_TAB:
			self.TxtCtr.Clear()
			self.TxtCtr.SetValue(select)
			self.TxtCtr.SetFocus()
		elif key == wx.WXK_UP:
			count = self.LBox.GetCount()
			next = self.LBox.GetSelection() - 1
			if next >=  0:
				self.LBox.SetSelection(next)
			else: self.LBox.SetSelection(count - 1)
		elif key == wx.WXK_DOWN:
			count = self.LBox.GetCount()
			next = self.LBox.GetSelection() + 1
			if next < count:
				self.LBox.SetSelection(next)
			else: self.LBox.SetSelection(0)
		elif key == wx.WXK_RETURN:
			self.TxtCtr.Clear()
			self.TxtCtr.SetValue(select)
			self.lbFrame.Hide()
			if os.path.isdir(select) :
				os.system("explorer " + select)
			else:
				os.system(select)
		else:
			if input != "" and os.path.exists(input) :
				if SearchExist(self, input):
					event.Skip()
				else:
					self.LBox.Clear()
					self.lbFrame.Show()
					files = os.listdir(input)
					for file in files:
						if os.path.isdir(file):
							self.LBox.Append(input + os.sep + file + os.sep)
						else:
							self.LBox.Append(input + os.sep + file)
					self.TxtCtr.SetFocus()
					event.Skip()
			else:
				event.Skip()

def SearchExist(self, target):
	for i in self.LBox.GetItems():
		if i == target :
			return True

def main():
	app = wx.App(False)
        launcher = CmdLauncher(None, 'My CmdLauncher')
	app.MainLoop()

if __name__ == '__main__':
    main()



#	dlg = wx.MessageDialog( self.lbFrame, inputValue, "Value", wx.OK)
#	dlg.ShowModal()
#	dlg.Destroy()

