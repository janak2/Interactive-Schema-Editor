import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from config import *
from old.color_detector import *
from old.line_detector import *
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


def load_image(path):
    if not os.path.isfile(path):
        raise Exception("Path doesnot exist.")
    img = cv2.imread(path)
    return img


def detect(marked_img):
    #cd = ColorDetector()
    #green_img, mask = cd.get_color_image(img, GREEN, COLOR_THRESHOLD['GREEN'])
    #show_image(green_img,"green")
    #hsv_img = LineDetector().convert_hsv(green_img)
    #show_image(hsv_img)
    #red_mask, masked_img = LineDetector().get_color(hsv_img)
    #show_image(masked_img)
    # convert all red into black on marked image and show new image
    #new_img = LineDetector().convert_color(green_img, red_mask)
    #show_image(new_img)
    #return new_img

    cd = Color()
    mask_green = cd.get_mask(marked_img, GREEN, COLOR_THRESHOLD['GREEN'], "BRG")
    marked_img_nogreen = cd.convert_color(marked_img, mask_green, 1)
    hsv_img = cd.convert_hsv(marked_img_nogreen)
    mask_red = cd.get_mask(hsv_img, RED, COLOR_THRESHOLD['RED'], "HSV")
    marked_img_nored_b = cd.convert_color(marked_img_nogreen, mask_red, 0)
    marked_img_nored_w = cd.convert_color(marked_img_nogreen, mask_red, 1)
    mask_red_invert = cd.invert_color(mask_red)

    cd = Text()
    marked_img_text = cd.get_text(mask_red_invert, marked_img_nogreen, marked_img_nored_w)
        
    ct = Template()
    temp_img = ct.match_template(marked_img_text, mask_red_invert)
    #show_image(temp_img)

    return temp_img


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
    img = save_image(save_name, img)
    

if __name__ == "__main__":
    pass
