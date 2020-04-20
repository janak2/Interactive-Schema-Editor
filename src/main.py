import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


def load_image(path):
    if not os.path.isfile(path):
        raise Exception("Path doesnot exist.")
    img = cv2.imread(path)
    return img

def detect():
    pass

def save_image(path,img):
    cv2.imwrite(path,img)

def show_image(img,name=""):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis("off")
    plt.show()    


if __name__ == "__main__":
    pass