#!/usr/local/bin/python3
import wx
import os
from random import randint
from dot_helper import sqauresBoard

class MyFrame(wx.Frame):
    def __init__(self, **kwargs):
        w,h = kwargs['size']
        w += kwargs['gutter'] * 2
        h += kwargs['gutter'] * 4
        super().__init__(parent=kwargs['parent'], 
                         title=kwargs['title'],
                         size = (w,h))
        
        self.width,self.height = kwargs['size']

        self.board = sqauresBoard(players=kwargs['players'], 
                         width=self.width,
                         height = self.height,
                         gap = kwargs['gap'],
                         gutter = kwargs['gutter'],
                         dot_size = kwargs['dot_size'],
                         dot_color = kwargs['dot_color'])

        self.InitUI()

    def InitUI(self): 
        #print("initUI")
        self.panel = wx.Panel(self)
        self.panel.BackgroundColour = wx.WHITE
        self.panel.Bind(wx.EVT_LEFT_UP, self.onClick)
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint) 
        self.Centre() 
        self.Show(True)

    def OnPaint(self,e):
        #print("onpaint")
        self.dc = wx.PaintDC(self.panel) 
        # brush = wx.Brush(self.panel.BackgroundColour)  
        # self.dc.SetBackground(brush)  



        self.print_board()

      
    def print_board(self):
        self.dc.SetPen(wx.Pen('RED'))
        self.dc.SetBrush(wx.Brush('RED')) 
        for nid,node in self.board.nodes.items():
            x,y = node.coord
            size = node.size
            self.dc.DrawEllipse(x, y, size, size)

        self.dc.SetPen(wx.Pen('BLUE'))
        self.dc.SetBrush(wx.Brush('BLUE')) 
        for sid,neighbors in self.board.graph.items():
            x1,y1 = self.board.nodes[sid].coord
            for nid in neighbors:
                x2,y2 = self.board.nodes[nid].coord
                print("{}=>{}".format(sid,nid))
                self.dc.DrawLine(x1+1, y1+1, x2+1, y2+1)


    def onClick(self, event):
        x,y = event.GetPosition()

        self.board.select_edge(x,y)
        self.panel.Refresh()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(title='Dot Game', size=(500,500),parent=None,players=['a','b','c'],gap=20,gutter=50,dot_size=2,dot_color=(0,255,0))
    app.MainLoop()
