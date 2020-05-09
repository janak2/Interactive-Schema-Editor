# -*- coding: utf-8 -*-
from main import *
from config import *
from color_detector import *

img = load_image("../data/Breaker Schematic Marked.png")
show_image(img)


cd = ColorDetector()
green_img, mask = cd.get_color_image(img, GREEN)
show_image(green_img,"green")

