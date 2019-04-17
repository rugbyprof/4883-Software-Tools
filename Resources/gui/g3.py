#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

This program draws a line in
a paint event.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""

import wx
from random import randint

def drawLine(**kwargs):
    if 'obj' in kwargs:
        obj = kwargs['obj']

    if 'width' in kwargs:
        width = kwargs['width']
    else:
        pass

    if 'height' in kwargs:
        height = kwargs['height']
    else:
        pass

    x1 = randint(0,width)
    y1 = randint(0,height)
    x2 = randint(0,width)
    y2 = randint(0,height)   

    dc = wx.PaintDC(obj)
    dc.DrawLine(x1, y1, x2, y2)

class Dispatcher():
    def __init__(self):
        self.functions = {}
        self.callQueue = []
    
    def registerFunction(self,label,f):
        self.functions[label] = f

    def push(self,fname,args):
        d = {'name':fname,'args':args}
        self.callQueue.append(d)
    
    def runQueue(self):
        print(self.functions)
        print(self.callQueue)
        for f in self.callQueue:
            self.functions[f['name']](**f['args'])



class MyFrame(wx.Frame):

    def __init__(self, title, size=(500,300),parent=None):
        super().__init__(parent=None, title=title,size = (500,300))
        self.InitUI(title)
        
        self.width,self.height = size

        self.d = Dispatcher()
        self.d.registerFunction('drawLine',drawLine)
        self.d.push('drawLine',{'obj':self})

    def InitUI(self,title):

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetTitle(title)
        self.Centre()

    def OnPaint(self, e):
        drawLine(obj=self,width=500,height=300)
        print(self.d)
        for i in range(10):
            self.d.runQueue()



def main():

    app = wx.App()
    ex = MyFrame("Drawing Sh**")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()