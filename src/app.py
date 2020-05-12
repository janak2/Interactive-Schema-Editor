import tkinter as tk
from tkinter import *
from tkinter import ttk, colorchooser,filedialog
import glob
from main import process,detect
from gui.shape_drawer import *
from gui.image_handler import *
from config import *

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 800

COLORS_ROW = 0
PEN_SLIDER_ROW = 1
SHAPES_ROW = 2
EDIT_ROW = 3
IMAGE_LABEL_ROW = 4
IMAGE_ROW = 5

OLD_IMAGE_WIDTH = 500
OLD_IMAGE_HEIGHT = 500

class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 2
        self.drawWidgets()
        self.shape_drawer = ShapeDrawer(self.c)
        self.image_handler = ImageHandler(self.c)


    def changeW(self,e): #change Width of pen through slider
        self.shape_drawer.set_pen_width(e)

    def clear(self):
        self.c.delete(ALL)

    def change_fg(self,color=RED):  #changing the pen color
        self.shape_drawer.set_color(convert_BGR_to_hex(color))

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
        
    def update_image(self):
        self.image_handler.update_image(detect,self.old_image_label,
                                        OLD_IMAGE_WIDTH,OLD_IMAGE_HEIGHT)
        
        
    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Pen Width:',font=('arial 18')).grid(row=PEN_SLIDER_ROW,column=0)
        Label(self.controls, text='2',font=('arial 10')).grid(row=PEN_SLIDER_ROW,column=1)
        
        self.slider = ttk.Scale(self.controls,from_= 2, to = 50,command=self.changeW,orient=HORIZONTAL)
        #self.slider.set(self.penwidth)
        self.slider.grid(row=PEN_SLIDER_ROW,column=2,ipadx=30)
        Label(self.controls, text='50',font=('arial 10')).grid(row=PEN_SLIDER_ROW,column=3)
        self.controls.pack(side=LEFT)
        
        BUTTON_HEIGHT = 2
        BUTTON_WIDTH = 2
        
        Label(self.controls, text='Colors:',font=('arial 18')).grid(row=COLORS_ROW,column=0)

        self.b1 = Button(self.controls,text="Deletion",
                         command=lambda : self.change_fg(GREEN),
                         bg=convert_BGR_to_hex(GREEN),fg="white", 
                         height=BUTTON_HEIGHT).grid(row=COLORS_ROW,column=1,padx=10,pady=30)
        self.b2 = Button(self.controls,text="Insertion",
                         command=lambda : self.change_fg(RED),
                         bg=convert_BGR_to_hex(RED),fg="white",
                         height=BUTTON_HEIGHT).grid(row=COLORS_ROW,column=2,padx=10,pady=30)
        self.b3 = Button(self.controls,text="Arrows",
                         command=lambda : self.change_fg(BLUE),
                         bg=convert_BGR_to_hex(BLUE),fg="white",
                         height=BUTTON_HEIGHT).grid(row=COLORS_ROW,column=3,padx=10,pady=30)
        
        Label(self.controls, text='Shapes:',font=('arial 18')).grid(row=SHAPES_ROW,column=0)

        self.b4 = Button(self.controls,text="Freehand",
                         command=lambda : self.set_shape("freehand"),
                         height=BUTTON_HEIGHT).grid(row=SHAPES_ROW,column=1,padx=10,pady=30)
        self.b5 = Button(self.controls,text="Rectangle",
                         command=lambda : self.set_shape("rectangle"),
                         height=BUTTON_HEIGHT).grid(row=SHAPES_ROW,column=2,padx=10,pady=30)
        self.b6 = Button(self.controls,text="Oval",
                         command=lambda : self.set_shape("oval"),
                         height=BUTTON_HEIGHT).grid(row=SHAPES_ROW,column=3,padx=10,pady=30)
        self.b9 = Button(self.controls,text="Line",
                         command=lambda : self.set_shape("line"),
                         height=BUTTON_HEIGHT).grid(row=SHAPES_ROW,column=4,padx=10,pady=30)

        Label(self.controls, text='Edit:',font=('arial 18')).grid(row=EDIT_ROW,column=0)
        self.b7 = Button(self.controls,text="Undo",
                         command=self.undo,
                         height=BUTTON_HEIGHT).grid(row=EDIT_ROW,column=1,padx=10,pady=30)
        self.b8 = Button(self.controls,text="Update",
                         command= self.update_image,
                         height=BUTTON_HEIGHT).grid(row=EDIT_ROW,column=2,padx=10,pady=30)

        Label(self.controls, text='Old Image:',font=('arial 18')).grid(row=IMAGE_LABEL_ROW,column=0)
        
        self.old_image_label = Label(self.controls)
        self.old_image_label.grid(row=IMAGE_ROW,columnspan=5)
        print(self.old_image_label)

        self.c = Canvas(self.master,width=CANVAS_WIDTH,height=CANVAS_HEIGHT,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)

        imagemenu = Menu(menu)
        menu.add_cascade(label = "File",menu=imagemenu)
        imagemenu.add_command(label="Load Image",command = self.load_image)
        imagemenu.add_command(label="Save Image",command = self.save_image)
        imagemenu.add_command(label='Clear Canvas',command=self.clear)
        imagemenu.add_command(label='Exit',command=self.master.destroy) 

        #editmenu = Menu(menu)
        #menu.add_cascade(label = "Edit",menu = editmenu)
        #editmenu.add_command(label="Undo",command=self.undo)

        #colormenu = Menu(menu)
        #menu.add_cascade(label='Colors',menu=colormenu)
        #colormenu.add_command(label='Brush Color',command=self.change_fg)
        #colormenu.add_command(label='Background Color',command=self.change_bg)

        #optionmenu = Menu(menu)
        #menu.add_cascade(label='Options',menu=optionmenu)
        #optionmenu.add_command(label='Clear Canvas',command=self.clear)
        #optionmenu.add_command(label='Exit',command=self.master.destroy) 
        
        #shapesmenu = Menu(menu)
        #menu.add_cascade(label = "Shapes",menu = shapesmenu)
        #shapesmenu.add_command(label="Freehand",command=lambda : self.set_shape("freehand"))
        #shapesmenu.add_command(label="Rectangle",command=lambda : self.set_shape("rectangle"))
        #shapesmenu.add_command(label="Oval",command=lambda : self.set_shape("oval"))
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