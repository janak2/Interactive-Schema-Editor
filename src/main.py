import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

def load_images():
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

def detect():
    pass


def save_image(path, img):
    cv2.imwrite(path, img)


def show_image(img: object, name: object = "") -> object:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    pass
