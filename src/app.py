import tkinter as tk
from tkinter import *
from tkinter import ttk, colorchooser,filedialog
import glob
from PIL import Image, ImageTk
import io
from main import process


CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 800
undo_list = []

class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)#drwaing the line 
        self.c.bind('<ButtonRelease-1>',self.reset)

    def paint(self,e):
        if self.old_x and self.old_y:
            line = self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)
            if len(undo_list) == 0:
                undo_list.append([])
            undo_list[-1].append(line)
            
        self.old_x = e.x
        self.old_y = e.y

    def reset(self,e):    #reseting or cleaning the canvas 
        self.old_x = None
        self.old_y = None
        undo_list.append([])

    def changeW(self,e): #change Width of pen through slider
        self.penwidth = e
           

    def clear(self):
        self.c.delete(ALL)
        undo_list = []

    def change_fg(self):  #changing the pen color
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):  #changing the background color canvas
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg
        
    def load_image(self,filename=""):
        #print("loading image:",i)
        if filename == "":
            filename = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
            print(filename)
        #img = PhotoImg("<path/to/image_file>.gif")
        self.img = Image.open(filename) 
        self.img = self.img.resize((CANVAS_WIDTH, CANVAS_HEIGHT), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.tatras = ImageTk.PhotoImage(self.img)
        image = self.c.create_image(0,0, anchor=NW, image=self.tatras)
        #undo_list.append(image)
        #self.tatras.pack(fill=BOTH)
        
    def save_image(self):
        files = [('Image', '*.png')] 
        file = filedialog.asksaveasfile(filetypes = files, defaultextension = files) 
        print(file)
        ps = self.c.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))     
        img.save(file.name)
        process(file.name)
        self.load_image(file.name) 

            
    def undo(self):
        obj = undo_list.pop()
        for i in obj:
            self.c.delete(i)
        
    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Pen Width:',font=('arial 18')).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 2, to = 50,command=self.changeW,orient=VERTICAL)
        self.slider.set(self.penwidth)
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