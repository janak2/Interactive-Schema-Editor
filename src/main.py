import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from config import *
from color_detector import *


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

def load_image(path):
    if not os.path.isfile(path):
        raise Exception("Path doesnot exist.")
    img = cv2.imread(path)
    return img

def detect(img):
    cd = ColorDetector()
    green_img, mask = cd.get_color_image(img, GREEN, COLOR_THRESHOLD['GREEN'])
    #show_image(green_img,"green")
    return green_img


def save_image(path, img):
    cv2.imwrite(path, img)


def show_image(img: object, name: object = "") -> object:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis("off")
    plt.show()

def process(path,save_name=""):
    img = load_image(path)
    img = detect(img)
    if save_name == "":
        save_name = path
    img = save_image(save_name,img)

if __name__ == "__main__":
    pass
