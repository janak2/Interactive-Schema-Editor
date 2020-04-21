import cv2
import numpy as np
from config import *

from Code.src.main import *


class ColorDetector:
    # returns all the pixels with a specific color

    def __init__(self):
        pass

    def get_color_image(self, image, color, COLOR_THRESHOLD):
        lower = np.array([color[0] - COLOR_THRESHOLD, color[1] - COLOR_THRESHOLD, color[2] - COLOR_THRESHOLD])
        upper = np.array([color[0] + COLOR_THRESHOLD, color[1] + COLOR_THRESHOLD, color[2] + COLOR_THRESHOLD])
        # lower = np.array([0,0,0])
        # upper = np.array([255,255,255])
        print(lower, upper)
        mask = cv2.inRange(image, lower, upper)
        # inv_mask = cv2.bitwise_not(mask)
        # print(mask)
        # masked = cv2.bitwise_and(image, image, mask = inv_mask)
        image[np.where((mask != [0]))] = [255, 255, 255]
        return image, mask
