import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import io
import numpy
import cv2


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
        #process(file.name)
        self.load_image(file.name) 
        
    def update_image(self,process,old_image_label,width,height):
        ps = self.c.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        
        img_small = img.resize((width,height),Image.ANTIALIAS)
        
        img2 = ImageTk.PhotoImage(img_small)
        old_image_label.configure(image = img2)
        old_image_label.image = img2
        #pil_image = img.convert('RGB') 
        numpy_image = numpy.array(img) 
        # Convert RGB to BGR 
        open_cv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
        open_cv_image = process(open_cv_image)
        numpy_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(numpy_image)
        self.img = img.resize((self.c.winfo_width(), self.c.winfo_height()), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.tatras = ImageTk.PhotoImage(self.img)
        image = self.c.create_image(0,0, anchor=NW, image=self.tatras)

        
if __name__ == "__main__":
    ih = ImageHandler()
        

        