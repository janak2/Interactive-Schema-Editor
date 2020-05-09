import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
<<<<<<< Updated upstream


=======
from config import *
from detector import *


def load_image_list():
    path_list = ["../data/Breaker Schematic.png",
                 "../data/Breaker Schematic Marked.png",
                 "../data/One Line.png",
                 "../data/One Line Marked.png"]

    img_list = []
    for path in path_list:
        if not os.path.isfile(path):
            raise Exception("Path doesnot exist.")
        img_list.append(cv2.imread(path))
    return img_list


>>>>>>> Stashed changes
def load_image(path):
    if not os.path.isfile(path):
        raise Exception("Path doesnot exist.")
    img = cv2.imread(path)
    return img

<<<<<<< Updated upstream
def detect():
    pass
=======

def detect(img):
    cd = Color()
    # green_img, mask = cd.get_color_image(img, GREEN, COLOR_THRESHOLD['GREEN'])
    mask_green = cd.get_mask(img, GREEN, COLOR_THRESHOLD['GREEN'], "BRG")
    marked_img_nogreen = cd.convert_color(img, mask_green, 1)
    # show_image(mask_green)
    # show_image(marked_img_nogreen)

    # show_image(green_img,"green")
    return marked_img_nogreen


def save_image(path, img):
    cv2.imwrite(path, img)
>>>>>>> Stashed changes

def save_image(path,img):
    cv2.imwrite(path,img)

def show_image(img,name=""):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis("off")
    plt.show()    

<<<<<<< Updated upstream
=======

def process(path, save_name=""):
    img = load_image(path)
    img = detect(img)
    if save_name == "":
        save_name = path
    img = save_image(save_name, img)

>>>>>>> Stashed changes

if __name__ == "__main__":
    pass