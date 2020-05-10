import tkinter as tk
from tkinter import *

trace = 0 

class ShapeDrawer: 
    def __init__(self,canvas, parent=None):
        #self.canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart) 
        canvas.bind('<B1-Motion>',     self.onGrow)  
        canvas.bind('<Double-1>',      self.onClear) 
        canvas.bind('<ButtonPress-3>', self.onMove)  
        #canvas.bind('<ButtonRelease-1>',self.reset)
        self.canvas = canvas
        self.drawn  = None
        self.kinds = {"oval":canvas.create_oval, "rectangle":canvas.create_rectangle, "freehand":canvas.create_line}
        self.shape = "freehand"
        self.shape_create = self.kinds[self.shape]
        self.penwidth = 5
        self.color = 'black'
        self.undo_list = []

        
    def onStart(self, event):
        #self.shape = self.kinds[0]
        #self.kinds = self.kinds[1:] + self.kinds[:1] 
        self.start = event
        self.drawn = None
        self.undo_list.append([])
        print("in start",self.undo_list)
        
    def onGrow(self, event):                         
        canvas = event.widget
        if self.shape == "freehand":
            self.start = event
            objectId = self.shape_create(self.start.x, self.start.y, event.x, event.y,width=self.penwidth,capstyle=ROUND,smooth=True)
            self.add_to_undo(objectId)
            self.drawn = objectId
            
        else:            
            if self.drawn: 
                canvas.delete(self.drawn)
            objectId = self.shape_create(self.start.x, self.start.y, event.x, event.y,width=self.penwidth)
            self.add_to_undo(objectId)
            if trace: 
                print(objectId)
            self.drawn = objectId
        
    def add_to_undo(self,objectId):
        if len(self.undo_list) == 0:
            self.undo_list.append([])
        self.undo_list[-1].append(objectId)
        
    def onClear(self, event):
        event.widget.delete('all')
                   
    def onMove(self, event):
        if self.drawn:                               
            if trace: 
                print(self.drawn)
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event
            
    def setShape(self,shape):
        self.shape = shape
        self.shape_create = self.kinds[self.shape]
            
        
    def set_pen_width(self,width):
        self.penwidth = width 
        
    def set_color(self):
        self.color=colorchooser.askcolor(color=self.color)[1]
        
    def undo(self):
        obj = self.undo_list.pop()
        for i in obj:
            self.canvas.delete(i)
            

if __name__ == '__main__':
    canvas = Canvas(width=300, height=300, bg='beige') 
    canvas.pack()
    ShapeDrawer(canvas)

    tk.mainloop()