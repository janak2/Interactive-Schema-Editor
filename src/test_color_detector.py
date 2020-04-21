# -*- coding: utf-8 -*-
from Code.src.main import *
from Code.src.config import *
from Code.src.color_detector import *

img = load_image("../data/Breaker Schematic Marked.png")
show_image(img)


cd = ColorDetector()
green_img, mask = cd.get_color_image(img, GREEN, COLOR_THRESHOLD['GREEN'])
show_image(green_img,"green")

