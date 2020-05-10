import tkinter as tk
from tkinter import *
from tkinter import ttk, colorchooser,filedialog
import glob
from main import process
from gui.shape_drawer import *
from gui.image_handler import *

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 800

class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.shape_drawer = ShapeDrawer(self.c)
        self.image_handler = ImageHandler(self.c)


    def changeW(self,e): #change Width of pen through slider
        self.shape_drawer.set_pen_width(e)

    def clear(self):
        self.c.delete(ALL)

    def change_fg(self):  #changing the pen color
        self.shape_drawer.set_color()

    def change_bg(self):  #changing the background color canvas
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg
        
    def load_image(self,filename=""):
        self.image_handler.load_image(filename)
        
    def save_image(self):
        self.image_handler.save_image(process)
            
    def undo(self):
        self.shape_drawer.undo()
            
    def set_shape(self,shape):
        self.shape_drawer.setShape(shape)
        
    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Pen Width:',font=('arial 18')).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 2, to = 50,command=self.changeW,orient=VERTICAL)
        #self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=1,ipadx=30)
        self.controls.pack(side=LEFT)
        
        self.c = Canvas(self.master,width=CANVAS_WIDTH,height=CANVAS_HEIGHT,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)

        colormenu = Menu(menu)
        menu.add_cascade(label='Colors',menu=colormenu)
        colormenu.add_command(label='Brush Color',command=self.change_fg)
        colormenu.add_command(label='Background Color',command=self.change_bg)

        optionmenu = Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas',command=self.clear)
        optionmenu.add_command(label='Exit',command=self.master.destroy) 

        imagemenu = Menu(menu)
        menu.add_cascade(label = "Images",menu=imagemenu)
        imagemenu.add_command(label="Load Image",command = self.load_image)
        imagemenu.add_command(label="Save Image",command = self.save_image)

        editmenu = Menu(menu)
        menu.add_cascade(label = "Edit",menu = editmenu)
        editmenu.add_command(label="Undo",command=self.undo)
        
        shapesmenu = Menu(menu)
        menu.add_cascade(label = "Shapes",menu = shapesmenu)
        shapesmenu.add_command(label="Freehand",command=lambda : self.set_shape("freehand"))
        shapesmenu.add_command(label="Rectangle",command=lambda : self.set_shape("rectangle"))
        shapesmenu.add_command(label="Oval",command=lambda : self.set_shape("oval"))
        #image_files = glob.glob("../../data/*")
        #print(image_files)
        #j = 0
        #for i in range(len(image_files)):
        #    file = image_files[i]
        #    j += 1  
        #    imagemenu.add_command(label=file[11:],command=lambda:self.load_image(str(j)))
        

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Application')
    root.resizable(False, False)

    root.mainloop()