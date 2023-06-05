#!/usr/local/bin/python3
import wx
import os
from random import randint




class sqauresBoard():
    def __init__(self,width=500,height=500,cell_size=10):
        self.players = players
        self.width = 500
        self.height = 500
        self.cell_size = cell_size


    def generateSquares():
        pass



def fatPoint(dc,x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            dc.DrawPoint(x+j,y+i)
            

def printGrid(dc,w,h,gap):
    cols = int(w / gap)
    rows = int(h / gap)

    x = gap
    y = gap

    for r in range(rows):
        for c in range(cols):
            dc.DrawEllipse(x, y, 3, 3)
            x += gap
        x = gap
        y += gap


class MyFrame(wx.Frame):
    def __init__(self, title, size=(500,300),parent=None):
        super().__init__(parent=None, title=title,size = (500,300))
        self.width,self.height = size
        self.InitUI()

    def InitUI(self): 
        print("initUI")
        self.panel = wx.Panel(self)
        self.panel.BackgroundColour = wx.WHITE
        self.panel.Bind(wx.EVT_LEFT_UP, self.onClick)
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint) 
        self.Centre() 
        self.Show(True)

    def OnPaint(self,e):
        print("onpaint")
        self.dc = wx.PaintDC(self.panel) 
        # brush = wx.Brush(self.panel.BackgroundColour)  
        # self.dc.SetBackground(brush)  

        self.dc.SetPen(wx.Pen('RED'))
        self.dc.SetBrush(wx.Brush('RED')) 
        printGrid(self.dc,self.width,self.height,15)
        # for i in range(1000):
        #     w, h = self.panel.GetSize()
        #     x = randint(1, w-1)
        #     y = randint(1, h-1)
        #     #self.dc.DrawPoint(x, y)
        #     fatPoint(self.dc,x,y)

        #self.dc.Clear()
      


    def onClick(self, event):
        print(event)
        self.panel.Refresh()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame('Dot Game')
    app.MainLoop()
