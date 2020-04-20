import cv2
import numpy as np
from Code.src.config import *


class LineDetector:
    def get_color(self, image):
        # red color mask
        lower = np.uint8([255, 100, 100])
        upper = np.uint8([255, 255, 255])
        red_mask = cv2.inRange(image, lower, upper)
        # combine the mask
        masked = cv2.bitwise_and(image, image, mask=red_mask)
        return masked

    def convert_gray_scale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    def apply_smoothing(self, image, kernel_size=15):
        """
        kernel_size must be positive and odd
        """
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    def detect_edges(self, image, low_threshold=50, high_threshold=150):
        return cv2.Canny(image, low_threshold, high_threshold)

    def hough_lines(self, image):
        """
        `image` should be the output of a Canny transform.

        Returns hough lines (not the image with lines)
        """
        return cv2.HoughLinesP(image, rho=1, theta=np.pi / 180, threshold=20, minLineLength=20, maxLineGap=300)

    def draw_lines(self, image, lines, color=[255, 0, 0], thickness=2, make_copy=True):
        # the lines returned by cv2.HoughLinesP has the shape (-1, 1, 4)
        if make_copy:
            image = np.copy(image)  # don't want to modify the original
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(image, (x1, y1), (x2, y2), color, thickness)
        return image

#    def __init__(self):
#        pass

#    def detect(self):
#        pass

#    def get_corners(self):
#        pass

#    def get_length(self):
#        pass
