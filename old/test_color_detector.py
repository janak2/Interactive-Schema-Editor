# -*- coding: utf-8 -*-
from main import *
from config import *
from color_detector import *

img = load_image("../data/Breaker Schematic Marked.png")
show_image(img)


cd = ColorDetector()
green_img, mask = cd.get_color_image(img, GREEN, COLOR_THRESHOLD['GREEN'])
show_image(green_img,"green")
#save_image("../data/test3.png",green_img)

process("../data/Breaker Schematic Marked.png","../data/Breaker Schematic Marked2.png")

