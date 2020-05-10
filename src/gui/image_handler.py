import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import io


class ImageHandler:
    
    def __init__(self,canvas):
        self.c = canvas
        
    def load_image(self,filename=""):
        if filename == "":
            filename = filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
            print(filename)
        #img = PhotoImg("<path/to/image_file>.gif")
        self.img = Image.open(filename) 
        self.img = self.img.resize((self.c.winfo_width(), self.c.winfo_height()), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.tatras = ImageTk.PhotoImage(self.img)
        image = self.c.create_image(0,0, anchor=NW, image=self.tatras)
        
    def save_image(self,process):
        files = [('Image', '*.png')] 
        file = filedialog.asksaveasfile(filetypes = files, defaultextension = files) 
        print(file)
        ps = self.c.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))     
        img.save(file.name)
        process(file.name)
        self.load_image(file.name) 

        