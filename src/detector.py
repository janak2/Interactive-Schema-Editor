import cv2
import pytesseract
import numpy as np
from config import *
from main import *


class Color:
    def __init__(self):
        pass

    def get_mask(self, image, color, COLOR_THRESHOLD, img_format):
        if img_format == "BRG":
            # Sets thresholds for colour detection
            lower = np.array([color[0] - COLOR_THRESHOLD, color[1] - COLOR_THRESHOLD, color[2] - COLOR_THRESHOLD])
            upper = np.array([color[0] + COLOR_THRESHOLD, color[1] + COLOR_THRESHOLD, color[2] + COLOR_THRESHOLD])

            # Creates new image file tha contains White pixels for selected color and black for all other pixels
            mask = cv2.inRange(image, lower, upper)
        elif img_format == "HSV":
            lower = np.array([90, 70, 170])
            upper = np.array([150, 255, 255])
            mask = cv2.inRange(image, lower, upper)
        return mask

    def convert_color(self, image, mask, white):
        if white == 1:
            image[np.where((mask != [0]))] = [255, 255, 255]
        elif white == 0:
            image[np.where((mask != [0]))] = [0, 0, 0]
        return image

    def invert_color(self, image):
        return 255 - image

    def convert_hsv(self, image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    def convert_hls(self, image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2HLS)

    def convert_gray_scale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


class Text:
    def __init__(self):
        pass

    def get_text(self, gray, marked, blank):
        # Mention the installed location of Tesseract-OCR in your system
        global pix
        #pytesseract.pytesseract.tesseract_cmd = '../tesseract/4.1.1/bin/tesseract'

        # Convert the image to gray scale
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Performing OTSU threshold
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

        # Specify structure shape and kernel size.
        # Kernel size increases or decreases the area
        # of the rectangle to be detected.
        # A smaller value like (10, 10) will detect
        # each word instead of a sentence.
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))

        # Applying dilation on the threshold image
        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

        # Finding contours
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        im2 = marked

        # A text file is created and flushed
        file = open("recognized.csv", "w+")
        file.write("")
        file.close()

        # Looping through the identified contours
        # Then rectangular part is cropped and passed on
        # to pytesseract for extracting text from it
        # Extracted text is then written into the text file
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)

            # Drawing a rectangle on copied image
            #rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Cropping the text block for giving input to OCR
            cropped = gray[y:y + h, x:x + w]

            # Open the file in append mode
            file = open("recognized.csv", "a")

            # Apply OCR on the cropped image
            text = pytesseract.image_to_string(cropped)
            text_lists = text.split("-\n")
            # print(text)

            new_img = blank
            if text != "":
                #rect = cv2.rectangle(new_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                #print("text")
                line_counter = 1
                for text_line in text_lists:
                    font = cv2.FONT_HERSHEY_SIMPLEX  # Select Font
                    new_img = cv2.putText(new_img, text_line, (x + 3, y + (11 * line_counter)), font, .33, (0, 0, 0), 1)
                    # show_image(blank)
                    line_counter = line_counter + 1
            else:
                #print("no text")
                for row in range(0, len(new_img)):
                    for col in range(0, len(new_img[0])):
                        # print(y,row,y+h)
                        # print(x,col,x+h)
                        # show_image(new_img)
                        if y < row < y + h and x < col < x + w:
                            pix = 255
                            if gray[row][col] == 0:
                                pix = 0
                            new_img[row][col] = pix

            # Appending the text into file
            file.write(text)
            file.write("\n")

            # Close the file
            file.close
        return new_img


class Line:
    def __init__(self):
        pass

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
            line = list(line)
            print(line)
            x1, y1, x2, y2 = line
            cv2.line(image, (x1, y1), (x2, y2), color, thickness)
        return image
